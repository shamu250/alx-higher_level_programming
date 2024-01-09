#!/usr/bin/python3
''' module: 101-stats
'''


import sys

def print_stats(total_size, status_codes):
    """
    Prints statistics based on the accumulated data.
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes):
        print("{:d}: {:d}".format(code, status_codes[code]))

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split(" ")
                size = int(parts[-1])
                status_code = int(parts[-2])

                total_size += size

                if status_code in status_codes:
                    status_codes[status_code] += 1

                count += 1

                if count % 10 == 0:
                    print_stats(total_size, status_codes)

            except (ValueError, IndexError):
                pass

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
