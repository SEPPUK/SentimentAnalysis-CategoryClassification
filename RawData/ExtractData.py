import json
import random

random.seed(0)

datasets = ['Books',
			'Clothing_Shoes_Jewelry',
			'Electronics',
			'Home_Kitchen',
			'Movies_TV',
			'Video_Games']

for dataset in datasets:
	dataset_name = f'./RawData/{dataset}.json'
	light_dataset = f'./LightData/Light_{dataset}.json'

	data = []
	with open(dataset_name) as f:
		for line in f:
			review = json.loads(line)
			data.append(review)

	reduced_data = random.sample(data, 15000)

	with open(light_dataset, 'w') as f:
		for review in reduced_data:
			f.write(json.dumps(review)+'\n')