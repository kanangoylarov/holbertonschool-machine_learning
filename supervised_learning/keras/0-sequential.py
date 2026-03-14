#!/usr/bin/env python3

'''
documented
'''
import tensorflow.keras as k

def build_model(nx, layers, activation, lambtha, keep_prob):
    '''
    doc
    '''
    model = [k.layers.Input(shape=(nx,))]
    for n, act in zip(layers, activation):
        model.append(k.layers.Dense(n, activation=act,
        kernel_regularizer=k.regularizers.l2(lambtha)))
        model.append(k.layers.Dropout(1 - keep_prob))
        model.pop()
    return k.Sequential(model)