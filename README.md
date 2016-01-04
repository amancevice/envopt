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
            -a --a-opt MY_OPT1  # An example option [default: foo]
            -b --b-opt MY_OPT2  # Another example option [default: bar]
            -c --c-opt MY_OPT3  # Yet another example option [default: baz] """
```

Parsing this example without any `ENV` variables set would yield:

```python
from envopt import envopt

print envopt(__doc__)

{ '--a-opt': 'foo',
  '--b-opt': 'bar',
  '--c-opt': 'baz' }
```

However, setting `ENV` variables `MY_OPT1`, `MY_OPT2`, or `MY_OPT3` will override the given defaults:

```python
import os
from envopt import envopt

os.environ['MY_OPT1'] = 'fe'
os.environ['MY_OPT2'] = 'fi'
os.environ['MY_OPT3'] = 'fo'

print envopt(__doc__)

{ '--a-opt': 'fe',
  '--b-opt': 'fi',
  '--c-opt': 'fo' }
```
