from flask_restful import fields

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