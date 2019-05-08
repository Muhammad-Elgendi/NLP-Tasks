import os
import re
from nltk.tag import stanford as STag
from tkinter import *
os.environ['STANFORD_PARSER'] = '/media/muhammad/disk/FCI/year 4/Second term/NLP/2019/stanford-postagger-full-2018-10-16'
os.environ['STANFORD_MODELS'] = '/media/muhammad/disk/FCI/year 4/Second term/NLP/2019/stanford-postagger-full-2018-10-16/models/'
tagger = STag.StanfordPOSTagger('arabic.tagger', '/media/muhammad/disk/FCI/year 4/Second term/NLP/2019/stanford-postagger-full-2018-10-16/stanford-postagger.jar')


def tokenizeArabic(text):
    return re.split(r'[-,،!\s\_]+',text)

def show_outputs():
    tokens = tokenizeArabic(e1.get())   
    lbl["text"] = str(tagger.tag(tokens))

master = Tk()
# master.geometry("500x600")
master.title('POS Tagging')
Label(master, text="Enter your text : ",font=("Arial", 16), anchor="e").grid(row=0)
Label(master, text="POS Tagging output :",font=("Arial", 16), anchor="e").grid(row=1)

e1 = Entry(master)

lbl = Label(master, text = '')
# lbl.config(height=15, width=30)

e1.grid(row=0, column=1,pady=10)
lbl.grid(row=1, column=1,pady=10)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='POS Tagging', command=show_outputs).grid(row=3, column=1, sticky=W, pady=4)

mainloop()

os.environ['STANFORD_PARSER'] = '/media/muhammad/disk/FCI/year 4/Second term/NLP/2019/stanford-postagger-full-2018-10-16'
os.environ['STANFORD_MODELS'] = '/media/muhammad/disk/FCI/year 4/Second term/NLP/2019/stanford-postagger-full-2018-10-16/models/'
tagger = STag.StanfordPOSTagger('arabic.tagger', '/media/muhammad/disk/FCI/year 4/Second term/NLP/2019/stanford-postagger-full-2018-10-16/stanford-postagger.jar')
# for tag in tagger.tag(tokenizeArabic("الله يثيب من العاملين من إجتهد وسعي وغالب هواه")):
# 	print(tag[1])

