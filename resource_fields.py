from flask_restful import fields

transformer_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'allegiance': fields.Integer,
    'allegiance_name': fields.String,
    'subgroup': fields.Integer,
    'subgroup_name': fields.String,
    'first_appearance': fields.String,
    'role': fields.String,
    'image': fields.String,
    'description': fields.String
}

allegiance_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'alignment': fields.String,
    'image': fields.String
}

subgroup_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'alignment': fields.String,
    'image': fields.String
}

tf_filter_resource_fields = {
    'num_pages': fields.Integer,
    'total_count':fields.Integer,
    'results': fields.List(fields.Nested(transformer_resource_fields))
}