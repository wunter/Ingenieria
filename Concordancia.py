def concordancia (texto, palabra, izquierda, derecha, n, regex = False):

	''' 

	texto : lista de palabras, 
	palabra : (string) palabra o expresion regular, ej. abogad[oa]
	izquierda y derecha: (int) cantidad de palabras que tomamos
	n : (int) numero de contextos a mostrar 

	'''


	texto.insert (0, "*START*")
	texto.append ("*END*")

	contextos = []

	for i in range(len(texto)):
	

		if re.match(palabra, texto[i]):

			if i < izquierda: # hay menos contexto izquierdo que palabras
				context_i = texto[:i]

			else:
				context_i = texto[i-izquierda:i]


			if len(texto) < (i+derecha):
				context_d = texto[i:]

			else: context_d = texto[i:(i+derecha+1)]

			context = tuple(context_i + context_d)
			contextos.append(context)

	print("Mostrando {0} de {1} contextos\n".format(n,len(contextos)))
	if len(contextos)< n:
		for w in contextos:

			print(w)
	else:
		for w in contextos[:n+1]:
			
			print(w)

	
	return tuple(contextos)
