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


def fill_grid(grid, rings):
    n = len(rings)-1

    x = y = n
    grid[y][x] = rings[0][0]
    turn = 'u'

    for r in rings[1:]:
        x += 1
        r_next = 0

        length = len(r)//4

        for r_next in range(0, len(r), length):
            if turn == 'u':
                for i in range(0, length):
                    grid[y][x] = r[r_next+i]
                    y -= 1
                y += 1
                turn = 'l'
                x -= 1
            elif turn == 'l':
                for i in range(0, length):
                    grid[y][x] = r[r_next+i]
                    x -= 1
                x += 1
                turn = 'd'
                y += 1
            elif turn == 'd':
                for i in range(0, length):
                    grid[y][x] = r[r_next+i]
                    y += 1
                y -= 1
                turn = 'r'
                x += 1
            elif turn == 'r':
                for i in range(0, length):
                    grid[y][x] = r[r_next+i]
                    x += 1
                x -= 1
                turn = 'u'
                y -= 1

        y += 1


def get_position(grid, rings, number):
    for y in range(0, len(grid)):
        if number in grid[y]:
            x = grid[y].index(number)
            break

    return (x, y)


def create_spiral(rings):
    RING_NUM = math.ceil((math.sqrt(rings)+1) / 2)

    diagonals = [x*x for x in range(1, RING_NUM*2, 2)]
    rings = [[1]]

    for i in range(1, RING_NUM):
        l = list()
        for j in range(diagonals[i-1]+1, diagonals[i]+1):
            l.append(j)
        rings.append(l)

    width = int(math.sqrt(diagonals[-1]))
    grid = [[0 for x in range(0, width)] for y in range(0, width)]

    fill_grid(grid, rings)
    return (grid, rings)


def distance(inp):
    grid, rings = create_spiral(int(inp))
    # print_grid(grid)
    x, y = get_position(grid, rings, int(inp))
    null = len(rings)-1

    distance = abs(x-null) + abs(y-null)
    return distance


if __name__ == "__main__":
    if len(sys.argv) != 2 or int(sys.argv[1]) <= 0:
        print('Usage:', sys.argv[0], '<input>')
        exit(1)

    result = distance(sys.argv[1])
    print('Result:', result)
