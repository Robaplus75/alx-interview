#!/usr/bin/python3

import sys


def print_msg(dict_sc, total_file_size):
    """
    logparsing func
    """

    print("File size: {}".format(total_file_size))
    for k, v in sorted(dict_sc.items()):
        if v != 0:
            print("{}: {}".format(k, v))


dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}
code = 0
c = 0
sum_size = 0

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            c += 1

            if c <= 10:
                sum_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in dict_sc.keys()):
                    dict_sc[code] += 1

            if (c == 10):
                print_msg(dict_sc, sum_size)
                c = 0

finally:
    print_msg(dict_sc, sum_size)
