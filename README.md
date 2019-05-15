[![version](https://img.shields.io/pypi/v/flask-objectid-converter.svg)](https://pypi.python.org/pypi/flask-objectid-converter)
[![license](https://img.shields.io/pypi/l/flask-objectid-converter.svg)](https://pypi.python.org/pypi/flask-objectid-converter)
[![pyversions](https://img.shields.io/pypi/pyversions/flask-objectid-converter.svg)](https://pypi.python.org/pypi/flask-objectid-converter)
[![pipeline status](https://travis-ci.org/Fischerfredl/flask-objectid-converter.svg?branch=master)](https://travis-ci.org/Fischerfredl/flask-objectid-converter)
[![coverage](https://img.shields.io/codecov/c/github/fischerfredl/flask-objectid-converter.svg)](https://codecov.io/gh/Fischerfredl/flask-objectid-converter)

# flask-objectid-converter
Provides url converters for flask to support pymonogs ObjectIDs

I found the snippet from [here](http://flask.pocoo.org/snippets/106/) by Armin Ronacher but could not find a package for it.

## Usage
* add the Converter to the flask app
* use it in routes

### Add Converter to app:

The package defines two converters to use: 
* ObjectIDConverter: stringify the id
* Base64ObjectIDConverter: produces smaller strings by encoding to base64

```python
from flask import Flask
from flask_objectid_converter import ObjectIDConverter

app = Flask(__name__)
app.url_map.converters['objectid'] = ObjectIDConverter
```

### Use in routes
```python
@app.route('/users/<objectid:oid>')
def get_user(oid):
    return User.objects.get(id=oid)
``` 

Throws 404 if the requested value cant be decoded

### get route via url_for
```python
from flask import url_for
url_for(get_user, oid=User.id)
```

## Testing
```python
python setup.py test
```

## Possible extensions

Make the package a proper flask extension with **init_app**, **encode**, **decode** functions, **configuration** of conversion algorithm (specify alphabet)...

## Changelog

* 1.0.0: Inital version. Encodes to base64 by default.
* 2.0.0: Provide two converter classes. A simple one and a base64 encoding one. Drop python2 support.