#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def checksum(text):
    lines = text.split('\n')
    chksum = 0
    for l in lines:
        data = [int(x) for x in l.strip().split('\t')]
        chksum += max(data) - min(data)

    return chksum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<input>')
        exit(1)

    with open(sys.argv[1]) as f:
        result = checksum(f.read().strip())
        print('Result:', result)
