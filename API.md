
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