from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy, Pagination
import model_args
import resource_fields

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
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
    description = db.Column(db.String(500))

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

class Transformer(Resource):
    @marshal_with(resource_fields.transformer_resource_fields)
    def get(self, transformer_id):
        result = TransformerModel.query.filter_by(id=transformer_id).first()
        if not result:
            abort(404, message="No Transfomer found with that ID")
        return result

    @marshal_with(resource_fields.transformer_resource_fields)
    def put(self, transformer_id):
        args = model_args.transformers_put_args.parse_args()
        # Check if the Transfomer with that ID already exists
        result = TransformerModel.query.filter_by(id=transformer_id).first()
        if result:
            abort(409, message="Transformer with that ID already exists")
        # Get the allegiance from the allegiance_id, throw an error if not found
        allegiance_result = AllegianceModel.query.filter_by(id=args['allegiance']).first()
        if not allegiance_result:
            abort(404, message="No allegiance found with given ID")
        # Get the subgroup from the subgroup_id
        subgroup_result = SubgroupModel.query.filter_by(id=args['subgroup']).first()
        if not subgroup_result:
            abort(404, message="No subgroup found with the given ID")
        # Create a new Transformer instance
        transformer = TransformerModel(id=transformer_id, name=args['name'], allegiance=args['allegiance'], subgroup=args['subgroup'], role=args['role'], image=args['image'], description=args['description'], first_appearance=args['first_appearance'], allegiance_name=allegiance_result.name, subgroup_name=subgroup_result.name)
        db.session.add(transformer)
        db.session.commit()
        return transformer, 201

    @marshal_with(resource_fields.transformer_resource_fields)
    def patch(self, transformer_id):
        args = model_args.transformer_patch_args.parse_args()
        # Check if the Transformer exists
        result = TransformerModel.query.filter_by(id=transformer_id).first()
        if not result:
            abort(404, message="No Transformer found with that ID")
        # Set the values if specified
        if args['role']:
            result.role = args['role']
        if args['first_appearance']:
            result.first_appearance = args['first_appearance']
        if args['image']:
            result.image = args['image']
        if args['description']:
            result.description = args['description']
        db.session.commit()
        return result

    def delete(self, transformer_id):
        result = TransformerModel.query.filter_by(id=transformer_id).first()
        if not result:
            abort(404, message="No Transfomer found with that ID")
        db.session.delete(result)
        db.session.commit()
        return '', 204

class Allegiance(Resource):
    @marshal_with(resource_fields.allegiance_resource_fields)
    def get(self, allegiance_id):
        result = AllegianceModel.query.filter_by(id=allegiance_id).first()
        if not result:
            abort(404, message="No allegiance was found with that ID")
        return result

    @marshal_with(resource_fields.allegiance_resource_fields)
    def put(self, allegiance_id):
        args = model_args.allegiance_put_args.parse_args()
        # Check that the ID doesn't exist
        checkForID = AllegianceModel.query.filter_by(id=allegiance_id).first()
        if checkForID:
            abort(409, message="Allegiance ID already exists")
        # Check if the allegiance already exists
        checkForAllegiance = AllegianceModel.query.filter_by(name=args['name']).first()
        if checkForAllegiance:
            abort(409, message="Allegiance already exists with that name")
        # Create new allegiance instance
        allegiance = AllegianceModel(id=allegiance_id, name=args['name'], alignment=args['alignment'], image=args['image'])
        db.session.add(allegiance)
        db.session.commit()
        return allegiance, 201

    def delete(self, allegiance_id):
        result = AllegianceModel.query.filter_by(id=allegiance_id).first()
        if not result:
            abort(404, message="No Allegiance found with that ID")
        db.session.delete(result)
        db.session.commit()
        return '', 204

class Subgroup(Resource):
    @marshal_with(resource_fields.subgroup_resource_fields)
    def get(self, subgroup_id):
        result = SubgroupModel.query.filter_by(id=subgroup_id).first()
        if not result:
            abort(404, message="No subgroup found with that ID")
        return result

    @marshal_with(resource_fields.subgroup_resource_fields)
    def put(self, subgroup_id):
        args = model_args.subgroup_put_args.parse_args()
        # Check that ID doesn't exists
        checkForID = SubgroupModel.query.filter_by(id=subgroup_id).first()
        if checkForID:
            abort(409, message="Subgroup ID already exists")
        # Check if the subgroup already exists
        checkForSubgroup = SubgroupModel.query.filter_by(name=args['name']).first()
        if checkForSubgroup:
            abort(409, message="Subgroup already exists")
        # Create new subgroup instance
        subgroup = SubgroupModel(id=subgroup_id, name=args['name'], alignment=args['alignment'], image=args['image'])
        db.session.add(subgroup)
        db.session.commit()
        return subgroup, 201

    def delete(self, subgroup_id):
        result = SubgroupModel.query.filter_by(id=subgroup_id).first()
        if not result:
            abort(404, message="No Subgroup found with that ID")
        db.session.delete(result)
        db.session.commit()
        return '', 204

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