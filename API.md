
### Create a new vending machine

POST `/machines/`

Request 
`

    {
        "name": "lydia",
        "location": "ol kalau",
        "manager": 1,
        "currency": "KES"
    }`

Response

    {
        "id": 7,
        "name": "lydia",
        "location": "ol kalau",
        "date_installed": "2022-08-24T17:05:18.375063Z",
        "manager": 1,
        "currency": "KES"
    }

