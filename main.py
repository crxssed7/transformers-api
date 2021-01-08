from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

transformers_put_args = reqparse.RequestParser()
transformers_put_args.add_argument("name", type=str, help="Name of the Transformer", required=True)
transformers_put_args.add_argument("allegiance", type=int, help="Transformers allegiance", required=True)
transformers_put_args.add_argument("subgroup", type=int, help="Transformers subgroup", required=False)
transformers_put_args.add_argument("role", type=str, help="Transformers role", required=False)
transformers_put_args.add_argument("first_appearance", type=str, help="The first appearance of the character", required=False)
transformers_put_args.add_argument("image", type=str, help="Transformers image", required=False)
transformers_put_args.add_argument("description", type=str, help="Transformers description", required=False)

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
    allegiance_name = db.Column(db.String(100))
    subgroup = db.Column(db.String(100))
    subgroup_name = db.Column(db.String(100))
    role = db.Column(db.String(100))
    first_appearance = db.Column(db.String(100))
    image = db.Column(db.String(200))
    description = db.Column(db.String(500))

class AllegianceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    alignment = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(200))

db.create_all()

class Transformer(Resource):
    @marshal_with(transformer_resource_fields)
    def get(self, transformer_id):
        result = TransformerModel.query.filter_by(id=transformer_id).first()
        if not result:
            abort(404, message="No Transfomer found with that ID")
        return result

    @marshal_with(transformer_resource_fields)
    def put(self, transformer_id):
        args = transformers_put_args.parse_args()
        result = TransformerModel.query.filter_by(id=transformer_id).first()
        if result:
            abort(409, message="Transformer with that ID already exists")
        allegiance_result = AllegianceModel.query.filter_by(id=args['allegiance']).first()
        if not allegiance_result:
            abort(404, message="No allegiance found with given ID")
        transformer = TransformerModel(id=transformer_id, name=args['name'], allegiance=args['allegiance'], subgroup=args['subgroup'], role=args['role'], image=args['image'], description=args['description'], first_appearance=args['first_appearance'], allegiance_name=allegiance_result.name, subgroup_name="teey")
        db.session.add(transformer)
        db.session.commit()
        return transformer, 201

class Allegiance(Resource):
    

api.add_resource(Transformer, "/transformers/<int:transformer_id>")

if __name__ == "__main__":
    app.run(debug=True)