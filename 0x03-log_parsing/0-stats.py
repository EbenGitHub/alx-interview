#!/usr/bin/python3
"""Log Parsing for parsing sys inputs using sys stdout and sys stdin"""

import sys
import re

total_file_size = 0
status_lists = [200, 301, 400, 401, 403, 404, 405, 500]
status_counter = {}
regex = re.compile(r'(\d+.\d+.\d+.\d+) - .+ (\d{3}) (\d+)$')

for status in status_lists:
    status_counter[status] = 0


def print_mssg():
    sys.stdout.write('File size: {}\n'.format(total_file_size))
    for status in status_counter:
        if status_counter[status] != 0:
            sys.stdout.write('{}: {}\n'.format(status, status_counter[status]))


try:
    line_counter = 0
    for line in sys.stdin:
        if line:
            regex_result = regex.search(line)
            if regex_result:
                (ip, status_code, file_size) = \
                    regex_result.group(1), regex_result.group(2), \
                    regex_result.group(3)
                if None not in (ip, status_code, file_size):
                    total_file_size += int(file_size)
                    status_code = int(status_code)
                    if status_code in status_lists:
                        status_counter[status_code] += 1
                        line_counter += 1
                    if line_counter == 10:
                        print_mssg()
                        line_counter = 0                        
            regex_result = None
except KeyboardInterrupt:
    print_mssg()
