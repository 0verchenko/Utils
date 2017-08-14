#! Python3
# PhoneAndEmail.py - Find phone numbers (in US format) and emails in a buffer.


import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # country code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first three digits 
    (\s|-|\.)                           # separator
    (\d{4})                             # last four digits
    (\s* (ext|x|ext.)\s*(\d{2,5}))?     # additional number
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-z0-9._%+-]+      # username
    @                   # at symbol
    [a-z0-9.-]+         # domain name
    (\.[a-z]{2,4})      # last part of email
)''', re.VERBOSE | re.I)


# Find matches in buffered text

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# Copy results to buffer

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to buffer:')
    print('\n'.join(matches))
else:
    print('Phones and Emails not found.')

