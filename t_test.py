# Ejemplo

import collections


def frec (lista):
  d = collections.defaultdict(int)
  
  for i in lista:
    d[i] += 1
    
  return d

def bigramas (lista):
  b = []
  for n in range(len(lista)-1):
    bigrama = (lista[n], lista[n+1])
    b.append(bigrama)
  return b




def student (lista, n):
  '''
  P (w1) = frecuencia w1 / total palabras
  P (w2) = frecuencia w2 / total palabras
  P (w1,w2) = P(w1)*P(w2) == En la formula de t-test = u
  t = x-u / squareroot (S² / N)
  '''
  t = {}
  
  tokens = lista 
  bigram = bigramas (lista) 
  frec_tokens = frec (tokens)
  frec_bigramas = frec (bigram)
  n = len(tokens)
  
  
  
  for bg in frec_bigramas:
    w1 = frec_tokens[bg[0]] / n
    w2 = frec_tokens[bg[1]] / n
    p = w1 * w2
   
    ##
    p_bigrama = frec_bigramas[bg] / n
    
    t_value = (p_bigrama - p) / (p_bigrama/n)**0.5
    t[bg] = t_value
  
  t_ordered = sorted(t.items(),key=lambda x:x[1],reverse=True)
  return t_ordered[:n]
  
  
    

tokens = ['she', 'knocked', 'on', 'his', 'door', 'she', 'knocked', 'at', 
'the', 'door','100', 'women', 'knocked', 'on', "Donaldson's", 'door', 'a', 
'man', 'knocked', 'on', 'the', 'metal', 'front', 'door']

print(student(tokens,10))
