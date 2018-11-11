# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 18:06:24 2018

@author: Administrator
"""
import random
class LNode:
    def __init__ (self, elem, next_ = None):
        self.elem = elem
        self.next = next_
        
    def length(head):
        p, n = head, 0
        while p is not None:
            n += 1
            p = p.next
        return n
class LinkedListUnderflow(ValueError):
    pass

class LList:
    def __init__ (self):
        self._head = None
    
    def is_empty(self):
        return self._head is None
    
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e
    
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
        
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p. next
        e = p.next.elem
        p.next = None
        return e
    
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem)
#            if p.next is not None:
#                print(', ')
            p = p.next
        print('')
        
class LList1(LList):
    def __init__ (self):
        LList.__init__(self)
        self._rear = None
    
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)
            
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next
            
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e
    
    def filter(self, pred): # 过滤器
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next
    
        
    
if __name__ == "__main__":
#    head = None
#    q = LNode(13)
#    q.next = head
#    head = q
#    print (head.elem)
#    llist1 = LNode(1)
#    p = llist1
#    for i in range(2,11):
#        p.next = LNode(i)
#        p = p.next
#        
#    p = llist1
#    while p is not None:
#        print(p.elem)
#        p = p.next
#    mlist1 = LList()
#    for i in range(10):
#        mlist1.prepend(i)
#    for i in range(11, 20):
#        mlist1.append(i)
#    mlist1.printall()
    
    mylist2 = LList1()
    mylist2.prepend(98)
    for i in range(11,20):
        mylist2.append(random.randint(1,20))
    
    for x in mylist2.filter(lambda y: y % 2 == 0):
        print(x)
        
    
    