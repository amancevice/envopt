""" Fork of docopt. """

import os
import re
import docopt


__all__ = ['envopt']


class EnvOption(docopt.Option):
    @classmethod
    def parse(class_, option_description):
        """ Parse the options using virtually the same code as docopt.
            If an ENV variable exists with the same name as the placeholder,
            use that value over the traditional default. """
        short, long, argcount, value, env = None, None, 0, False, None
        options, _, description = option_description.strip().partition('  ')
        options = options.replace(',', ' ').replace('=', ' ')
        for s in options.split():
            if s.startswith('--'):
                long = s
            elif s.startswith('-'):
                short = s
            else:
                argcount = 1
                # Store option placeholder as ENV name
                env = s
        if argcount:
            matched = re.findall('\[default: (.*)\]', description, flags=re.I)
            value = matched[0] if matched else None
            # Replace value if the placeholder exists as an ENV variable
            if env is not None:
                value = os.getenv(env, value)
        return class_(short, long, argcount, value)


def envopt(doc, argv=None, help=True, version=None, options_first=False):
    return docopt.docopt(doc, argv, help, version, options_first)


docopt.Option = EnvOption
envopt.__doc__ = docopt.docopt.__doc__.replace('docopt', 'envopt')
