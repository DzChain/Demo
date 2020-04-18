from tkinter import *
import suijishu
import duquguaci

class App():
    def __init__(self, root,key):
        self.key = key
        guaming = ""
        guaci = ""
        frame = Frame(root)
        root.title("周易学习")
        Label(frame, text="卦名").grid(row=0, sticky=W)
        Label(frame, text="卦辞").grid(row=1, sticky=W)
        text1 = Text(root, width=40, height=1)
        text1.grid(row=0, column=1)
        text1.insert(INSERT, guaming)
        text2 = Text(frame, width=40, height=5)
        text2.grid(row=1, column=1)
        text2.insert(INSERT, guaci)
        Button(root,text="起卦", width=10, command=self.getgua).grid(row=4, columnspan=3, pady=5)
    def getgua(self):
        self.key = suijishu.qigua()
        guaming = duquguaci.getguaming(self.key)
        guaci = duquguaci.getguaci(self.key)

def main():
    root =Tk()
    app = App(root,"111111")
    root.mainloop()
if __name__ == '__main__':
    main()
