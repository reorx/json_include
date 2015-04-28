# An extension for JSON to support file including

json-include is an extended way for JSON to support file including, it has two parts:

1. A syntax definition called **include syntax**.

2. A Python implementation to parse and build JSON file that contains **include syntax**.


## Syntax

json-include supports one and only one syntax, formatted as:

```json
{
    "...": "include(<json file name>)"
}
```

The include syntax means that this object (the whole `{"...": "include()"}`) in JSON
is a reference to the JSON file specified in `include(<json file name>)` notation,
and should be included into its place.

The included JSON should always be an object (dict) rather than an array (list),
to prevent implicit meaning and make sure we can get a clear view of the structure
without looking into the included JSON files.

In a normal JSON when we want to include another JSON on an attribute, it should
be written as follows:

```json
{
    "username": "alice",
    "profile": {
        "...": "include(profile_model.json)"
    }
}
```

In this JSON `profile_model.json` is included to present `profile` attribute,
if the content of `profile_model.json` is like:


```json
{
    "age": 18,
    "gender": "female"
}
```

then what we mean by the include syntax is that, when this JSON is being used
as a normal JSON, it should be seen as:

```json
{
    "username": "alice",
    "profile": {
        "age": 18,
        "gender": "female"
    }
}
```

## Python Implementation

### Installation

```
python setup.py install
```

### Usage

Try running the package as a script:

```
python -m json_include test/source_json/ a.json
```

The parsed and built result of `a.json` will be printed.

Further usage of `json_include` package is documented in its source code,
`test/` can also give you better understandings of how it works.


## TODOs

[ ] Prevent circluar include
[ ] Test circluar include
[ ] Test invalid syntax
