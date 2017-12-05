#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def digit_sum(text):
    # make sum of characters
    sum = 0
    for i in range(0, len(text)-1):
        if text[i] == text[i+1]:
            sum += (int)(text[i])

    # check bounds
    if text[0] == text[-1]:
        sum += (int)(text[0])
    return sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<input>')
        exit(1)

    with open(sys.argv[1]) as f:
        result = digit_sum(f.read().strip())
        print('Result:', result)
