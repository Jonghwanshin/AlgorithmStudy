#!/usr/bin/env python

names = []
volumes = []
values = []
max_val_cache = []
def pack(capacity, idx):
	if idx == len(names)-1:
		return 0 
	ret = max_val_cache[capacity][idx]
	if ret != -1:
		return ret
	ret = pack(capacity, idx+1)
	if capacity >= volumes[idx]:
		ret = max(ret, pack(capacity-volumes[idx], idx+1) + values[idx])
	max_val_cache[capacity][idx] = ret
	return ret
		
rl = lambda: raw_input().strip()
cases = int(rl())
for case in xrange(cases):
	names = []
	volumes = []
	values = []
	max_val_cache = []
	nw_pair = rl().strip().split()
	len_things = int(nw_pair[0])
	capacity = int(nw_pair[1])
	for ci in xrange(capacity+1):
		max_val_cache.append([])
		for ti in xrange(len_things):
			max_val_cache[ci].append(-1)
	things = [rl() for _ in xrange(len_things)]
	for thing in things:
		splitted = thing.strip().split()
		names.append(splitted[0])
		volumes.append(int(splitted[1]))
		values.append(int(splitted[2]))

	# BAG PACKING
	bag = []
	for idx, thing in enumerate(things):
		if idx < len(things)-1 and pack(capacity, idx) != pack(capacity, idx+1):
			bag.append(names[idx])
			capacity -= volumes[idx]
	
	# PRINT RESULT
	val_res = [values[names.index(name)] for name in bag]
	print str(sum(val_res)) + ' ' + str(len(bag))
	for name in bag:
		print name
