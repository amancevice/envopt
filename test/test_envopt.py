"""
This is an example.

Usage:
    my_example.py [options]

Options:
    -a --a-opt OPT  # An example long option [default: foo]
    -b OPT          # An example short option [default: bar]
    --cee           # An example long switch option
    -d              # An example short switch option
"""


import os
from envopt import envopt
from nose.tools import assert_dict_equal


def test_long_opt_defaults():
    returned = envopt(__doc__)
    expected = {
        '--a-opt' : 'foo',
        '--cee'   : False,
        '-b'      : 'bar',
        '-d'      : False }
    assert_dict_equal(returned, expected)


def test_long_opt_with_env():
    os.environ['A_OPT'] = 'bar'
    os.environ['CEE']   = 'true'
    os.environ['B']     = 'baz'
    os.environ['D']     = 'true'
    returned = envopt(__doc__)
    expected = {
        '--a-opt' : 'bar',
        '--cee'   : True,
        '-b'      : 'baz',
        '-d'      : True }
    assert_dict_equal(returned, expected)


def test_long_opt_with_env_and_override():
    os.environ['A_OPT'] = 'far'
    os.environ['B']     = 'faz'
    argv = '--a-opt', 'buzz', '--cee', '-b', 'fizz', '-d'
    returned = envopt(__doc__, argv=argv)
    expected = {
        '--a-opt' : 'buzz',
        '--cee'   : True,
        '-b'      : 'fizz',
        '-d'      : True }
    assert_dict_equal(returned, expected)


def test_long_opt_defaults_with_prefix():
    returned = envopt(__doc__, env_prefix='MY')
    expected = {
        '--a-opt' : 'foo',
        '--cee'   : False,
        '-b'      : 'bar',
        '-d'      : False }
    assert_dict_equal(returned, expected)


def test_long_opt_with_env_with_prefix():
    os.environ['MY_A_OPT'] = 'bar'
    os.environ['MY_CEE']   = 'true'
    os.environ['MY_B']     = 'baz'
    os.environ['MY_D']     = 'true'
    returned = envopt(__doc__, env_prefix='MY')
    expected = {
        '--a-opt' : 'bar',
        '--cee'   : True,
        '-b'      : 'baz',
        '-d'      : True }
    assert_dict_equal(returned, expected)


def test_long_opt_with_env_and_override_with_prefix():
    os.environ['MY_A_OPT'] = 'far'
    os.environ['MY_B']     = 'faz'
    argv = '--a-opt', 'buzz', '--cee', '-b', 'fizz', '-d'
    returned = envopt(__doc__, argv=argv, env_prefix='MY')
    expected = {
        '--a-opt' : 'buzz',
        '--cee'   : True,
        '-b'      : 'fizz',
        '-d'      : True }
    assert_dict_equal(returned, expected)
