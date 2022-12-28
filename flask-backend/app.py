from flask import Flask, render_template, make_response, Response
from flask_restx import Api, Resource, reqparse
from flask_cors import CORS
import os

import json
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


@api.route('/generateimage')
class ImageGenerate(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('prompt',
                       type=str,
                       required=True,
                       help="prompt message is required")
    parse.add_argument('size',
                       type=str,
                       required=True,
                       help="size message is required")

    def get(self):
        return {"name": "image API"}

    def post(self):
        data = ImageGenerate.parse.parse_args()
        size = ""
        if data['size'] == 'small':
            size = "256x256"
        elif data['size'] == 'medium':
            size = "512x512"
        else:
            size = "1024x1024"

        response = openai.Image.create(prompt=data['prompt'], size=size, n=1)

        return response.data[0]


if __name__ == '__main__':
    app.run(debug=True)
