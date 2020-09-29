import tkinter
from tkinter.ttk import *
from tkinter import filedialog
import pandas as pd
import numpy as np


def clicked_1():
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv(import_file_path)
    L1.configure(text='Data Operational parameters Uploaded!', width=50,height=1)
#     L1.configure(text='Address is '+ import_file_path, 
#                  width=50,height=1,font=('Arial Bold', 8))



def clicked_2():
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv(import_file_path)
    L2.configure(text='Data bit details Uploaded!', width=50,height=1)


def clicked_3():
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv(import_file_path)
    L3.configure(text='Data Temperature properties Uploaded!', width=50,height=1)


def clicked_4():
    L4.configure(text='The Simulator is Running...!', width=50,height=1)

def clicked_5():
    L5.configure(text='Real-time UCS was calculated.!', width=50,height=1)

def clicked_6():
    L6.configure(text='Optimum Realtime Analysis done!', width=50,height=1)













