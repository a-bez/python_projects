person = [
    {'name' : 'Alex', 'age' : 21, 'status' : 'student'},
    {'name' : 'Vycheslav', 'age' : 58, 'status' : 'working'},
    {'name' : 'Mykolyi', 'age' : 63, 'status' : 'general'},
    {'name' : 'Anna', 'age' : 75, 'status' : 'pension'},
]

filtred_by_lambda = list(filter(lambda x : x['age'] <= 60, person))     # use filter() method with lambda function

print(filtred_by_lambda)        # [
                                #   {'name': 'Alex', 'age': 21, 'status': 'student'},
                                #   {'name': 'Vycheslav', 'age': 58, 'status': 'working'
                                # ]