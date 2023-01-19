import sys
import re

test = re.search('(\d+.\d+.\d+.\d+) - .+ (\d{3}) (\d+)$', '14.193.229.164 - [2023-01-19 21:35:13.589212] "GET /projects/260 HTTP/1.1" 200 395')
IP = None
STATUS = None
FILE = None
TOTALFILE = 0
STATUSLIST = [200, 301, 400, 401, 403, 404, 405, 500]
STATUSCOUNTER = {}

for status in STATUSLIST:
    STATUSCOUNTER[status] = 0

def PRINTMSSG():
    sys.stdout.write('File size: {}'.format(TOTALFILE))
    for status in STATUSCOUNTER:
        if STATUSCOUNTER[status] != 0:
            sys.stdout.write('{}: {}'.format(status, STATUSCOUNTER[status]))

for line in sys.stdin:
    LINECOUNT = 0
    try:
        regex = re.search('(\d+.\d+.\d+.\d+) - .+ (\d{3}) (\d+)$', '14.193.229.164 - [2023-01-19 21:35:13.589212] "GET /projects/260 HTTP/1.1" 200 395')
        (IP, STATUS, FILE) = regex.group(1), regex.group(2), regex.group(3)
        if None not in (IP, STATUS, FILE):
            TOTALFILE += int(FILE)
            if STATUS in STATUSLIST:
                STATUSCOUNTER[STATUS] += 1
        if LINECOUNT == 10:
            PRINTMSSG()
            LINECOUNT = 0
        else:
            LINECOUNT += 1
    except KeyboardInterrupt:
        PRINTMSSG()
        break