# Item Management Service

## Usage
All responses will have the form:

```json
{
    "message": "Description of what happened",
    "data": "Mixed type holding the content of the response"
}
```
Subsequent response definitions will only detail the expected value of the `data` field.

### List all items
**Definition**

`GET /item`

**Response**

- 200: success

```json 
[
    {
        "identifier": "id1",
        "name": "shoes",
        "brand": "Nike",
        "item_type": "sth-to-wear",
        "expire_date": "2020-11-11",
        "desire":"2",
        "sales": {
            "platform": "Youtube",
            "name": "Suggy",
            "link":"https://www.nike.com/cn/"
        }
    },
    {
        "identifier": "id2",
        "name": "Camera A7C",
        "brand": "Sony",
        "item_type": "electronic",
        "expire_date": "never", 
        "desire":"5",
        "sales": {
            "platform": "taobao",
            "name": "system recomendation",
            "link":""
        }
    }
]
```

### Add a new wish item
**Definition**

`POST /item`

**Arguments**

- `"identifier":string` a globally unique identifier for this wish item
- `"name":string` a friendly name for the wish item
- `"item_type":string` the type of the device as understood by the client
- `"expire_date":string` the item will be deleted automatically at expire date (a email notice?)
- `"desire":string` star your desire of this item (1 to 5)
- `"sales_platform":string` the place the item is recommended
- `"sales_name":string` the person who made this item recomendation

If the identifier already exists, the existing device will be overwritten.

**Response**

- 201: created successfully

Returns the new item if successful.

```json
{
        "identifier": "id2",
        "name": "Camera A7C",
        "brand": "Sony",
        "item_type": "electronic",
        "expire_date": "never", 
        "desire":"5",
        "sales": {
            "platform": "taobao",
            "name": "system recomendation",
            "link":""
        }
    }
```

### Lookup item details
**Definition**

`GET /item/<identifier>`

**Response**

- 404: item not found
- 200: success


### Delete a item
**Definition**

`DELETE /item/<identifier>`

**Response**

- 404: item not found
- 204: success

