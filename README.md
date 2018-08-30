## Project Overview

Python Flask app, which connects to two APIs [postcodesio](https://postcodes.op) and [mapbox](https://www.mapbox.com/help/how-static-maps-work/) retrieves a list of postcodes,
queries them, sorts.

## Dependencies and Installation

#### Overview of architecture

The project is wrapped in a Docker container running alpine Linux.

#### Requirements

- Docker
- docker-compose

#### Installation and access

`git clone https://github.com/robalaban/postcode-store-search.git && cd postcode-store-search`

`docker-compose up --build`

`localhost:5000`

## TODO

- Order postcodes / stores by nearest outcode
- Write some test cases
