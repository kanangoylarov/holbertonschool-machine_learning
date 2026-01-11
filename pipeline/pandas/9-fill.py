#!/usr/bin/env python3
"""
9-fill.py
"""


def fill(df):
    """
    Removes the 'Weighted_Price' column and fills missing values:
    - 'Close': forward fill (previous row's value)
    - 'High', 'Low', 'Open': filled with the row's 'Close'
    - 'Volume_(BTC)', 'Volume_(Currency)': filled with 0

    Returns the modified DataFrame.
    """

    if 'Weighted_Price' in df.columns:
        df = df.drop(columns=['Weighted_Price'])


    df['Close'] = df['Close'].fillna(method='ffill')


    for col in ['High', 'Low', 'Open']:
        if col in df.columns:
            df[col] = df[col].fillna(df['Close'])

    for col in ['Volume_(BTC)', 'Volume_(Currency)']:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    return df
