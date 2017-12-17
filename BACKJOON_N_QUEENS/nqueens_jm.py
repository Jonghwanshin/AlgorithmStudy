#!/usr/bin/env python

rl = lambda: raw_input().strip()
n = int(rl())

queen_columns = {}
res = 0

def addQueen(y) :
	global res

	# bottom of board
	if y == n:
		return True 


	for x in xrange(n) :
		next_flag = False

		# check columns
		if x in queen_columns.values() :
			next_flag = True

		# check diagonals
		for qy in queen_columns :
			if (y - qy) == abs(x - queen_columns[qy]) :
				next_flag = True
				
		if next_flag == False : 
			queen_columns[y] = x 
			if addQueen(y+1) :
				res += 1

		if y in queen_columns :
			del queen_columns[y]
addQueen(0)
print res
