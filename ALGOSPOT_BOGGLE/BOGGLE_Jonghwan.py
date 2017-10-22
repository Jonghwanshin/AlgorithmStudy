#!/usr/bin/python

import timeit
start = timeit.default_timer()

import sys
import copy

dirs = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

def find(word, block):
    cache = [[[int(0) for z in range(10)] for y in range(5)] for x in range(5)]
    for wIdx, w in enumerate(word):
        coudlntFind = True
        for y in range(5):
            for x in range(5):
                if block[y][x] == w:
                    coudlntFind = False
                    if wIdx == 0:
                        cache[y][x][wIdx] = 1
                    else:
                        for d in dirs:
                            if y+d[1] >=0 and y+d[1] <= 4 and x+d[0] >=0 and x+d[0] <= 4: 
                                if(cache[y+d[1]][x + d[0]][wIdx-1]):
                                    cache[y][x][wIdx] = 1
                                    if wIdx == len(word) -1:
                                        return True
        if coudlntFind: 
            return False
                

def readLine(): return sys.stdin.readline()

n = int(readLine())
for ci in range(n):
    blocklist = []
    wordlist = []
    for bi in range(5):
        blocklist.append(readLine().strip())
    n = int(readLine())
    for wi in range(n):
        wordlist.append(readLine().strip())
    for word in wordlist:
        find_flag = False
        #print(word)
        find_flag = find(word, blocklist)
        if find_flag:
            print word + ' ' + "YES"
        else:
            print word + ' ' + "NO"

end = timeit.default_timer()
print end - start
