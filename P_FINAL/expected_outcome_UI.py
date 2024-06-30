import pandas as pd
from tkinter import *
from tkinter import ttk
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import random
from PIL import ImageTk, Image  

root = Tk()
root.title("Welcome")
img =Image.open('BC.png')
bg = ImageTk.PhotoImage(img)

##root.geometry("550x450")

# Add image
label = Label(root, image=bg)
label.place(x = 0,y = 0)

root.geometry("1350x850")

# Add image
label = Label(root, image=bg)
label.place(x = 0,y = 0)

label_1 = ttk.Label(root, text ='Input labels',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 100,y = 100)

label_1 = ttk.Label(root, text ='input value getting labels',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 300,y = 100)

label_1 = ttk.Label(root, text ='Attribute 1',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 100,y = 200)
    
Entry_1= Entry(root)
Entry_1.place(x = 300,y = 200)

label_1 = ttk.Label(root, text ='Attribute 2',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 100,y = 300)
    
Entry_1= Entry(root)
Entry_1.place(x = 300,y = 300)

label_1 = ttk.Label(root, text ='Attribute n',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 100,y = 400)
    
Entry_1= Entry(root)
Entry_1.place(x = 300,y = 400)

label_1 = ttk.Label(root, text ='types of classification prediciton ',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 100)
label_1 = ttk.Label(root, text ='Normal ',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 150)
label_1 = ttk.Label(root, text ='Old Anterior Myocardial Infarction',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 200)
label_1 = ttk.Label(root, text ='Old Inferior Myocardial Infarction',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 250)
label_1 = ttk.Label(root, text ='Sinus tachycardia',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 300)
label_1 = ttk.Label(root, text ='Ventricular Premature Contraction (PVC)',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 350)
label_1 = ttk.Label(root, text ='Supraventricular Premature Contraction',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 400)
label_1 = ttk.Label(root, text ='Left bundle branch block',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 450)
label_1 = ttk.Label(root, text ='Right bundle branch block',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 500)
label_1 = ttk.Label(root, text ='Left ventricle hypertrophy',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 550)
label_1 = ttk.Label(root, text ='Atrial Fibrillation or Flutter',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 600)
label_1 = ttk.Label(root, text ='Others type of arrhythmia 1',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 650)
label_1 = ttk.Label(root, text ='other type of arrhytmia 2 and 3',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 500,y = 700)



b1 = Button(root, text = 'predict',font=("Helvetica", 16),background="#14161a",command = predict,foreground="#ffffff")
b1.place(x = 80,y = 500)
    
output = Entry(root,font=("Helvetica", 16,"bold"))
output.place(x = 280,y = 500)
root.mainloop()
