# Transformers API
A database of Transformers characters

![Transformers](logo.png)

# Endpoints
`baseURL` - LOCALHOST

# Transformers

## **GET** */transformers/{`id`}* <br>
*Get the Transformer that has the specified ID* <br>
`id` - Required, ID of the Transformer *{INTEGER}*

## **GET** */transformers?filter=`filter_by`&query=`query`&page=`page`* <br>
*Filter for a Transformer* <br>
`filter_by` - Required, the value to filter by, could be `name`, `allegiance`, or `subgroup` etc *{STRING}* <br>
`query` - Required, the term to filter for *{STRING}* <br>
`page` - Optional, the page to return. Default is 1 *{INTEGER}*

# Models

## Transformer Model

```
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

## Allegiance Model
```
{
	'id' : integer,
	'name' : string,
	'alignment' : string,
	'image' : string
}
```
```
Allegiances: 
	None, 
	Autobot, 
	Decepticon, 
	Quintesson, 
	Unicron
```
## Subgroup Model
```
{
	'id' : integer,
	'name' : string,
	'alignment' : string,
	'image' : string
}
```
```
Subgroups:
	None,
	Aerialbot,
	Lithone,
	Protectobot,
	Combaticon,
	Insecticon,
	Stunticon,
	Constructicon,
	Predacon,
	Dinobot,
	Quintesson,
	Battlecharger,
	Junkion
```
