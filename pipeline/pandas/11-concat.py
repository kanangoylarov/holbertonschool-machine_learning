#!/usr/bin/env python3
"""
11-concat.py
"""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """
    Indexes both dataframes on 'Timestamp', filters df2 up to timestamp
    1417411920, concatenates df2 (bitstamp) on top of df1 (coinbase),
    and adds keys to distinguish the sources.

    Returns the concatenated DataFrame.
    """

    df1 = index(df1)
    df2 = index(df2)

    df2_filtered = df2.loc[:1417411920]

    result = pd.concat(
        [df2_filtered, df1],
        keys=['bitstamp', 'coinbase']
    )

    return result
