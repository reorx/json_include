An extension for JSON to support file inclusion
===============================================

json-include is an extended way for JSON to support file inclusion, it has two parts:

1. A syntax definition called **include syntax**.

2. A Python implementation to parse and build JSON file that contains **include syntax**.


Syntax
------

json-include supports an extended syntax called **include syntax** in JSON,
formatted as:

.. code-block:: json

    {
        "...": "<json file name>"
    }

The include syntax means that this object (the whole ``{"...": "<json file name>"}``) in JSON
is a reference to the JSON file named in ``<json file name>`` notation,
and should be included into its place.

The included JSON should always be an object (dict) rather than an array (list),
to prevent implicit meaning and make sure we can get a clear view of the structure
without looking into the included JSON files.

In a normal JSON when we want to include another JSON on an attribute, it should
be written as follows:

.. code-block:: json

    {
        "username": "alice",
        "profile": {
            "...": "<profile_model.json>"
        }
    }

In this JSON a ``profile_model.json`` is included to present ``profile`` attribute,
if the content of ``profile_model.json`` is like:

.. code-block:: json

    {
        "age": 18,
        "gender": "female"
    }

then what we mean by the include syntax is that, when this JSON is being used
as a normal JSON, it should be seen as:

.. code-block:: json

    {
        "username": "alice",
        "profile": {
            "age": 18,
            "gender": "female"
        }
    }

To ture JSON with include syntax into a normal JSON, a build process is needed,
that's what the implementation does.

Python Implementation
---------------------

Implementation could be of any language as long as it can understand the include syntax
and output as expected, this repo contains a Python implementation for use.

Installation
~~~~~~~~~~~~

::

    pip install json-include

Usage
~~~~~

By installation a command called ``json-include`` will be registerd as an entry point,
use it as follows::

    usage: json-include [-h] DIR FILE

    Command line tool to build JSON file by include syntax.

    positional arguments:
      DIR         The directory path of source json files
      FILE        The name of the source json file

    optional arguments:
      -h, --help  show this help message and exit

For example::

    json-include test/source_json/ c.json

The parsed and built result of ``c.json`` will be printed.

Further usage of ``json_include`` package is documented in its source code,
and ``test/`` can also give you better understandings of how it works.

TODOs
-----

- [ ] Prevent circluar inclusion
- [ ] Test circluar inclusion
- [ ] Test invalid syntax
