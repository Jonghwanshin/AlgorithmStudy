#!/usr/bin/python

import sys
import copy

dirs = [ [-1,-1], [0,-1], [1,-1], [-1,0], [1,0], [-1,1], [0,1], [1,1] ]
remain_init = [ [1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1] ]

def find(y, x, w, bl, remain):
	for d in dirs:
		nx = x+d[0]
		ny = y+d[1]
		if ny > -1 and nx > -1 and ny < 5 and nx < 5 and remain[ny][nx] == 1:
			if bl[ny][nx] == w[0]:
				if len(w) == 1:
					return True
				else:
					return find(ny, nx, w[1:], bl, remain)
			elif bl[ny][nx] not in w[1:]:
					remain[ny][nx] = -1				
	return False

rl = lambda: sys.stdin.readline()
n = int(rl())
for ci in range(n):
	bl = []
	wl = []
	for bi in range(5):
		bl.append(rl().strip())
	n = int(rl())
	for wi in range(n):
		wl.append(rl().strip())
	for w in wl:
		find_flag = False
		for y, b in enumerate(bl):
			if w[0] in b:
				remain = copy.deepcopy(remain_init)
				x = b.index(w[0])
				ret = find(y, x, w[1:], bl, remain)
				if ret == True:
					find_flag = True
					break
		if find_flag == True:
			print w + ' ' + "YES"
		else:
			print w + ' ' + "NO"
