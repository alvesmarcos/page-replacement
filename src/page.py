#!/usr/bin/env python3
#--
# Author: Marcos Alves
#++
#

# First In, First Out
def fifo(queue):
	# index circulate
	index = 0
	# get numbers frames
	frames = [-1 for x in range(queue[0])]
	queue.pop(0)
	# swap pages
	count = 0
	# iterable in queue
	for q in queue:
		# check if the page is out
		if not q in frames:
			frames[index] = q 
			count += 1
			index += 1
			index %= len(frames)
	print("FIFO", count)

# Least Recently Used 
def lru(queue):
	# mark last page
	last_page = 0
	# index circulate
	index = 0
	# get numbers frames
	frames = [-1 for x in range(queue[0])]
	queue.pop(0)
	# dictionary
	table = {}
	# swap pages
	count = 0
	# iterable in queue
	for q in queue:
		# check if the page is table
		if not q in table:
			table[q] = 1
		else:
			table[q] += 1 

		# check if the page is out
		if not q in frames:
			if len(frames) != index:
				frames[index] = q 
				index += 1
			else:
				key, less = frames[0], table[frames[0]]
				for i in range(len(frames)):
					if less > table[frames[i]] and frames[i] != last_page:
						key, less = frames[i], table[frames[i]]
				frames[frames.index(key)] = q
			count += 1
			last_page = q
	print("LRU", count)

# Great Algorithm
def otm():
	pass

# tests 
l = [4,1,2,3,4,1,2,5,1,2,3,4,5] 
l1 = [3,7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]

fifo(list(l))
lru(list(l))
fifo(list(l1))
lru(list(l1))