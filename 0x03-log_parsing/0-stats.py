#!/usr/bin/python3
"""Log Parsing for parsing sys inputs using sys stdout and sys stdin"""

import sys
import re

ip = None
status_code = None
file_size = None
total_file_size = 0
status_lists = [200, 301, 400, 401, 403, 404, 405, 500]
status_counter = {}

for status in status_lists:
    status_counter[status] = 0

def PRINTMSSG():
    sys.stdout.write('File size: {}\n'.format(total_file_size))
    for status in status_counter:
        if status_counter[status] != 0:
            sys.stdout.write('{}: {}\n'.format(status, status_counter[status]))

try:
    line_counter = 1
    for line in sys.stdin:
        if line:
            regex = re.search('(\d+.\d+.\d+.\d+) - .+ (\d{3}) (\d+)$', line)
            if regex:
                (ip, status_code, file_size) = regex.group(1), regex.group(2), regex.group(3)
                if None not in (ip, status_code, file_size):
                    total_file_size += int(file_size)
                    status_code = int(status_code)
                    if status_code in status_lists:
                        status_counter[status_code] += 1
                    if line_counter == 10:
                        PRINTMSSG()
                        line_counter = 1
                    else:
                        line_counter += 1
except KeyboardInterrupt:
    PRINTMSSG()
