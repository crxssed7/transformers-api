from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy, Pagination
import model_args
import resource_fields

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)

class TransformerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    allegiance = db.Column(db.Integer, nullable=False)
    allegiance_name = db.Column(db.String(100))
    subgroup = db.Column(db.Integer, nullable=False)
    subgroup_name = db.Column(db.String(100))
    role = db.Column(db.String(100))
    first_appearance = db.Column(db.String(100))
    image = db.Column(db.String(200))
    description = db.Column(db.String(1500))

class AllegianceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    alignment = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(200))

class SubgroupModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    alignment = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(200))

db.create_all()

class Transformer(Resource):
    @marshal_with(resource_fields.transformer_resource_fields)
    def get(self, transformer_id):
        result = TransformerModel.query.filter_by(id=transformer_id).first()
        if not result:
            abort(404, message="No Transfomer found with that ID")
        return result

class Allegiance(Resource):
    @marshal_with(resource_fields.allegiance_resource_fields)
    def get(self, allegiance_id):
        result = AllegianceModel.query.filter_by(id=allegiance_id).first()
        if not result:
            abort(404, message="No allegiance was found with that ID")
        return result

class Subgroup(Resource):
    @marshal_with(resource_fields.subgroup_resource_fields)
    def get(self, subgroup_id):
        result = SubgroupModel.query.filter_by(id=subgroup_id).first()
        if not result:
            abort(404, message="No subgroup found with that ID")
        return result

class TransformerFilter(Resource):
    @marshal_with(resource_fields.tf_filter_resource_fields)
    def get(self):
        args = model_args.transformer_filter_args.parse_args()

        page = 1

        # Check if there is a page specified
        if args['page']:
            page = args['page']

        if args['filter'].lower() == "allegiance":
            # Filter by allegiance
            
            result = TransformerModel.query.filter(TransformerModel.allegiance_name.like('%' + args['query'] + '%')).paginate(page=page, per_page=10, error_out=True)
            if not result.items:
                abort(404, message="No results found")
            
            results = {
                'num_pages': result.pages,
                'total_count': result.total,
                'results': result.items
            }

            return results
        elif args['filter'].lower() == "subgroup":
            # Filter by subgroup

            result = TransformerModel.query.filter(TransformerModel.subgroup_name.like('%' + args['query'] + '%')).paginate(page=page, per_page=10, error_out=True)
            if not result.items:
                abort(404, message="No results found")
            
            results = {
                'num_pages': result.pages,
                'total_count': result.total,
                'results': result.items
            }

            return results
        elif args['filter'].lower() == "name":
            # Search by name

            result = TransformerModel.query.filter(TransformerModel.name.like('%' + args['query'] + '%')).paginate(page=page, per_page=10, error_out=True)
            if not result.items:
                abort(404, message="No results found")
            
            results = {
                'num_pages': result.pages,
                'total_count': result.total,
                'results': result.items
            }

            return results
        else:
            abort(400, message="Connot use the filter: " + args['filter'])

api.add_resource(Transformer, "/transformers/<int:transformer_id>")
api.add_resource(TransformerFilter, "/transformers")
api.add_resource(Allegiance, "/allegiance/<int:allegiance_id>")
api.add_resource(Subgroup, "/subgroup/<int:subgroup_id>")

if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.15')