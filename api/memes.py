import json
from flask import Blueprint, request, jsonify
import requests
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime



memes_api = Blueprint('memes_api', __name__,
                   url_prefix='/api/memes')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(memes_api)

class MemesAPI:     
    class TopText(Resource):  # User API operation for Create, Read.  THe Update, Delete methods need to be implemeented
        def get(self, top_text): # Create method
            url = f"https://imaad08.github.io/tri-2-csp/2024/01/16/Temp_Frontend_IPYNB_2_.html"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return jsonify(data)
    class BottomText(Resource):
        def get(self, bottom_text):
            bottomText = bottom_text
        
    
    api.add_resource(TopText, '/get_text/<top_text>')
    api.add_resource(BottomText, '/get_text/<bottom_text>')