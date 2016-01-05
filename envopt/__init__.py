""" Fork of docopt. """

import os
import re
import docopt


__all__ = ['envopt']


_ENV_PREFIX = None


class EnvOption(docopt.Option):
    """ Override of the docopt.Option class. """
    @classmethod
    def parse(cls, option_description):
        """ Parse the options using virtually the same code as docopt.
            If an ENV variable exists with the same name as the placeholder,
            use that value over the traditional default. """
        short, lng, argcount, value, env = None, None, 0, False, None
        options, _, description = option_description.strip().partition('  ')
        options = options.replace(',', ' ').replace('=', ' ')
        for sec in options.split():
            if sec.startswith('--'):
                lng = env = sec
            elif sec.startswith('-'):
                short = env = sec
            else:
                argcount = 1
            env = env.lstrip('-').replace('-', '_').upper()
        env = _ENV_PREFIX+env
        # Fetch input value
        if argcount:
            matched = re.findall(r'\[default: (.*)\]', description, flags=re.I)
            value = matched[0] if matched else None
            # Replace value if the placeholder exists as an ENV variable
            value = os.getenv(env, value)
        # Fetch switch value
        elif value is False and os.getenv(env, '').lower() in ('true', '1'):
            value = True
        return cls(short, lng, argcount, value)


def envopt(doc, argv=None, hlp=True, version=None, options_first=False, env_prefix=None):
    """ Override of docopt.docopt(). """
    globals()['_ENV_PREFIX'] = '' if env_prefix is None else "%s_" % env_prefix
    return docopt.docopt(doc, argv, hlp, version, options_first)


docopt.Option = EnvOption
envopt.__doc__ = docopt.docopt.__doc__.replace('docopt', 'envopt')
