# RESTful API for Ramen Rating
A Simple RESTful API in Python.

## Install
    pip3 install -r requirements.txt

## Run the app
    python main.py

# REST API
The REST API for the ramen rating app is described below.

## Get list of Reviews

### Request

`GET /reviews`

    curl -i -H 'Accept: application/json' http://localhost:5000/reviews

### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 182
    Server: Werkzeug/1.0.1 Python/3.8.2
    Date: Wed, 28 Apr 2021 16:59:23 GMT
    
    [
        {
            "id": 1,
            "brand": "Westbrae",
            "variety": "Miso Ramen",
            "style": "Pack",
            "country": "USA",
            "stars": "0.5",
            "top_ten": ""
        },
        ....
        {
            "id": 2580,
            "brand": "New Touch",
            "variety": "T's Restaurant Tantanmen ",
            "style": "Cup",
            "country": "Japan",
            "stars": "3.75",
            "top_ten": ""
        }
    ]

## Get list of Reviews filter by Country

### Request

`GET /reviews?country=Japan`

    curl -i -H 'Accept: application/json' 'http://localhost:5000/reviews?country=USA'

### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 182
    Server: Werkzeug/1.0.1 Python/3.8.2
    Date: Wed, 28 Apr 2021 16:59:23 GMT
    
    [
        ...
        {
            "id": 2578,
            "brand": "Nissin",
            "variety": "Cup Noodles Chicken Vegetable",
            "style": "Cup",
            "country": "USA",
            "stars": "2.25",
            "top_ten": ""
        }
    ]

## Get list of Reviews by Partial Text

### Request

`GET /reviews?query=seaweed`

    curl -i -H 'Accept: application/json' 'http://localhost:5000/reviews?query=seaweed'

### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 1529
    Server: Werkzeug/1.0.1 Python/3.8.2
    Date: Wed, 28 Apr 2021 17:38:46 GMT
    
    [
        {
            "id": 712,
            "brand": "Four Seas",
            "variety": "Seaweed",
            "style": "Bowl",
            "country": "Hong Kong",
            "stars": "3.25",
            "top_ten": ""
        },
        {
            "id": 1172,
            "brand": "Koyo",
            "variety": "Seaweed Ramen Made With Organic Noodles",
            "style": "Pack",
            "country": "USA",
            "stars": "2.75",
            "top_ten": ""
        },
        {
            "id": 1365,
            "brand": "Four Seas",
            "variety": "Seaweed Hot & Spicy Instant Noodle Mushroom & Beef Flavour",
            "style": "Bowl",
            "country": "Hong Kong",
            "stars": "3.5",
            "top_ten": ""
        },
        {
            "id": 2093,
            "brand": "Oni Hot Pot",
            "variety": "Seaweed Flavour Noodle",
            "style": "Pack",
            "country": "Taiwan",
            "stars": "2",
            "top_ten": ""
        },
        {
            "id": 2254,
            "brand": "Nissin",
            "variety": "Disney Cuties Instant Noodle Seaweed Flavour",
            "style": "Cup",
            "country": "Thailand",
            "stars": "3",
            "top_ten": ""
        },
        {
            "id": 2382,
            "brand": "Nongshim",
            "variety": "Seaweed Instant Noodle",
            "style": "Cup",
            "country": "South Korea",
            "stars": "0.5",
            "top_ten": ""
        },
        {
            "id": 2472,
            "brand": "GGE",
            "variety": "Noodle Snack Wheat Cracks Seaweed Flavor",
            "style": "Pack",
            "country": "Taiwan",
            "stars": "3.5",
            "top_ten": ""
        }
    ]

## Create a new Review

### Request

`POST /reviews`

    curl -i -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"brand":"GGE","variety":"Noodle Snack Wheat Cracks Seaweed Flavor","style":"Pack","country":"Taiwan","stars":"3.5","top_ten":""}' -X POST http://localhost:5000/reviews

#### Request-Body
    {
        "brand": "GGE",
        "variety": "Noodle Snack Wheat Cracks Seaweed Flavor",
        "style": "Pack",
        "country": "Taiwan",
        "stars": "3.5",
        "top_ten": ""
    }

### Response

    HTTP/1.0 201 CREATED
    Content-Type: application/json
    Content-Length: 183
    Server: Werkzeug/1.0.1 Python/3.8.2
    Date: Wed, 28 Apr 2021 17:47:59 GMT
    
    {
        "id": 2581,
        "brand": "GGE",
        "variety": "Noodle Snack Wheat Cracks Seaweed Flavor",
        "style": "Pack",
        "country": "Taiwan",
        "stars": "3.5",
        "top_ten": ""
    }

## Edit Review
This API allows to update a proportion of the review's details

### Request

`PUT /reviews/{id}`

    curl -i -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"brand":"Anything"}' -X PUT http://localhost:5000/reviews/2581

#### Request-Body
    {
        "brand": "GGE"
    }

### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 188
    Server: Werkzeug/1.0.1 Python/3.8.2
    Date: Wed, 28 Apr 2021 17:49:48 GMT
    
    {
        "id": 2581,
        "brand": "Anything",
        "variety": "Noodle Snack Wheat Cracks Seaweed Flavor",
        "style": "Pack",
        "country": "Taiwan",
        "stars": "3.5",
        "top_ten": ""
    }

## Delete Review

### Request

`DELETE /reviews/{id}`

    curl -i -X DELETE http://localhost:5000/reviews/2581

### Response

    HTTP/1.0 204 NO CONTENT
    Content-Type: application/json
    Server: Werkzeug/1.0.1 Python/3.8.2
    Date: Wed, 28 Apr 2021 17:50:39 GMT