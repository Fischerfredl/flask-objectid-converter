|version| |license| |pyversions| |pipeline status| |coverage|

flask-objectid-converter
========================

Provides url converters for flask to support pymonogs ObjectIDs

I found the snippet from `here <http://flask.pocoo.org/snippets/106/>`__
by Armin Ronacher but could not find a package for it.

Ideas for extended functionality: See ToDo.

Usage
-----

-  add the Converter to the flask app
-  use it in routes ### Add Converter to app: \`\`\`python from flask
   import Flask from objectid\_converter import ObjectIDConverter

app = Flask(\ **name**) app.url\_map.converters['objectid'] =
ObjectIDConverter ``### Use in routes``\ python @app.route('/users/')
def get\_user(oid): return User.objects.get(id=oid) \`\`\`

Throws 404 if the requested value cant be decoded

get route via url\_for
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from flask import url_for
    url_for(get_user, oid=User.id)

Encoding and Decoding
---------------------

The converter encodes the objectid to base64. For manual encoding and
decoding use the itsdangerous library:

.. code:: python

    import bson
    from itsdangerous import base64_encode, base64_decode

    # encoding
    oid = bson.ObjectId()
    base64_encode(oid.binary)

    # decoding
    value = 'SomeBase64DecodedString'
    bson.ObjectId(base64_decode(value))

Testing
-------

.. code:: python

    python setup.py test

ToDo
----

Make a proper flask extension with **init\_app**, **encode**, **decode**
functions, **configuration** of conversion algorithm (specify alphabet).

base64 is sufficient for me. So i will not touch this right now. If
somebody needs this, let me know.

.. |version| image:: https://img.shields.io/pypi/v/flask-objectid-converter.svg
   :target: https://pypi.python.org/pypi/flask-objectid-converter
.. |license| image:: https://img.shields.io/pypi/l/flask-objectid-converter.svg
   :target: https://pypi.python.org/pypi/flask-objectid-converter
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/flask-objectid-converter.svg
   :target: https://pypi.python.org/pypi/flask-objectid-converter
.. |pipeline status| image:: https://travis-ci.org/Fischerfredl/flask-objectid-converter.svg?branch=master
   :target: https://travis-ci.org/Fischerfredl/flask-objectid-converter
.. |coverage| image:: https://img.shields.io/codecov/c/github/fischerfredl/flask-objectid-converter.svg
   :target: https://codecov.io/gh/Fischerfredl/flask-objectid-converter
