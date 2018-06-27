#coding:utf-8
import os
import codecs
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

f = codecs.open("./newssets.txt",'r', 'utf-8', errors='ignore')

texts = f.read()
#__label__ でList作る
doc = texts.split("\n")
#リストをシャッフル
import random
random.shuffle(doc)
#Textに戻す
random_sent = doc

corpus = "\n".join(random_sent)

with open("newsTexts", "w", encoding='utf-8') as text_file:
    text_file.write(corpus)