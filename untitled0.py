# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 22:06:11 2019

@author: vanbinhd
"""

# -*- coding: utf-8 -*-


# In[] Import
import argparse
import os
import pandas as pd


# In[] Argument
parser=argparse.ArgumentParser(description="input the [-p path]path that would like to list in [-e extension]")
parser.add_argument('-p','--path')
parser.add_argument('-e','--extension')
parser.add_argument('-px','--perfix')
args=parser.parse_args()
print(f'Arguments: {args.__dict__}')
