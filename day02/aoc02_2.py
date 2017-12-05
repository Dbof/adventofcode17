#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import itertools


def checksum(text):
    lines = text.split('\n')
    chksum = 0
    for l in lines:
        data = [int(x) for x in l.strip().split('\t')]
        perm = itertools.permutations(data, 2)
        chksum += [a//b for a,b in perm if a % b == 0][0]
    return chksum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<input>')
        exit(1)

    with open(sys.argv[1]) as f:
        result = checksum(f.read().strip())
        print('Result:', result)
