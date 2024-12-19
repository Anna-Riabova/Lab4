import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

    # Конвертация в JSON
    json_data = json.dumps(data, indent=4)

    # Запись JSON в файл
    with open(OUTPUT_FILENAME, 'w') as file:
        file.write(json_data)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
           print(line, end="")
