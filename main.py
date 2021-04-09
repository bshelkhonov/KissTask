import argparse

from src.solver import Solver


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("text_file", help="Text with cipher",
                        type=argparse.FileType('r'))
    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()
    solver = Solver(args.text_file)
    solver.run()


if __name__ == "__main__":
    main()
