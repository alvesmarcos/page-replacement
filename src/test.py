#!/usr/bin/env python3
#--
# Author: Marcos Alves
#++
#
import page

def main():
	vec = []
	while True:
		try:
			value = int(input())
			vec.append(value)
		except EOFError:
			break
	# passando uma copia das listas para os algoritmos de páginação
	page.fifo(list(vec))
	page.otm(list(vec))
	page.lru(list(vec))

if __name__== "__main__":
	main()