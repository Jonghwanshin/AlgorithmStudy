#!/usr/bin/python

import timeit
start = timeit.default_timer()

import sys


def find(y, x, w, wi):
	if x < 0 or y < 0 or x > 4 or y > 4:
		return 0 
	
	if cache[y][x][wi] != -1:
		return cache[y][x][wi]

	if w[wi] != bl[y][x]:
		cache[y][x][wi] = 0
		return 0
	
	if len(w)-1 == wi:
		cache[y][x][wi] = 1
		return 1

	cache[x][y][wi] = find(y-1, x-1, w, wi+1) or \
			find(y-1, x, w, wi+1) or \
			find(y-1, x+1, w, wi+1) or \
			find(y, x-1, w, wi+1) or \
			find(y, x+1, w, wi+1) or \
			find(y+1, x-1, w, wi+1) or \
			find(y+1, x, w, wi+1) or \
			find(y+1, x+1, w, wi+1)
	return cache[x][y][wi]

rl = lambda: sys.stdin.readline()
n = int(rl())
bl = []
wl = []
cache = []
for tci in range(n):
	for bi in range(5):
		bl.insert(bi, rl().strip())
	n = int(rl())
	for wi in range(n):
		wl.insert(wi, rl().strip())
	for w in wl:
		cache = [[[-1 for val in range(10)] for x in range(5)] for y in range(5)]
		find_flag = False
		for y, b in enumerate(bl):
			for x, c in enumerate(b):
				ret = find(y, x, w, 0)
				if ret == 1:
					find_flag = True
					break
		if find_flag == True:
			print w + ' ' + "YES"
		else:
			print w + ' ' + "NO"

end = timeit.default_timer()
print(end - start)
