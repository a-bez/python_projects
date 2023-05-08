import math
r = 0
def compute_idf(word, corpus):
    r = math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))
    return r
texts = [
    ['pasta','la','vista','baby','la','vista'],
    ['hasta','siempre','comandante','baby','la','siempre'],
    ['siempre','comandante','baby','la','siempre']
]

print(compute_idf('comandante', texts))