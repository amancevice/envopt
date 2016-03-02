""" Fork of docopt. """

import os
import re
import sys
import docopt


__all__ = ['envopt']


class EnvOption(docopt.Option):
    """ Override of the docopt.Option class. """
    __prefix__ = None

    @classmethod
    def prefix(cls):
        return cls.__prefix__ or ''

    @classmethod
    def set_prefix(cls, prefix):
        cls.__prefix__ = prefix

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
        env = cls.prefix() + env
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
    if env_prefix:
        EnvOption.set_prefix("%s_" % env_prefix)
    return docopt.docopt(dochelper(doc), argv, hlp, version, options_first)


def dochelper(doc):
    doc_ = doc
    for default in docopt.parse_defaults(doc):
        optname = default.name.strip('-').replace('-','_').upper()
        envname = "%s%s" % (EnvOption.__prefix__ or '', optname)
        optval = os.getenv(envname)
        search = r"(%s.*?)\[default: (\$.*?)\]$" % (default.name)
        replace = "\\1[default: %s]" % optval if optval is not None else "\\1"
        doc_ = re.sub(search, replace, doc_, flags=re.MULTILINE)
    return doc_

docopt.Option = EnvOption
envopt.__doc__ = docopt.docopt.__doc__.replace('docopt', 'envopt')
