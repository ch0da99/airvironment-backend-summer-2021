# RBT Summer Internship 2021 Backend

Backend code written in Python for Airvironment 2021 Summer internship.

A running application is live on
`https://airvironment.live`

It can be started locally in developer mode by running:

```bash
python3 run.py
```

or in production mode by running following commands:

```bash
export FLASK_APP=run.py
flask run
```

Before running the project, a `.env` file should be created in the root
directory with following key/values:

```
DEBUG=1
ENVIRONMENT="Development"
DATABASE_URL="postgresql+psycopg2://<db_user>:<db_password>@<db_host>:<db_port>/<db_name>"
```

## Requests and Responses
GET /api/measurements
Response:
```JSON
{
   "meta": {
      "total": "Int",
      "page": "Int",
      "per_page": "Int"
   },
   "results": [
       {
          "id": "Int",
          "pollution": "Float",
          "temperature": "Float",
          "humidity": "Float",
          "created": "DateTime"
       }
   ]
}
```

POST /api/measurements
Post Request:
```JSON
{
   "pollution": "Float, required",
   "temperature": "Float, required",
   "humidity": "Float, required"
}
```

Response:
```JSON
{
   "id": "Int",
   "pollution": "Float",
   "temperature": "Float",
   "humidity": "Float",
   "created": "DateTime"
}
```

GET /api/measurements/latest
Response:
```JSON
{
  "id": "Int",
  "pollution": "Float",
  "temperature": "Float",
  "humidity": "Float",
  "created": "DateTime"
}

GET /api/measurements/<int: id>
Response:
```JSON
{
   "id": "Int",
   "pollution": "Float",
   "temperature": "Float",
   "humidity": "Float",
   "created": "DateTime"
}
```

PATCH /api/measurements/<int: id>
Post Request:
```JSON
{
   "pollution": "Float, optional",
   "temperature": "Float, optional",
   "humidity": "Float, optional"
}
```

Response:
```JSON
{
   "id": "Int",
   "pollution": "Float",
   "temperature": "Float",
   "humidity": "Float",
   "created": "DateTime"
}
```