
### Vending Machine requests
#### Create new vending machine
POST `/machines/`

Request 

    {
        "name": "lydia",
        "location": "ol kalau",
        "manager": 1,
        "currency": "KES"
    }

Response

    {
        "id": 7,
        "name": "lydia",
        "location": "ol kalau",
        "date_installed": "2022-08-24T17:05:18.375063Z",
        "manager": 1,
        "currency": "KES"
    }


### Coin requests
#### Create new coin
POST `/coins/`

Request

    {
        "coin": 25,
        "total_available": 20,
        "vending_machine": 1
    }

Response
   
    {
        "id": 5,
        "coin": 25,
        "total_available": 20,
        "vending_machine": 1
    }

GET `/coins/`
#### List all coins
Response

    [
        {
            "id": 2,
            "coin": 1,
            "total_available": 20,
            "vending_machine": 1
        },
        {
            "id": 1,
            "coin": 5,
            "total_available": 20,
            "vending_machine": 1
        },
        {
            "id": 3,
            "coin": 10,
            "total_available": 20,
            "vending_machine": 1
        }
    ]


### Product requests
#### Create new product
POST `/products/`

Request

    {
        "name": "magazine",
        "price": 120.0,
        "quantity": 30,
        "vending_machine": 1
    }

Response

    {
        "name": "magazine",
        "price": 120.0,
        "quantity": 30,
        "vending_machine": 1
    }


GET `/products/`

Response 

    [
        {
            "id": 3,
            "name": "Wine",
            "price": 120.0,
            "quantity": 0,
            "code": "0YSL4",
            "vending_machine": 1
        },
        {
            "id": 1,
            "name": "bun",
            "price": 34.0,
            "quantity": 0,
            "code": "RLK6F",
            "vending_machine": 12
        },
        {
            "id": 2,
            "name": "water bottle",
            "price": 29.0,
            "quantity": 0,
            "code": "ZQ18V",
            "vending_machine": 1
        }
    ]


### Product Order requests
#### Create new product order

Request

POST `/orders/`

    {
        "amount_paid": 50.0,
        "product": "RKL6F"
    }
GET `/orders/` 

    [
        {
            "id": 8,
            "amount_paid": 50.0,
            "change_given": -21.0,
            "order_status": "INCOMPLETE",  
            "order_date": "2022-08-27T06:28:33.353003Z",
            "product": 2,
            "customer": 1
        },
        {
            "id": 1,
            "amount_paid": 50.0,
            "change_given": -16.0,
            "order_status": "COMPLETE",
            "order_date": "2022-08-27T05:48:29.104188Z",
            "product": 1,
            "customer": 1
        }  
    ]