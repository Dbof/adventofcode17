#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def has_duplicate(phrase):
    seen = set()

    words = phrase.split(' ')
    for w in words:
        if w in seen:
            return True
        seen.add(w)
    return False


def check(text):
    count = 0
    phrases = text.split('\n')

    for p in phrases:
        if not has_duplicate(p):
            count += 1
    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<input>')
        exit(1)

    with open(sys.argv[1]) as f:
        result = check(f.read().strip())
        print('Result:', result)
