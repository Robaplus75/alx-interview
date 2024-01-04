#!/usr/bin/python3
''' pascal triangle'''

def pascal_triangle(k):
    ''' pascal triangle func'''
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
