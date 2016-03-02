
# Código para depurar el archivo del crea, disponible en http://corpus.rae.es/creanet.html

crea = open('crea.txt', 'r').read() 

crea_def = []

lineas = crea.split('\n')
for i in lineas:
	crea_def.append(i.split('\t'))

diccionario_crea = {}

for j in crea_def:
	try:
		diccionario_crea[j[1]] = [j[2].strip(), j[3].strip()]
	except IndexError:
		pass


for entrada in diccionario_crea:
	n1 = int(re.sub(',','',diccionario_crea[entrada][0]))
	n2 = float(diccionario_crea[entrada][1])
	diccionario_crea[entrada] = [n1,n2]

# Si necesitas el diccionario ordenado
# scores_sorted = sorted(scores.items(), key=lambda item: item[1][0], reverse=True)
