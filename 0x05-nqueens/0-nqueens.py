#!/usr/bin/python3
""" nqueens project """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)


def solve_func(n):
    """ solve func """
    j = 0
    m = []
    for solution in q_func(n, 0):
        for s in solution:
            m.append([j, s])
            j += 1
        print(m)
        m = []
        j = 0


def q_func(n, i=0, a=[], b=[], c=[]):
    """ possible positions finder """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from q_func(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


num = int(sys.argv[1])
solve_func(num)
