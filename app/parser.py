import json

STORE_FILE = 'stores.json'

def load_data():
	with open(STORE_FILE) as f:
		data = json.load(f)

	return data