# Transformers API
A database of Transformers characters

![Transformers](logo.png)

# Endpoints
`baseURL` - LOCALHOST

# Transformers

## **GET** */transformers/{`id`}* <br>
*Get the Transformer that has the specified ID* <br>
`id` - Required, ID of the Transformer *{INTEGER}*

## **GET** */transformers/filter={`filter_by`}&pageSize={`page_size`}* <br>
*Filter for a Transformer* <br>
`filter_by` - Required, the value to filter by, could be `name`, `function`, `allegiance` etc *{STRING}* <br>
`page_size` - Optional, the maximum amount of results the request should return. Default is 10 *{INTEGER}*

## **GET** */transformers/search/{`query`}* <br>
*Search for a Transformer based off of the given query* <br>
`query` - Required, the name of the Transformer to search for *{STRING}*

# Models

## Transformer

```json
{
	'id' : integer,
	'name' : string,
	'allegiance' : integer,
	'allegiance_name' : string,
	'subgroup' : integer,
	'subgroup_name' : string,
	'role' : string,
	'first_appearance' : string,
	'image' : string,
	'description' : string
}
```

