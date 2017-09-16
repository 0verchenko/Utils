#! Python3
# renameDate.py - rename file name that include date in US format (MM-DD-YYYY)
# to EU format (DD-MM-YYYY)

import shutil, os, re

#Regex for US dates
datePattern = re.compile(r"""^(.*?)  # All text before date
    ((0|1)?\d)-                      # one or two month digits 
    ((0|1|2|3)?\d)-                  # one or two day digits
    ((19|20)\d\d)                    # four year digits
    (.*?)$                           # all text after date
    """, re.VERBOSE)

# Loop for files in working catalog
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Leave files with names than not include dates
    if mo == None:
        continue
    
    # Taking different parts of filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Forming names in EU format
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Taking fool absolute paths to files
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Renaming files
    print('Changing name "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)