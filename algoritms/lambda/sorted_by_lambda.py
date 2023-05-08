grades = [{'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Aaron', 'final': 98}]

sorted_by_name = sorted(grades, key=lambda x : x['name'])                   # sorted by 'name'
sorted_by_score = sorted(grades, key=lambda x : x['final'], reverse=True)    # sorted by 'final' score min->max

print(sorted_by_name)
print(sorted_by_score)