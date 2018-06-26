#coding:utf-8
import os
import codecs
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

directory = os.listdir("./tech")
array = []

for file in directory:
    f = codecs.open("./tech/{}".format(file),'r', 'utf-8', errors='ignore')
    lines = f.read()
    test = lines.split("\n")
    non_spaceList = [w for w in test if not w in '']
    #Add "." to the title.
    non_spaceList.pop(0)
    nonSpaceString = " ".join(non_spaceList)
    array.append(nonSpaceString)