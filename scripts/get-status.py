#!/usr/bin/env python
import argparse
from src import getPVStatus

if __name__ == "__main__":
    parser = argparse.ArgumentParser("getPVStatus Request")
    parser.add_argument("search", type=str, help="search glob pattern")
    args = parser.parse_args()
    getPVStatus(search=args.search)
