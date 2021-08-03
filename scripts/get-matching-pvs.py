#!/usr/bin/env python
import argparse
from siriuscommon.archiver import getMatchingPVs

if __name__ == "__main__":
    parser = argparse.ArgumentParser("getMatchingPVs Request")
    parser.add_argument("search", type=str, help="search glob pattern")
    args = parser.parse_args()
    getMatchingPVs(search=args.search)
