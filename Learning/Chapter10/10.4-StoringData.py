import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj2:
    numbers2 = json.load(f_obj2)

print(numbers2)