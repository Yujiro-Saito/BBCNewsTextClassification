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
    fixedLines = lines.split("\n")
    non_spaceList = [w for w in fixedLines if not w in '']
    #Add "." to the title.
    non_spaceList.pop(0)
    nonSpaceString = " ".join(non_spaceList)
    labelStr = "__label__tech "
    processedSent = labelStr + nonSpaceString
    array.append(processedSent)

correctString = "\n".join(array)

with open("demo.txt", "w", encoding='utf-8') as text_file:
    text_file.write(correctString)

