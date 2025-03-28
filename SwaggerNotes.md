# Notes for how to integrate Swagger with Flask app

## Installing the required packages

1. first we need to install swagger packages for flask

   in addition to the installed packages we install

```
pip install flask flask-swagger-ui flask-restx
```

2. inside `app.py` we import

```python
from flask import Flask
from flask_restx import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
```

3. configure the swagger ui in `app.py`

```python
# Setup Flask-RESTX API
api = Api(app, version='1.0', title='Simple API',
          description='A simple API with OpenAPI 3.0 documentation')

# Create a Swagger UI blueprint
SWAGGER_URL = '/swagger'  # Swagger UI URL endpoint
API_URL = '/static/swagger.json'  # Swagger JSON URL endpoint

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Flask Swagger UI Example"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# API Namespace
ns = api.namespace('api', description='Sample operations')
```

4. we create the Swagger JSON file

```json
{
  "swagger": "2.0",
  "info": {
    "title": "Flask Swagger UI Example",
    "description": "This is a simple API to demonstrate Swagger UI integration with Flask",
    "version": "1.0.0"
  },
  "paths": {
    "/api/greet": {
      "get": {
        "summary": "Greet endpoint",
        "responses": {
          "200": {
            "description": "A greeting message",
            "schema": {
              "type": "object",
              "properties": {
                "message": {
                  "type": "string"
                }
              }
            }
          }
        }
      }
    },
    "/api/square/{number}": {
      "get": {
        "summary": "Square a number",
        "parameters": [
          {
            "name": "number",
            "in": "path",
            "type": "integer",
            "required": true,
            "description": "The number to square"
          }
        ],
        "responses": {
          "200": {
            "description": "The squared result",
            "schema": {
              "type": "object",
              "properties": {
                "result": {
                  "type": "integer"
                }
              }
            }
          }
        }
      }
    }
  }
}
```
