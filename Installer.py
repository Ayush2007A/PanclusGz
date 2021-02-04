import  pip
import tkinter
from PIL import Image, ImageTk
from tkinter import *
def install():
    installer()
root = tkinter.Tk()
root.geometry('200x50')
root.title('Gz')
e1 = Entry(root,  width = 30)
e1.pack()
b1 = Button(root,text='install', command = install).pack()

def installer():
    print(e1.get())
    x=e1.get()
    pip.main(['install', x])
