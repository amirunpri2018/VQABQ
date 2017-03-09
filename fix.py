import json

original_dataset = './data/OpenEnded_mscoco_test-dev2015_questions.json'

def get(file):
	with open(file, 'r') as f:
		data = json.load(f)
	return data

def fix(file):
	data = get(file)
	dataset = get(original_dataset)
	dataset = dataset['questions']
	dataset = [d['question_id'] for d in dataset]
	#remove all non dictionary
	data = [d for d in data if type(d) is dict]
	#get all ids
	ids = [d['question_id'] for d in data]
	#remove what is extra
	data = [d for d in data if d['question_id'] in dataset]
	#add what is missing
	for d in dataset:
		if d not in ids:
			data.append({'question_id':d, 'answer':'NOTGIVENTON'})
	with open(file+'e', 'w') as f:
		json.dump(data, f)

def check(data):
	for d in data:
		if type(d) is not dict:
			print(d)
		elif len(d.keys())!=2:
			print(d)

#fix('data/dev_test2015_answers_0.json')
#fix('data/dev_test2015_answers_1.json')
#fix('data/dev_test2015_answers_2.json')

