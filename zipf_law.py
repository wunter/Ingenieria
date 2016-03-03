
import re
import matplotlib
from matplotlib import pyplot
import pylab

def zipf_law (texto, scale = False):

	'''
	Calcular la ley de Zipf.
	
	r * Prob(r) = A
	
	r -> rank
	Prob(r) -> the probability of a word at rank r. Prob(r) = freq(r) / N
	N -> numero total de palabras en el texto (NO palabras únicas)
	A -> constante. Para calcular A = (r * freq(r))/N 
	scale = cambiar a False para desactivar / 'log' escala logaritmica
	'''
	# Distribución de frecuencia
	dist_frec = {}
	for w in texto:
		if w not in dist_frec:
			dist_frec[w] = 1
		else:
			dist_frec[w]+= 1
	
	
	# Distribución de Zipf del texto dado
	frecuencia = [i for i in dist_frec.values()]
	
	frecuencia.sort(reverse = True)
	
	datos_zipf = [(rank, frec) for rank,frec in enumerate(frecuencia)]
	
	
	# Distribución de Zipf ideal
	a_values = [(rank*(frec/len(texto))) for rank, frec in datos_zipf]

	constant_a = sum(a_values)/len(a_values)

	zipf_ideal = [(n,(constant_a*len(texto))/n) for n in range(1,len(texto))]

	
	# Plotear los datos obtenidos en una gráfica
	
	rank, frec = zip(*datos_zipf)
	r_ideal, f_ideal = zip(*zipf_ideal)
	
	
	pyplot.plot(rank, frec, 'r-', label = "Distribución del texto")

	pyplot.plot(r_ideal, f_ideal, "b-", label = "Distribución Ideal")
	
	if scale:
		pyplot.xscale(scale)
		pyplot.yscale(scale)
		
	pyplot.title('Zipf plot')
	pyplot.xlabel('Rank')
	pyplot.ylabel('Frequency')
	pylab.legend(loc='upper right')
	
	return pyplot.show()

