# Transformers API
A database of Transformers characters

![Transformers](https://assets.stickpng.com/images/5cb4886a5f1b6d3fbadece80.png)

# Endpoints
`baseURL` - LOCALHOST

# Transformers

## **GET** */transformers/{id}* <br>
*Get the Transformer that has the specified ID* <br>
`id` - Required, ID of the Transformer *{INTEGER}*

## **GET** */transformers/filter={filter_by}&pageSize={page_size}* <br>
*Filter for a Transformer* <br>
`filter_by` - Required, the value to filter by, could be `name`, `function`, `alignment` etc *{STRING}* <br>
`page_size` - Optional, the maximum amount of results the request should return. Default is 10 *{INTEGER}*

## **GET** */transformers/search/{query}* <br>
*Search for a Transformer based off of the given query* <br>
`query` - Required, the name of the Transformer to search for *{STRING}*
