# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 11:23:59 2018

@author: Administrator
"""

class Solution:
    def Fibonacci(self, n):
        # write code here
        if(n ==0):
            return 0
        if(n==1):
            return 1
        f1=0
        f2=1
        for i in xrange(n-1):
            ret=f1+f2
            f1=f2
            f2=ret
        return ret