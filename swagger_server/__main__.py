#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder
from flask_cors import CORS


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    CORS(app.app)
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'This is a API document for Stylens Service'})
    app.run(port=8080)
