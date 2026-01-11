#!/usr/bin/env python3

'''
This is creating pandas dataframe from numpy array function file
'''
import pandas as pd


def from_numpy(array):

    '''
    Creating function for process
    '''

    order = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    df = pd.DataFrame(array, columns=order[:array.shape[1]])
    return df
