# c2j - it`s a .csv-.json transformer python-package
## How to install
pip install c2j
## Guide

```python
from c2j.transform import csv_json, json_csv

# You can transform .csv-file into .json-file
csv_json(csv_path)  # csv_path – path to .csv-file

# You can transform .json-file into .csv-file
json_csv(json_path)  # json_path – path to .json-file
```
## Example of usage

```python
from c2j.transform import csv_json, json_csv

csv_json('my_csv.csv') # transform .csv to .json
json_csv('my_json.json')  # transform .json to .csv
```