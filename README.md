# envopt
Wrapper for [docopt](https://github.com/docopt/docopt) to allow ENV variables to override default arguments.


## Usage

Example docopt pydoc:

```python
__doc__ = \
    """ This is an example.

        Usage:
            python my_example.py [options]

        Options:
            -a --a-opt OPT  # An example long option [default: foo]
            -b OPT          # An example short option [default: bar]
            --cee           # An example long switch option
            -d              # An example short switch option """
```

Parsing this example without any `ENV` variables set would yield:

```python
from envopt import envopt

print envopt(__doc__)

{ '--a-opt' : 'foo',
  '-b'      : 'bar',
  '--cee'   : False,
  '-d'      : False }
```

However, setting `ENV` variables `A_OPT`, `B`, `CEE`, or `D` will override the given defaults:

```python
import os
from envopt import envopt

os.environ['A_OPT'] = 'fizz'
os.environ['B']     = '1'
os.environ['CEE']   = 'buzz'
os.environ['D']     = '1'

print envopt(__doc__)

{ '--a-opt' : 'fizz',
  '-b'      : 'buzz',
  '--cee'   : True,
  '-d'      : True }
```

For switch-style arguments, the existence of the `ENV` variable is enough to set the value to `True`. Unset the variable to return the default value to `False`.

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
