#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:21:38 2020

@author: avni_aaron
"""


def my_map(val, start, fin, start2, fin2):
    out = val
    inFraction = (val - start) / (fin - start)
    print(inFraction)
    out += start2 - start
    out *= fin2 / fin
    return 
my_map(3, 2, 4, 0, 255)
my_map(0.75, 0, 1, 0, 255)
my_map(512, -1024, 1024, 0, 100)

#val =  0.5    start=0   fin=1     start2 = 0   fin2 = 255   expOut=127.5    actOut=127.5
#val =  3    start=2   fin=4     start2 = 0   fin2 = 255   expOut=127.5    actOut=
#val =  512    start=-1024   fin=1024     start2 = 0   fin2 = 100   expOut=75    actOut=