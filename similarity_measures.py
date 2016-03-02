import re, math
from collections import Counter

def cosine_similarity(sent1, sent2): # 
    """ 
    Calculates cosine between two words, sentences or documents
    """
    words = re.compile(r'\w+')
    def get_cosine(vec1, vec2): # los vectores son diccionarios de frecuencia
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        
        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
        
        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    def text_to_vector(text):
        palabras = words.findall(text)
        return Counter(palabras)
    
    vector1 = text_to_vector(sent1)
    vector2 = text_to_vector(sent2)
    cosine = get_cosine(vector1, vector2)
    return cosine
