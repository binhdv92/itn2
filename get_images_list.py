# -*- coding: utf-8 -*-
# In[] Import
import argparse
import os
import pandas as pd


# In[] Def
def get_list(path, extension):
	temp2=os.listdir(path)
	temp=[]
	for i,v in enumerate(temp2):
		if extension in v:
			temp.append(v)
	return temp


# In[]
parser=argparse.ArgumentParser(description="input the [-p path]path that would like to list in [-e extension]")
parser.add_argument('-p','--path',default='images')
parser.add_argument('-e','--extension',default='jpg')
parser.add_argument('-o','--output',default='ouput_images_list.csv')
args=parser.parse_args()
print(args.__dict__)
temp=get_list(args.path,args.extension)


# In[]
df=pd.DataFrame(temp)
df.to_csv(args.output,header=False,sep=',',index=False,line_terminator='\r\n')


# In[]
for i in temp:
	print(i)


