#!/usr/bin/python3

def pascal_triangle(k):
    res = []
    if k > 0:
        for i in range(1, k + 1):
            l = []
            a = 1
            for j in range(1, i + 1):
                l.append(a)
                a = a * (i - j) // j
            res.append(l)
    return res
