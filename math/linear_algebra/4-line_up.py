#!/usr/bin/env python3
"""docs"""
new = []
def add_arrays(arr1, arr2):
    """addition of array"""
    if len(arr1) != len(arr2):
        return None
    else:
        for i in range(len(arr1)):
            new.append(arr1[i] + arr2[i])
    return new
