import os
import json
import csv
import pandas


def csv_json(csv_path: str):
    """
    Transforms .csv to .json\n
    :param csv_path: path to .csv-file
    """
    directory = os.path.split(csv_path)
    os.chdir(directory[0])
    data = []
    with open(csv_path) as csvFile:
        reader = csv.DictReader(csvFile, delimiter=";")
        title = reader.fieldnames
        for line in reader:
            data.extend([{title[i]: line[title[i]] for i in range(len(title))}])

    with open('yourjsonfile.json', 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


def json_csv(json_path: str):
    """
    Transform .json to .csv\n
    :param json_path: path to .json-file
    """
    directory = os.path.split(json_path)
    os.chdir(directory[0])
    with open(json_path) as jsonFile:
        data = json.loads(jsonFile.read())

    df = pandas.json_normalize(data)

    with open('yourcsvfile.csv', 'w', newline='') as csvFile:
        for element in data:
            s = list(element.keys())
        writer = csv.DictWriter(csvFile, fieldnames=s)
        writer.writeheader()
        writer.writerows(data)
