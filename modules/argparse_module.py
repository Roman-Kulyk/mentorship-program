"""
The argparse module makes it easy to write user-friendly command-line interfaces.
The program defines what agruments it requires, and argparse will figure out how
to parse those out of sys.argv. The argparse module also automatically generates
help and usage messages. The module will also issue errors when users give the 
program invalid agruments.
"""
# Intoducing Positional arguments


# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number",
#                     type =int)
# args = parser.parse_args()
# print(args.square**2)


# Introducing Optional arguments


# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")


# Combining Positional and Optional arguments


# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int, choices=[0,1,2],
#                     help="increase output verbosity")
# args = parser.parse_args()
# print(args)
# answer = args.square**2
# if args.verbosity == 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.square}^2 =={answer}")
# else:
#     print(answer)


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
print(args)
answer = args.square**2
if args.verbosity >= 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
    print(f"{args.square}^2 >={answer}")
else:
    print(answer)