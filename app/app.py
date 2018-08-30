from flask import Flask
from parser import load_data

app = Flask(__name__)

# Load data once
data = load_data()

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
