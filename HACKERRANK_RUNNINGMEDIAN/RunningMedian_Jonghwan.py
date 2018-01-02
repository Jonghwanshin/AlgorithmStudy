#!/bin/python3
import sys
import heapq

class Heap:
    """Implementation of heap"""
#    heaplist = []
#    maxOrMin = 'max'
    def __init__(self):
        self.heaplist=[]
        self.maxOrMin = 'max'
        
    def setMaxOrMin(self, choice):
        self.maxOrMin = choice
    
    def add(self, newvalue):
        self.heaplist.append(newvalue)
        idx = len(self.heaplist) - 1
        parent_idx = (idx-1) >> 1
        if self.maxOrMin == 'min':
            while idx > 0 and self.heaplist[parent_idx] > self.heaplist[idx]:
                temp = self.heaplist[idx]
                self.heaplist[idx] = self.heaplist[parent_idx]
                self.heaplist[parent_idx] = temp
                idx = parent_idx
                parent_idx = (idx-1) >> 1 
        elif self.maxOrMin == 'max':
            while idx > 0 and self.heaplist[parent_idx] < self.heaplist[idx]:
                temp = self.heaplist[idx]
                self.heaplist[idx] = self.heaplist[parent_idx]
                self.heaplist[parent_idx] = temp
                idx = parent_idx
                parent_idx = (idx-1) >> 1
                
    def pop(self):
        res = self.heaplist.pop(0)
        if self.maxOrMin == 'min':
            here = 0
            while True:
                left = here*2 + 1
                right = here*2+2
                if(left >= len(self.heaplist)): break
                next_idx = here
                if(self.heaplist[next_idx] > self.heaplist[left]):
                    next_idx = left
                if(right < len(self.heaplist) and self.heaplist[next_idx] > self.heaplist[right]):
                    next_idx = right
                if(next_idx == here): break
                temp = self.heaplist[here]
                self.heaplist[here] = self.heaplist[next_idx]
                self.heaplist[next_idx] = temp
                here = next_idx
        elif self.maxOrMin == 'max':
            here = 0
            while True:
                left = here*2 + 1
                right = here*2+2
                if(left >= len(self.heaplist)): break
                next_idx = here
                if(self.heaplist[next_idx] < self.heaplist[left]):
                    next_idx = left
                if(right < len(self.heaplist) and self.heaplist[next_idx] < self.heaplist[right]):
                    next_idx = right
                if(next_idx == here): break
                temp = self.heaplist[here]
                self.heaplist[here] = self.heaplist[next_idx]
                self.heaplist[next_idx] = temp
                here = next_idx
        return res
    
    def size(self):
        return len(self.heaplist)
    
    def getHead(self):
        return self.heaplist[0]
    
    def getList(self):
        return self.heaplist
    
n = int(input().strip())
minHeap = Heap()
minHeap.setMaxOrMin('min')
maxHeap = Heap()
a_i = 0
ret = 0
for a_i in range(1,n+1):
    a_t = int(input().strip())
    
    if(maxHeap.size() == 0):
        maxHeap.add(a_t)
    elif(maxHeap.getHead() < a_t):
        maxHeap.add(a_t)
    else:
        minHeap.add(a_t)
    
    #balancing the heap
    sizediff = minHeap.size() - maxHeap.size()
    if(sizediff < -1):
        a = maxHeap.pop()
        minHeap.add(a)
    elif(sizediff >= 1):
        a = minHeap.pop()
        maxHeap.add(a)

    if(minHeap.size() != 0 and maxHeap.size() != 0 and minHeap.getHead() < maxHeap.getHead()):
        a = minHeap.pop() #swap
        b = maxHeap.pop()
        maxHeap.add(a)
        minHeap.add(b)
    
    sizediff = minHeap.size() - maxHeap.size()
    if(sizediff == 0):
        #print("same",sizediff)
        ret = (maxHeap.getHead() + minHeap.getHead())/2
    else:
        if(sizediff <= -1):
            ret = maxHeap.getHead()
        else:
            ret = minHeap.getHead()
    print(float(ret))
    #print(maxHeap.getList(), minHeap.getList())