#coding:utf-8
import os
import codecs
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

directory = os.listdir("./tech")

for file in directory:
    f = codecs.open("./tech/{}".format(file),'r', 'utf-8', errors='ignore')
    



