import sys
import argparse
from dateutil.parser import parse
from dts.seq import seqGen, DT_UNIT, DTS_DEFAULT_UNIT, DTS_DEFAULT_INTERVAL, DTS_DEFAULT_FORMAT

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.
    parser = argparse.ArgumentParser(description='seq for datetime')
    parser.add_argument('FIRST', metavar='FIRST',
            help='first date of the seq. For example, 2018-05-01, 20180501, 20180501-0900, 2018-05-01T09:00')
    parser.add_argument('LAST', metavar='LAST',
            help='last date of the seq. See also, FIRST')
    parser.add_argument('-i', '--interval', help='interval: h1, d1, w1. default value is d1')
    parser.add_argument('-f', '--format', help='see also, datetime.strftime')

    args = parser.parse_args()

    try:
      first = parse(args.FIRST)
      last = parse(args.LAST)
    except:
      print("invalid datetime format")
      sys.exit(1)

    fmt = DTS_DEFAULT_FORMAT
    if args.format:
      fmt = args.format

    unit = DTS_DEFAULT_UNIT
    how_long = DTS_DEFAULT_INTERVAL

    if args.interval and len(args.interval) >= 2 and args.interval[0] in DT_UNIT:
      unit = args.interval[0]
      how_long = int(args.interval[1:])

    hseq = seqGen(first, last, unit, how_long, fmt)

    for d in hseq:
      print(d)

if __name__ == "__main__":
    main()