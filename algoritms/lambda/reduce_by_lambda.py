lst = [1, 2, 3, 4]

reduced_by_lambda = list(map(lambda x : x**x, lst))     # exponentiation to the same num

print(reduced_by_lambda)    # [1, 4, 27, 256]