import os
from setuptools import setup

NAME    = "envopt"
VERSION = "0.1.1"
AUTHOR  = "amancevice"
EMAIL   = "smallweirdnum@gmail.com"
DESC    = "Wrap docopt to allow ENV variables as argument defaults"

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.7",
    "Topic :: Utilities" ]
REQUIRES = ["docopt==0.6.2"]
TEST_REQUIRES = ["nose", "mock"]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name                 = NAME,
    version              = VERSION,
    author               = AUTHOR,
    author_email         = EMAIL,
    packages             = [ NAME ],
    package_data         = { "%s" % NAME : ['README.md'] },
    include_package_data = True,
    url                  = 'http://www.smallweirdnumber.com',
    description          = DESC,
    long_description     = read('README.md'),
    classifiers          = CLASSIFIERS,
    install_requires     = REQUIRES,
    test_requires        = TEST_REQUIRES,
    test_suite           = "nose.collector" )
