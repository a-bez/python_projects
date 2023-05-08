from collections import Counter



dct = Counter({'la': 0.42857142857142855, 'vista': 0.2857142857142857, 'hasta': 0.14285714285714285, 'baby': 0.14285714285714285})
num = 0.17609125905568124
print(dct)
res=0
for i in dct:
    res = dct[i] * num

