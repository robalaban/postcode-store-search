import requests
from flask import Flask, render_template, request
from parser import load_data
from helpers import get_static_image

app = Flask(__name__)

# Load data once
data = load_data()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/sort')
def render_alphabetical():
	sortedData = data
	sortedData.sort(key=lambda _: _['name'])
	return render_template('postcodes.html', data=sortedData)


@app.route('/maps')
def extract_postcodes():
	postcodes = [_['postcode'] for _ in data]
	query = {"postcodes": postcodes}

	# Bulk request of postcode data
	r = requests.post('http://postcodes.io/postcodes', query)

	if r.status_code == 200:
		result = r.json()['result']
		# Append lat, long to data dict
		for idx in range(len(result)):
			if result[idx]['result']:
				data[idx].update(
					longitude=result[idx]['result']['longitude'],
					latitude=result[idx]['result']['latitude']
				)
			
			static_map = get_static_image(data[idx])
			data[idx].update(
				static_map=static_map
			)

	return render_template('maps.html', data=data)


@app.route('/search', methods=['POST'])
def search_nearest_postcode():
	# Get Postcode
	postcode = request.form['postcode']

	# Query for outcode
	r = requests.get('http://postcodes.io/postcodes/%s' % postcode)
	if r.status_code == 200:
		result = r.json()['result']
		outcode = result['outcode']
	
	# Use outcode for reverse search and filter out the postcodes
	# To be implemented ...

	return render_template('index.html', outcode=outcode)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
