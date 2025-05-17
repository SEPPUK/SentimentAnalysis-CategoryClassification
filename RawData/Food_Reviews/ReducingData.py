import csv
import json
import random

csv_file = './RawData/Food_Reviews/Food_Reviews.csv'
json_file = './LightData/Food_Reviews/Light_Food_Reviews.json'

data = []
with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        json_obj = {
            "user_id": int(row['user_id']),
            "recipe_id": int(row['recipe_id']),
            "date": row['date'],
            "rating": int(row['rating']),
            "review": row['review']
        }
        data.append(json_obj)

reduced_data = random.sample(data, 15000)

with open(json_file, 'w', encoding='utf-8') as jsonfile:
    for item in reduced_data:
        json.dump(item, jsonfile, ensure_ascii=False)
        jsonfile.write('\n')