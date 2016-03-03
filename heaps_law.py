
import re
import matplotlib
from matplotlib import pyplot
import pylab


def heaps_law (texto, scale = False, k = 30, b = 0.5):

	'''
	Calcular la ley de Heaps. Formula --> V = k* (n**b)

	Donde V -> numero de palabras unicas, n -> total de palabras, 
	k -> variable con valor entre 10 y 100
	b -> variable con valor entre 0.4 y 0.6

	Los valores de k y b hay que optimizarlos para cada corpus o texto.

	scale = cambiar a False para desactivar / 'log' escala logaritmica


	'''
	# Distribución del texto dado

	unique_words = set()

	heaps_data = []

	for i, w in enumerate (texto):
		unique_words.add(w)
		heaps_data.append((i,len(unique_words)))

	# Distribución ideal de Heaps --> V = k * (n**b) 

	heaps_ideal= [(n, k*(n**b)) for n in range(1,len(texto))]
	

	# Plotting

	unique,total = zip(*heaps_data)

	u_ideal,t_ideal = zip(*heaps_ideal)

	if scale:
		pyplot.xscale(scale)
		pyplot.yscale(scale)

	pyplot.plot(unique, total, 'r-', label = "Distribución del texto")

	pyplot.plot(u_ideal, t_ideal, "b-", label = "Distribución Ideal")

	pylab.legend(loc='upper left')
	pyplot.title('Ley de Heaps')
	pyplot.xlabel('Numero de Palabras')
	pyplot.ylabel('Palabras Unicas')

	return pyplot.show()
