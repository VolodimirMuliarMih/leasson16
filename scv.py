#csv
import json
with open("lel_dict_json.json", "r") as my_file:
    b_tel = json.load(my_file)
import csv
tel_csv = "tel_csv"
cols = ["Tel", "name/age"]
with open(tel_csv, 'w', newline='') as f:
    wr = csv.writer(f)
    print(cols)
    for key, volue in b_tel.items():
        print(key,volue)

