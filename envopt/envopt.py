""" EnvOpt overrides """

import os
import re
import docopt


class EnvOption(docopt.Option):
    """ Override of the docopt.Option class. """
    __prefix__ = None

    @classmethod
    def prefix(cls):
        """ Get ENV prefix. """
        return cls.__prefix__ or ''

    @classmethod
    def set_prefix(cls, prefix):
        """ Set ENV prefix. """
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


# pylint: disable=too-many-arguments
def envopt(doc, argv=None, hlp=True, version=None, options_first=False, env_prefix=None):
    """ Override of docopt.docopt(). """
    if env_prefix:
        EnvOption.set_prefix("%s_" % env_prefix)
    return docopt.docopt(dochelper(doc), argv, hlp, version, options_first)


def dochelper(doc):
    """ Helper to add defaults from ENV to pydoc. """
    doc_ = doc
    for default in docopt.parse_defaults(doc):
        optname = default.name.strip('-').replace('-', '_').upper()
        envname = EnvOption.prefix() + optname
        optval = os.getenv(envname)
        if optval is not None:
            search = r"(^ *(%s|%s|%s %s) .*?$)" \
                % (default.short, default.long, default.short, default.long)
            for match in re.findall(search, doc, re.MULTILINE):
                whole = match[0]
                if not re.search(r"\[default: .*?\]", whole):
                    doc_ = doc_.replace(whole, "%s [default: %s]" % (whole, optval))
    return doc_


docopt.Option = EnvOption
envopt.__doc__ = docopt.docopt.__doc__.replace('docopt', 'envopt')
