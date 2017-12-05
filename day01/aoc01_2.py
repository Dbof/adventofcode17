#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def digit_sum(text):
    # make sum of characters
    sum = 0
    mid = (int)(len(text)/2)
    for i in range(0, len(text)):
        if text[i] == text[i-mid]:
            sum += (int)(text[i])
    return sum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<input>')
        exit(1)

    with open(sys.argv[1]) as f:
        result = digit_sum(f.read().strip())
        print('Result:', result)
