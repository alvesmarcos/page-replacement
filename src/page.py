#!/usr/bin/env python3
#--
# Author: Marcos Alves
#++
#

# First In, First Out
def fifo(vector):
	# indice circular do quadro
	index = 0
	# inicializando o quadro com valores default (-1)
	frames = [-1 for x in range(vector[0])]
	# retiro do vetor o número de quadros
	vector.pop(0)
	# contador para troca de pagina
	count = 0
	
	for v in vector:
		# checando se a página está fora do quadro
		if not v in frames:
			# troca
			frames[index] = v 
			count += 1
			index += 1
			index %= len(frames)
	print("FIFO", count)

# Least Recently Used 
def lru(vector):
	# indice do quadro
	size_max = vector.pop(0)
	frames = []

	# retiro do vetor o número de quadros
	count = 0
	for v in vector:
		# checando se a página está fora do quadro
		if not v in frames:
			# caso tenha espaço no quadro
			if len(frames) != size_max:
				# troca
				frames.insert(0, v) 
			else:
				frames.pop()
				frames.insert(0, v)
			count += 1
		else:
			key = frames.index(v)
			frames.pop(key)
			frames.insert(0, v)
	print("LRU", count)

# Great Algorithm	
def otm(vector):
	# índice apontador para próxima posição do atual elemento do vector
	index_vector = 0
	# indice do quadro
	index = 0
	# inicializando o quadro com valores default (-1)
	frames = [-1 for x in range(vector[0])]
	# retiro do vetor o número de quadros
	vector.pop(0)
	# contador para troca de pagina
	count = 0

	for v in vector:
		# incremento índice do vector para próxima posição
		index_vector += 1
		# checando se a página está fora do quadro
		if not v in frames:
			# caso tenha espaço no quadro
			if len(frames) != index:
				# troca
				frames[index] = v 
				index += 1
			else:
				key = 0
				larger = 0
				gap = 0
				# teste cada página do quadro com o que resta da entrada
				for p in frames:
					# procurando do indice apontador até o final do vector
					for j in range(index_vector, len(vector)):
						if vector[j] == p: break
						gap += 1
					# checando se o gap é maior que o atual
					if gap > larger:
						larger = gap
						# salvando a pagina referente ao gap
						key = p
					gap = 0
				# troca
				frames[frames.index(key)] = v
			count += 1
	print("OTM", count)