"""
Template
"""

from sys import stderr
from argparse import ArgumentParser, Namespace

def main():
    """
    Say Hello
    """
    parser = get_argument_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help(stderr)

def get_argument_parser() -> ArgumentParser:
    """
    Get command line arguments.
    """
    parser = ArgumentParser(
        description="Say Hello")

    subparsers = parser.add_subparsers(title="subcommands")

    parser_count_above_below = subparsers.add_parser("say-hello")
    parser_count_above_below.add_argument('-n', '--name',
                                         help="a name")
    parser_count_above_below.set_defaults(func=do_say_hello)

    return parser

def do_say_hello(args: Namespace) -> None:
    print("Hello {}".format(args.name))

if __name__ == "__main__":
    main()