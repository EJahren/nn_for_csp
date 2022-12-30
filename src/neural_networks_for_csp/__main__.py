import argparse
import sys

from neural_networks_for_csp import __version__


def make_parser(prog):
    parser = argparse.ArgumentParser(
        prog=prog, description="Experiments of using neural networks to solve csp"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    return parser


def parse_args(argv):
    parser = make_parser(argv[0])
    return parser.parse_args(argv[1:])


def run_neural_networks_for_csp(args):
    # TODO
    pass


def parse_args_and_run(argv):
    run_neural_networks_for_csp(parse_args(argv))


def main():
    parse_args_and_run(sys.argv)


if __name__ == "__main__":
    main()
