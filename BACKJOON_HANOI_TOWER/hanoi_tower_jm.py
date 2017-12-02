#!/usr/bin/env python

rl = lambda: raw_input().strip()
ndisks = int(rl())
phase = 0

def hanoiRecursive(ndisks, startPeg=1, endPeg=3):
	global phase
	if ndisks:
		extraPeg = 6 - endPeg - startPeg
		hanoiRecursive(ndisks-1, startPeg, extraPeg)
		# print ' '.join([str(ndisks), "'s disk moving.."])
		print ' '.join([str(startPeg), str(endPeg)])
		hanoiRecursive(ndisks-1, extraPeg , endPeg)
		phase += 1

hanoiRecursive(ndisks)
print phase
