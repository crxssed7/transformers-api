from flask_restful import reqparse

transformers_put_args = reqparse.RequestParser()
transformers_put_args.add_argument("name", type=str, help="No `name` value was specified, Example: Optimus Prime", required=True)
transformers_put_args.add_argument("allegiance", type=int, help="No `allegiance` value was specified. Example: 2 (Autobot)", required=True)
transformers_put_args.add_argument("subgroup", type=int, help="No `subgroup` value was specified. Example: 1 (None)", required=True)
transformers_put_args.add_argument("role", type=str, help="No `role` value was specified. Example: Warrior", required=False)
transformers_put_args.add_argument("first_appearance", type=str, help="No `first_appearance` value was specified. Example: Transformers Prime - S01E01", required=False)
transformers_put_args.add_argument("image", type=str, help="No `image` value was specified", required=False)
transformers_put_args.add_argument("description", type=str, help="No `description` value was specified", required=False)

allegiance_put_args = reqparse.RequestParser()
allegiance_put_args.add_argument("name", type=str, help="No `name` value was specified. Example: Autobot", required=True)
allegiance_put_args.add_argument("alignment", type=str, help="No `alignment` value was specified. Example: Good", required=True)
allegiance_put_args.add_argument("image", type=str, help="No `image` value was specified", required=False)

subgroup_put_args = reqparse.RequestParser()
subgroup_put_args.add_argument("name", type=str, help="No `name` value was specified. Example: Predacon", required=True)
subgroup_put_args.add_argument("alignment", type=str, help="No `alignment` value was specified. Example: Bad", required=True)
subgroup_put_args.add_argument("image", type=str, help="No `image` value was specified", required=False)

transformer_filter_args = reqparse.RequestParser()
transformer_filter_args.add_argument("query", type=str, help="No `query` value was specified. Example: Bumblebee", required=True)
transformer_filter_args.add_argument("filter", type=str, help="No `filter` value was specified. Example: Allegiance", required=True)
transformer_filter_args.add_argument("page", type=int, help="No `page` value was specified. Example: 1", required=False)

transformer_patch_args = reqparse.RequestParser()
transformer_patch_args.add_argument("role", type=str, help="No `role` value was specified. Example: Warrior", required=False)
transformer_patch_args.add_argument("first_appearance", type=str, help="No `first_appearance` value was specified. Example: Transformers Prime - S01E01", required=False)
transformer_patch_args.add_argument("image", type=str, help="No `image` value was specified", required=False)
transformer_patch_args.add_argument("description", type=str, help="No `description` value was specified", required=False)