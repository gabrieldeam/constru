from flask_restful import Resource
from models.example_model import ExampleModel
from flask import jsonify

class ExampleResource(Resource):
    def get(self):
        examples = ExampleModel.query.all()
        return jsonify([{'id': example.id, 'name': example.name} for example in examples])
