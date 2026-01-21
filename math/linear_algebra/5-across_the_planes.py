#!/usr/bin/env python3
"""docs of this file"""


def add_matrices2D(arr1, arr2):
    """addition of array"""
    new = []
    if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]):
        return None
    else:
        for i in range(len(arr1)):
            '''appending function'''
            x = []
            for j in range(len(arr1[0])):
                '''new appending functiion'''
                x.append(arr1[i][j] + arr2[i][j])
            new.append(x)
    return new
