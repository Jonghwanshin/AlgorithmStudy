#!/usr/bin/env python

import math

def mergesort(front, last) :
	if front < last :
		half = math.floor( (front + last) / 2 )
		mergesort(front, half)
		mergesort(half + 1, last)
		merge(front, half, last)
		
def merge(front, half, last) :
	i = front
	j = half + 1
	k = front

	temp = [0 for x in range(n)]
	while(i <= half and j <= last) : 
		if num_raw[i] <= num_raw[j] : 
			temp[k] = num_raw[i]
			i += 1
		else :	
			temp[k] = num_raw[j]
			j += 1
		k += 1

	while(i <= half) :
		temp[k] = num_raw[i]
		i += 1
		k += 1
	while(j <= last) :
		temp[k] = num_raw[j]
		j += 1
		k += 1
	
	for i in range(front, last+1) :
		num_raw[i] = temp[i]

	
rl = lambda: input()
n = int(rl())

num_raw = []
for i in range(n) :
	num_raw.append(int(rl()))

mergesort(0, n-1)
for num in num_raw :
	print(num)
