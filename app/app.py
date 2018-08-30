from flask import Flask
from parser import load_data, render_template

app = Flask(__name__)

# Load data once
data = load_data()

@app.route('/sort')
def render_alphabetical():
	sortedData = data
	sortedData.sort(key=lambda _: _['name'])
	return render_template('postcodes.html', data=sortedData)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
