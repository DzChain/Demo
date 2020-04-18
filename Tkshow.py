#  coding = utf-8
#! python3.6
# 2019.12.25

import suijishu
import duquguaci
from tkinter import *
#import tkinter as t

guaming_text = ""
guaci_text = ""
def showgua():
    key = suijishu.qigua()
    global guaming_text
    guaming_text = duquguaci.getguaming(key)
    global  guaci_text
    guaci_text = duquguaci.getguaci(key)
root  = Tk()
root.title("周易学习")
Label(root, text = "卦名").grid(row = 0, sticky = W)
Label(root, text = "卦辞").grid(row = 1, sticky = W)

text1 = Text(root, width = 80, height = 1)
text1.grid(row = 0, column = 1)
text1.insert(INSERT, guaming_text)
text2 = Text(root, width = 80, height = 5)
text2.grid(row = 1, column = 1)
text2.insert(INSERT, guaci_text)

Button(text = "起卦", width = 20, command = showgua()).grid(row = 4, columnspan = 3, pady = 5)
#print(suijishu.qigua())

mainloop()
