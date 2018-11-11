# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 00:10:52 2018

@author: Administrator
"""

class BinTNode:
    def __init__ (self, dat, left = None, right = None):
        self.data = dat
        self.left = left
        self.right = right
    
    
         
def count_BinTNodes(t):
        if t is None:
            return 0
        else:
            return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)
        
def sum_BinTNodes(t):
        if t is None:
            return 0
        else:
            return t.data + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)        

def preorder(t,proc):
    assert(isinstance(t, BinTNode)) #对于链接树对象才可继续
    if t is None:
        return
    proc(t.data)
    preorder(t.left)
    preorder(t.right)
    
def print_BinTNodes(t):
    if t is None:
        print("^") #空树输出^
        return
    print("(" + str(t.data))
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(")")
    
    
if __name__ == "__main__":
    t = BinTNode(1, BinTNode(2), BinTNode(3))
    print (count_BinTNodes(t))
    print(sum_BinTNodes(t))
    print_BinTNodes(t)