"""
This is an example.

Usage:
    my_example.py [options]

Options:
    -a --a-opt OPT  # An example long option
    -b OPT          # An example short option [default: foo]
    --cee           # An example long switch option
    -d              # An example short switch option
"""

import os
import mock
from envopt.envopt import dochelper
from envopt.envopt import envopt
from envopt.envopt import EnvOption


class TestEnviron(object):
    def setup(self):
        os.environ = {}
        EnvOption.set_prefix(None)

    def test_dochelper(self):
        EnvOption.set_prefix('MYPREFIX_')
        os.environ['MYPREFIX_A_OPT'] = 'FUZZ'
        returned = dochelper(__doc__)
        expected = __doc__.replace(
            "-a --a-opt OPT  # An example long option",
            "-a --a-opt OPT  # An example long option [default: FUZZ]")
        print(returned)
        print(expected)
        assert returned == expected

    def test_no_env_defaults(self):
        returned = envopt(__doc__, argv=())
        expected = {
            '--a-opt': None,
            '--cee': False,
            '-b': 'foo',
            '-d': False}
        assert returned.keys() == expected.keys()
        for key, val in returned.items():
            assert returned[key] == expected[key]

    def test_long_opt_with_env(self):
        os.environ['A_OPT'] = 'bar'
        os.environ['CEE'] = 'true'
        os.environ['B'] = 'baz'
        os.environ['D'] = 'true'
        returned = envopt(__doc__, argv=())
        expected = {
            '--a-opt': 'bar',
            '--cee': True,
            '-b': 'baz',
            '-d': True}
        assert returned.keys() == expected.keys()
        for key, val in returned.items():
            assert returned[key] == expected[key]

    def test_long_opt_with_env_and_override(self):
        os.environ['A_OPT'] = 'far'
        os.environ['B'] = 'faz'
        argv = '--a-opt', 'buzz', '--cee', '-b', 'fizz', '-d'
        returned = envopt(__doc__, argv=argv)
        expected = {
            '--a-opt': 'buzz',
            '--cee': True,
            '-b': 'fizz',
            '-d': True}
        assert returned.keys() == expected.keys()
        for key, val in returned.items():
            assert returned[key] == expected[key]

    def test_long_opt_defaults_with_prefix(self):
        returned = envopt(__doc__, argv=(), prefix='MY_')
        expected = {
            '--a-opt': None,
            '--cee': False,
            '-b': 'foo',
            '-d': False}
        assert returned.keys() == expected.keys()
        for key, val in returned.items():
            assert returned[key] == expected[key]

    def test_long_opt_with_env_with_prefix(self):
        os.environ['MY_A_OPT'] = 'bar'
        os.environ['MY_CEE'] = 'true'
        os.environ['MY_B'] = 'baz'
        os.environ['MY_D'] = 'true'
        returned = envopt(__doc__, argv=(), prefix='MY_')
        expected = {
            '--a-opt': 'bar',
            '--cee': True,
            '-b': 'baz',
            '-d': True}
        assert returned.keys() == expected.keys()
        for key, val in returned.items():
            assert returned[key] == expected[key]

    def test_long_opt_with_env_and_override_with_prefix(self):
        os.environ['MY_A_OPT'] = 'far'
        os.environ['MY_B'] = 'faz'
        argv = '--a-opt', 'buzz', '--cee', '-b', 'fizz', '-d'
        returned = envopt(__doc__, argv=argv, prefix='MY_')
        expected = {
            '--a-opt': 'buzz',
            '--cee': True,
            '-b': 'fizz',
            '-d': True}
        assert returned.keys() == expected.keys()
        for key, val in returned.items():
            assert returned[key] == expected[key]
