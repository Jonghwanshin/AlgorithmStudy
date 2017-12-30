#!/usr/bin/env python

def selection() :
	last = n
	while(last > 1) :
		# ---------
		# find max
		# ---------
		maxnum = -1001
		maxnum_idx = -1001
		for idx in xrange(last) : 
			curnum = num_raw[idx]
			if maxnum < curnum :
				maxnum = curnum 
				maxnum_idx = idx
		
		# ------------
		# max to last
		# ------------
		num_raw[maxnum_idx] = num_raw[last-1]
		num_raw[last-1] = maxnum

		last -= 1
		

def bubble() :
	last = n
	while(last > 1) :
		# ----------------------
		# find larger with next 
		# ----------------------
		for idx in xrange(last) :
			curnum = num_raw[idx]
			if idx != last-1 and curnum > num_raw[idx+1] :
				num_raw[idx] = num_raw[idx+1]
				num_raw[idx+1] = curnum

		last -= 1
		

rl = lambda: raw_input().strip()
n = int(rl())

num_raw = []
for i in xrange(n) :
	num_raw.append(int(rl()))

#selection()
bubble()
for num in num_raw :
	print num
