

import os

# Función para crear una carpeta
def create_dir (path):

	if not os.path.exists(path): # Si solo indica el nombre, creará el archivo en el os.getcwd()

		print("Creating the directory {}".format(name))

		os.makedirs(path)

# Función para leer un archivo
def read_file (file):
	f = open(filename, 'r', encoding = "utf-8")
	f = f.read()
	f.close
	return f

# Función para leer todos los archivos de una carpeta con una extensión determinada
def read_dir (path, extension = False): # path from directory, and file extension eg ('.png', '.jpg', '.jpeg')
	
	output = []

	list_dir = os.listdir(path)

	if extension:
		list_dir = [f for f in list_dir if f.lower().endswith(extension)]

	for filename in list_dir:
		f = read_file(filename)
		output.append(f)

	return output
