import csv

def load(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def save(filename, data, fieldnames):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
