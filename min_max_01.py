import argparse
# defined command line options
# this also generates --help and error handling
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "integers",  # name on the CLI - drop the `--` for positional/required parameters
  metavar='N',
  nargs="+",  # 0 or more values expected => creates a list
  type=int,
  default=[1, 2, 3],  # default if nothing is provided
  help='list of values (default: 1, 2, 3)'
)

# parse the command line
args = CLI.parse_args()
min = 0
max = 0
for i in args.integers:
    if i < min:
        min = i
    elif i > max:
        max = i


# access CLI options
print("list: %r" % args.integers)
print("min: %d max: %d" % (min, max))

