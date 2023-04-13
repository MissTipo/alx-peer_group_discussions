#!/usr/bin/python3
""""""
# read from stdin
# for line in stdin, check if format is , else skip
# declare a counter variable that increments, check if the counter is 10, 
# calculate 
# declare a dict for storing the status codes {ststus code}
# declare a variable to store the file size
# every time a line is read, check if key is availale in dict
# update file size
# print file size
# if !key || !value, continue
# else print status code
# 
import re
import sys

status_dict = {200: 0, 301:0, 400:0, 401:0, 403:0, 405:0, 500:0}
stdin = sys.stdin 
counter = 0
total_file_size = 0

try:
    for line in stdin:
        output = line.split()
        if int(output[-2]) in status_dict.keys() and len(output) == 9:
            counter += 1
            status_dict[int(output[-2])] += 1
            total_file_size += int(output[-1])
        if counter % 10 == 0:
            print('File size: {}'.format(total_file_size))
            for key, value in status_dict.items():
                if value:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt as error:
            print('File size: {}'.format(total_file_size))
            for key, value in status_dict.items():
                print("{}: {}".format(key, value))
