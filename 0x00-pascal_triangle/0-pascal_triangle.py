#!/usr/bin/python3
"""Determinew q pascal triangle for of any length"""
def pascal_triangle(n):
    """
    returns a list of lists of integers representing the pascal triangle of length n
    """
    trgnl = []
    if n <= 0:
        return trgnl
    for i in range(n):
        tmp_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                tmp_list.append(1)
            else:
                tmp_list.append(trgnl[i-1][j-1] + trgnl[i-1][j])
        trgnl.append(temp_list)
    return trgnl
