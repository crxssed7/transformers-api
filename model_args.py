from flask_restful import reqparse

transformers_put_args = reqparse.RequestParser()
transformers_put_args.add_argument("name", type=str, help="Name of the Transformer", required=True)
transformers_put_args.add_argument("allegiance", type=int, help="Transformers allegiance", required=True)
transformers_put_args.add_argument("subgroup", type=int, help="Transformers subgroup", required=True)
transformers_put_args.add_argument("role", type=str, help="Transformers role", required=False)
transformers_put_args.add_argument("first_appearance", type=str, help="The first appearance of the character", required=False)
transformers_put_args.add_argument("image", type=str, help="Transformers image", required=False)
transformers_put_args.add_argument("description", type=str, help="Transformers description", required=False)

allegiance_put_args = reqparse.RequestParser()
allegiance_put_args.add_argument("name", type=str, help="Name of the allegiance, eg, Autobot", required=True)
allegiance_put_args.add_argument("alignment", type=str, help="The alignment, eg, Bad", required=True)
allegiance_put_args.add_argument("image", type=str, help="Logo for the Allegiance", required=False)

subgroup_put_args = reqparse.RequestParser()
subgroup_put_args.add_argument("name", type=str, help="Name of the allegiance, eg, Autobot", required=True)
subgroup_put_args.add_argument("alignment", type=str, help="The alignment, eg, Bad", required=True)
subgroup_put_args.add_argument("image", type=str, help="Logo for the Allegiance", required=False)

transformer_filter_args = reqparse.RequestParser()
transformer_filter_args.add_argument("query", type=str, help="String to search for", required=True)
transformer_filter_args.add_argument("filter", type=str, help="What to filter by", required=True)
transformer_filter_args.add_argument("page", type=int, help="The page of results to return", required=False)

transformer_patch_args = reqparse.RequestParser()
transformer_patch_args.add_argument("role", type=str, help="Transformers role", required=False)
transformer_patch_args.add_argument("first_appearance", type=str, help="The first appearance of the character", required=False)
transformer_patch_args.add_argument("image", type=str, help="Transformers image", required=False)
transformer_patch_args.add_argument("description", type=str, help="Transformers description", required=False)