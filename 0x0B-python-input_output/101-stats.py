#!/usr/bin/python3
''' module: 101-stats
'''


import signal
import sys

def print_stats(total_size, status_codes):
    """
    Prints statistics based on the accumulated data.
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes):
        print("{:d}: {:d}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).
    """
    print_stats(total_size, status_codes)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line_num, line in enumerate(sys.stdin, 1):
        data = line.split()
        if len(data) >= 8:
            total_size += int(data[-1])
            status_code = int(data[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1

        if line_num % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise
