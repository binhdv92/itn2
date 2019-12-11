# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square',help="display a square of a given number",type=int)
args = parser.parse_args()

parser.add_argument

print(args.square**2)
