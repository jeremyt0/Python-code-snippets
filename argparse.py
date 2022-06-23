
# argparse library
import argparse
import sys
PARSER = argparse.ArgumentParser(
        description="""Description of argparser""",
        formatter_class=argparse.RawDescriptionHelpFormatter)
PARSER.add_argument("--argument1", type=str, required=True,
    default = "", help="This is the first argument to pass in cmd")

# Just show the help if no arguments
if len(sys.argv)==1:
    PARSER.print_help(sys.stderr)
    sys.exit(1)

# All variables are stored in ARGS
ARGS = PARSER.parse_args()
var1 = ARGS.argument1

