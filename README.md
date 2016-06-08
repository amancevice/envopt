# envopt

[![Build Status](https://travis-ci.org/amancevice/envopt.svg?branch=master)](https://travis-ci.org/amancevice/envopt)
[![PyPI version](https://badge.fury.io/py/envopt.svg)](https://badge.fury.io/py/envopt)

Wrapper for [docopt](https://github.com/docopt/docopt) to allow ENV variables to override default arguments.

Last updated: *`0.1.0`*

## Usage

Example docopt pydoc:

```python
""" 
This is an example.

Usage:
    python my_example.py [options]

Options:
    -a --a-opt OPT  # An example long option with magic default
    -b OPT          # An example short option with normal default [default: buzz]
    --cee           # An example long switch option
    -d              # An example short switch option
"""
```

* The value of `--a-opt` will be taken using command line, or from the `ENV` variable `$A_OPT`. If neither is provided the value will be `None`
* The value of `-b` will be taken from the command line, from the `ENV` variable `$B`. If neither is provided the `default` value `"buzz"` will be used
* The value of `--cee` will be take from the command line, or from the `ENV` variable `$CEE`. If neither is provided the flag will be set to `False`
* The value of `-d` will be take from the command line, or from the `ENV` variable `$D`. If neither is provided the flag will be set to `False`

Notice the `-a-opt` option has been defined using a "magic" default. Because the default has been defined as the string describing the corresponding `ENV` variable, the value will not only be taken from the `ENV` at execution time, but will also print when the `--help` flag is provided.

So, given the following `ENV` configuration:

```
A_OPT='Hello, World!'
```

The help message of this script would be:

```
This is an example.

Usage:
    python my_example.py [options]

Options:
    -a --a-opt OPT  # An example long option with magic default [default: Hello, World!]
    -b OPT          # An example short option with normal default [default: buzz]
    --cee           # An example long switch option
    -d              # An example short switch option
```

## Using a Prefix

Specifying a `env_prefix` value in the `envopt()` call will prefix `ENV` variables with this prefix right-padded with an underscore:

```python
import os
from envopt import envopt

os.environ['MY_A_OPT'] = 'fizz'
os.environ['MY_B']     = '1'
os.environ['MY_CEE']   = 'buzz'
os.environ['MY_D']     = '1'

print envopt(__doc__, env_prefix='MY')

{ '--a-opt' : 'fizz',
  '-b'      : 'buzz',
  '--cee'   : True,
  '-d'      : True }
```
