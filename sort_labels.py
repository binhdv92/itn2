# -*- coding: utf-8 -*-
import pandas as pd

import numpy as np


#with open("C:\\itn2\images2\\500237051_(1).txt",mode="r") as f:
#    data = f.readcsv
#
nametable=["images2/500237051_(1).txt",
           "images2/500237051_(2).txt"
           "images2/500237051_(3).txt"
           "images2/500237051_(4).txt"
           "images2/500237051_(5).txt"
           "images2/500237051_(6).txt"]
           
tempname="images2/500237051_(1).txt"

for tempname in nametable:
    print(tempname)
    data = pd.read_csv(tempname,delimiter=' ',encoding='utf-8',header=None,prefix='var')
    data.sort_values(by=['var2','var1'],inplace=True)
    data.to_csv(tempname,sep=' ',index=False,header=False)