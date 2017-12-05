#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import itertools


def has_anagram(phrase):
    words = phrase.split(' ')
    combinations = [(w1, w2) for w1, w2 in itertools.combinations(words, 2)
                    if sorted(w1) == sorted(w2)]
    return len(combinations) > 0


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
        if not has_duplicate(p) and not has_anagram(p):
            count += 1
    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<input>')
        exit(1)

    with open(sys.argv[1]) as f:
        result = check(f.read().strip())
        print('Result:', result)
