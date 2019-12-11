# -*- coding: utf-8 -*-
# In[]
import argparse
parser=argparse.ArgumentParser(description="input the [-p path]path that would like to list in [-e extension]")
parser.add_argument('-p','--path',default='images')
parser.add_argument('-e','--extension',default='jpg')
parser.add_argument('-o','--output',default='ouput_images_list.csv')
args=parser.parse_args()

print(args.__dict__)

# In[]
import os
temp2=os.listdir(args.path)

temp=[]
# filter *.jpg
for i,v in enumerate(temp2):
    if args.extension in v:
        temp.append(v)
 

# In[]
import pandas as pd
df=pd.DataFrame(temp)
df.to_csv(args.output,header=False,sep=',',index=False,line_terminator='\r\n')

# In[]
for i in temp:
	print(i)

