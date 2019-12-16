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


def get_list_perfix(path, extension, perfix):
    temp_perfix=""
    for i in perfix:
        temp_perfix=os.path.join(temp_perfix,i)
    
    temp2=os.listdir(path)
    temp=[]
    for i,v in enumerate(temp2):
        if extension in v:
            temp.append(os.path.join(temp_perfix,v))
            
    return temp


# In[] Argument
parser=argparse.ArgumentParser(description="input the [-p path]path that would like to list in [-e extension]")
parser.add_argument('-p','--path',default='images')
parser.add_argument('-e','--extension',default='jpg')
parser.add_argument('-o','--output',default='ouput_images_list.csv')
parser.add_argument('-px','--perfix',default=['itn2','images'])
args=parser.parse_args()
print(f'Arguments: {args.__dict__}')


# In[] 
temp=get_list(args.path,args.extension)
df=pd.DataFrame(temp)
df.to_csv(args.output,header=False,sep=',',index=False,line_terminator='\n')
for i in temp:
	print(i)


# In[]
temp2=get_list_perfix(args.path,args.extension,args.perfix)
df2=pd.DataFrame(temp2)
df2.to_csv(f'perfix_{args.output}',header=False,sep=',',index=False,line_terminator='\n')
for i in temp2:
	print(i)