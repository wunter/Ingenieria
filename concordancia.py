def concordancia (texto, palabra, izquierda, derecha, eprint = False, n = 20):
	
	''' 

	texto : (iterable)texto tokenizado en palabras 
	palabra : (string) palabra o expresion regular, ej. abogad[oa]
	izquierda y derecha: (int) cantidad de palabras que tomamos de contexto
	eprint: True (imprime en pantalla los contextos encontrados), False 
	n : (int) numero de contextos a mostrar 

	'''


	texto.insert (0, "*START*")
	texto.append ("*END*")

	todos_contextos = []

	for i in range(len(texto)):
	
		if re.match(palabra, texto[i]):

			if i < izquierda: # hay menos contexto izquierdo que palabras
				context_i = texto[:i]

			else:
				context_i = texto[i-izquierda:i]


			if len(texto) < (i+derecha):
				context_d = texto[i:]

			else: context_d = texto[i:(i+derecha+1)]

			context = tuple(context_i + context_d)
			todos_contextos.append(context)
	
	if eprint:

		print("\nMostrando {0} de {1} contextos".format(n,len(contextos)))
		if len(todos_contextos)< n:
			for w in todos_contextos:
				print(w)
		else:
			for w in todos_contextos[:n+1]:
				print(w)

	
	return tuple(todos_contextos)
