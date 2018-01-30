import random
import json
import datetime
import ssl
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


def change_host_file_configuration(for_disabling=False, path_to_hosts_file='C:\\Windows\\System32\\drivers\\etc\\hosts'):
    def check_if_hosts_file_hacked(path='C:\\Windows\\System32\\drivers\\etc\\hosts'):
        with open(path, 'r') as target_file:
            target_file_content = target_file.read()
            if 'android.googleapis.com' in target_file_content:
                return True
            else:
                return False
    try:
        if for_disabling:
            if not check_if_hosts_file_hacked(path=path_to_hosts_file):
                print('The "android.googleapis.com" record not in hosts file.')
                return True
            else:
                with open(path_to_hosts_file, 'r') as hosts_file:
                    hosts_file_content = hosts_file.readlines()
                with open(path_to_hosts_file, 'w') as hosts_file:
                    for line in hosts_file_content:
                        if 'android.googleapis.com' not in line:
                            hosts_file.write(line)
                if not check_if_hosts_file_hacked(path=path_to_hosts_file):
                    print('The "android.googleapis.com" record was removed from hosts file.')
                    return True
        else:
            if not check_if_hosts_file_hacked(path=path_to_hosts_file):
                with open(path_to_hosts_file, 'a') as hosts_file:

                    ################################################################################
                    ################################################################################
                    # Server ip that will be GCM imitator type below:
                    ################################################################################
                    ################################################################################
                    hosts_file.write('127.0.0.1    android.googleapis.com\n')
                if check_if_hosts_file_hacked(path=path_to_hosts_file):
                    print('The "android.googleapis.com" record was added to hosts file.')
                    return True
            else:
                print('The "android.googleapis.com" record is already in hosts file.')
                return False
    except IOError:
        print('Unable to check/modify hosts file.')
        return False

class Responce_Sender(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=UTF-8')
        self.send_header('Date', '%s' % datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT'))
        self.send_header('Expires', '%s' % datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT'))
        self.send_header('Cache-Control', 'private, max-age=0')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'SAMEORIGIN')
        self.send_header('Server', 'GSE')
        self.send_header('Alt-Svc', 'quic=":443"; ma=2592000; v="39,38,37,35"')
        self.send_header('Accept-Ranges', 'none')
        self.send_header('Vary', 'Accept-Encoding')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        print self.path
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)

        # print post_body
        try:
            json_request = eval(post_body)
            number_of_tokens = len(json_request['registration_ids'])
            print('number of tokens:%s' % number_of_tokens)
        except:
            print 'error happened'
            with open('logfile.txt', 'a') as logfile:
                logfile.write(post_body)
                return
        self._set_headers()
        multicast_id = random.randint(1000000000000000000, 9999999999999999999)
        message_id = int(str(multicast_id)[:16])

        post_responce = {
            "multicast_id": multicast_id,
            "success": number_of_tokens,
            "failure":0,
            "canonical_ids":0,
            "results": []}
        for x in range(number_of_tokens):
            post_responce["results"].append({"message_id": "0:{message_id}%8ad5829ef9fd7ecd".format(message_id=message_id + x)})
        print('Sending responce for %s tokens' % number_of_tokens)
        self.wfile.write(json.dumps(post_responce))


def run(server_class=HTTPServer, handler_class=Responce_Sender, port=2195):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile='server.pem', server_side=True)
    print '%s - starting httpd...' % datetime.datetime.now().strftime('%d %b %Y %H:%M:%S')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print '\t%s - stopping httpd.' % datetime.datetime.now().strftime('%d %b %Y %H:%M:%S')

if __name__ == "__main__":
    from sys import argv
    change_host_file_configuration()
    print('Starting http mock')
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
