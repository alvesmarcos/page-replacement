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
	frames = [-1] * queue[0]
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
def lru():
	pass

# Great Algorithm
def otm():
	pass