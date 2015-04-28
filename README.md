# An extension for JSON to support file including

json-include is a extended way for JSON to support file including, it has two parts:

1. An expression definition

2. A Python implementation to parse and build JSON file that contains the expression.


## The Expression

json-include support one and only expression, formated as:

        {
            "...": "include(<json file name>)"
        }

The expression means that this object (the whole `{"...": "include()"}`) in JSON
is a reference to the JSON file specified in `include(<json file name>)` notation,
and should be included into its place.

The included JSON should always be an object (dict) rather than an array (list),
to prevent implicit meaning and make sure we can get a clear view of what
the structure is like without looking into the included JSON files.

In normal JSON when we want to include another JSON on an attribute, the expression
is write as follows:

        {
            "username": "alice",
            "profile": {
                "...": "include(profile_model.json)"
            }
        }

if the content of `profile_model.json` is like:

        {
            "age": 18,
            "gender": "female"
        }

then what we mean by the expression is that the previous JSON should be like this
when it's being used as a normal JSON:

        {
            "username": "alice",
            "profile": {
                "age": 18,
                "gender": "female"
            }
        }

## The Python Implementation

### Install

        python setup.py install

### Usage

Try running the package as a script:

        python -m json_include test/source_json/ a.json

The parsed and built result of a.json will be printed.

Further usage of `json_include` package is documented in its source code,
test cases can also give you better understandings of how it works.
