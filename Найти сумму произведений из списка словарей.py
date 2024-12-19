import json

# TODO решите задачу
def task() -> float:
    filename = "input.json"
    with open(filename) as file:
        data = json.load(file)
        sum = 0
        for el in data:
           sum += el['score'] * el['weight']
    return round(sum, 3)


print(task())
