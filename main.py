from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

transformer_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'allegiance': fields.String,
    'allegiance_name': fields.String,
    'subgroup': fields.String,
    'subgroup_name': fields.String,
    'role': fields.String,
    'image': fields.String,
    'description': fields.String
}

class TransformerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    allegiance = db.Column(db.Integer, nullable=False)
    allegiance_name = db.Column(db.String(100), nullable=False)
    subgroup = db.Column(db.String(100))
    subgroup_name = db.Column(db.String(100))
    role = db.Column(db.String(100))
    first_appearance = db.Column(db.String(100))
    image = db.Column(db.String(200))
    description = db.Column(db.String(500))

class Transformer(Resource):
    @marshal_with(transformer_resource_fields)
    def get(self, transformer_id):
        result = TransformerModel.query.filter_by(id=transformer_id).first()
        if not result:
            abort(404, message="No Transfomer found with that ID")
        return result

api.add_resource(Transformer, "/transformers/<int:transformer_id>")

if __name__ == "__main__":
    app.run(debug=True)