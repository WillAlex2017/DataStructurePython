# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 16:01:18 2018

@author: Administrator
"""

    count=0
    while n!=0:
        n= n & (n-1)
        count=count+1
    return count