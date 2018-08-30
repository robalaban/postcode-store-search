import requests

API_KEY = "pk.eyJ1IjoibWF0dG1hZ2xlbm5vbiIsImEiOiJjamxnaGExZjExNDVyM2txdTkyOW5yb21tIn0.y05jrjDfy4WvweGw6VD6kQ"
URL = "https://api.mapbox.com/styles/v1/mapbox/streets-v10/static/url-https%3A%2F%2Fwww.mapbox.com%2Fimg%2Frocket.png({LONG},{LAT})/{LONG},{LAT},15/200x200?access_token={API_KEY}"

def get_static_image(data):
    if 'longitude' and 'latitude' in data:
        query = {
            "LONG": data['longitude'],
            "LAT": data['latitude'],
            "API_KEY": API_KEY
        }

        return URL.format(**query)