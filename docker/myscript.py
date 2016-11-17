"""
Sample envopt script.

Usage:
    myscript.py [options]

Options:
    -a --option-a OPT  # A
    -b --option-b OPT  # B
    -c --option-c OPT  # C [default: I am hardcoded in myscript.py]
    -d --option-d OPT  # D
"""

from envopt import envopt


if __name__ == "__main__":
    args = envopt(__doc__)
    for item in sorted(args.items()):
        print("{} :: {}".format(*item))
