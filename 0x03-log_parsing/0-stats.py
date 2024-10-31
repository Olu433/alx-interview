#!/usr/bin/python3

import sys


def print_msg(dict_sc, total_file_size):
    """
    Method to print the metrics.
    Args:
        dict_sc: dict of status codes
        total_file_size: total size of files processed
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        if len(parsed_line) > 1:
            counter += 1

            # Update total file size
            total_file_size += int(parsed_line[-1])

            # Update status code count
            code = parsed_line[-2]
            if code in dict_sc:
                dict_sc[code] += 1

            # Print stats every 10 lines
            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    # Ensure statistics are printed if interrupted
    print_msg(dict_sc, total_file_size)
