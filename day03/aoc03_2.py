#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math


def print_grid(grid):
    for row in grid:
        print('[', end='\t')
        for x in row:
            print(str(x), end='\t')
        print(']')
    print()


def find_value(grid, value):
    for g in grid:
        for x in reversed(g):
            if x >= value:
                return x
    return None

def calc(grid, x, y):
    indices = [-1, 0, 1]
    sum = 0
    for dy in indices:
        for dx in indices:
            try:
                ynew, xnew = y+dy, x+dx
                val = 0
                if ynew < 0 or xnew < 0:
                    raise IndexError

                val = grid[ynew][xnew]
                sum += val
            except IndexError:
                pass
    return sum

def fill_grid(grid, width):
    mid = width // 2
    grid[mid][mid] = 1

    x = y = mid
    # starting ring
    ring = 0

    for roundx in range(mid):
        ring += 2
        x += 1
        turn = 'u'

        while (turn != 's'):
            if turn == 'u':
                for i in range(ring):
                    grid[y][x] = calc(grid, x, y)
                    y -= 1
                y += 1
                turn = 'l'
                x -= 1
            elif turn == 'l':
                for i in range(ring):
                    grid[y][x] = calc(grid, x, y)
                    x -= 1
                x += 1
                turn = 'd'
                y += 1
            elif turn == 'd':
                for i in range(ring):
                    grid[y][x] = calc(grid, x, y)
                    y += 1
                y -= 1
                turn = 'r'
                x += 1
            elif turn == 'r':
                for i in range(ring):
                    grid[y][x] = calc(grid, x, y)
                    x += 1
                x -= 1
                turn = 's'
                y -= 1
        y += 1


def create_spiral(rings):
    width = rings*2-1
    grid = [[0 for x in range(0, width)] for y in range(0, width)]
    fill_grid(grid, width)
    return grid


def distance(inp):
    max_val = int(inp)

    i = 1
    while(True):
        grid = create_spiral(i)
        big_val = find_value(grid, max_val)
        if big_val != None:
            print_grid(grid)
            return 'Possibly {}, but check the table.'.format(big_val)
        i += 1

    return None


if __name__ == "__main__":
    if len(sys.argv) != 2 or int(sys.argv[1]) <= 0:
        print('Usage:', sys.argv[0], '<input>')
        exit(1)

    result = distance(sys.argv[1])
    print('Result:', result)
