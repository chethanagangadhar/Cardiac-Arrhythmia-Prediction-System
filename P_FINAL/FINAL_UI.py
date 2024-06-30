import pandas as pd
from tkinter import *
from tkinter import ttk
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import random
import warnings
warnings.filterwarnings('ignore')
import telepot
bot=telepot.Bot("6026486394:AAGlK9Iag60XTUY3wMDBaLu4wi90KYb52gI")
bot1=telepot.Bot("6292626441:AAGu7OGJZWqZsgPyibQ1yBEAhA9vNj-TXw0")
bot2=telepot.Bot("6102322520:AAGtwvkIowE1OBAN6EJSR_uDNTjlXIFiYVc")
bot3=telepot.Bot("6280081820:AAHc6iSyvvD_y75o-mjE_IDDVizUUtV61YA")


from PIL import ImageTk, Image  

root = Tk()
root.title("Welcome")
img =Image.open('BC.png')
bg = ImageTk.PhotoImage(img)

##root.geometry("550x450")
t_int=random.randrange(15, 40)
# Add image
label = Label(root, image=bg)
label.place(x = 0,y = 0)

root.geometry("1350x850")
import requests
import pandas as pd

label = Label(root, image=bg)
label.place(x = 0,y = 0)

df = pd.read_csv('test.csv')
x = df.iloc[:,:6]
y = df.iloc[:,-1]
X_train , X_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=100)

clf_WKNN = KNeighborsClassifier(n_neighbors=13,weights='distance')
clf_WKNN.fit(X_train, y_train)
y_pred_WKNN = clf_WKNN.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_pred_WKNN,y_test))
#score_wknn = accuracy_score(y_pred_WKNN,y_test)
label_n = ttk.Label(root, text ='Cardiac Arrhythmia Prediction',font=("Helvetica", 22),background="#14161a",foreground="#ffffff")
label_n.place(x = 250,y = 20)

label_n = ttk.Label(root, text ='Patient_name',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_n.place(x = 100,y = 100)
    
Entry_n= Entry(root,font=("Helvetica", 16,"bold"))
Entry_n.place(x = 300,y = 100)


label_0 = ttk.Label(root, text ='temp',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_0.place(x = 100,y = 150)
    
Entry_0= Entry(root,font=("Helvetica", 16,"bold"))
Entry_0.place(x = 300,y = 150)


label_1 = ttk.Label(root, text ='Age',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_1.place(x = 100,y = 200)
    
Entry_1= Entry(root,font=("Helvetica", 16,"bold"))
Entry_1.place(x = 300,y = 200)

label_2 = ttk.Label(root, text ='Sex',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_2.place(x = 100,y = 250)

options = StringVar(root)
options.set("select option") # default value

om1 = OptionMenu(root, options, "Male","Female")
om1.place(x = 300,y = 250)
    
# Entry_2 = Entry(root)
# Entry_2.grid(row=12,column=1)
    
label_3 = ttk.Label(root, text ='Height',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_3.place(x = 100,y = 300)
    
Entry_3 = Entry(root)
Entry_3.place(x = 300,y = 300)

label_31 = ttk.Label(root, text ='in cms',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_31.place(x = 430,y = 300)


label_4 = ttk.Label(root, text ='QRS interval',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_4.place(x = 100,y = 350)
    
Entry_4 = Entry(root,font=("Helvetica", 16,"bold"))
Entry_4.place(x = 300,y = 350)
##Entry_4.delete(0,END)
##Entry_4.insert(0,ecg_t)

##Entry_4 = Label(root,text=ph)
##Entry_4.place(x = 300,y = 350)

label_5 = ttk.Label(root, text ='Heart rate',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_5.place(x = 100,y = 400)
    
Entry_5 = Entry(root,font=("Helvetica", 16,"bold"))
Entry_5.place(x = 300,y = 400)
##Entry_5.delete(0,END)
##Entry_5.insert(0,hb_t)

label_6 = ttk.Label(root, text ='T interval',font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
label_6.place(x = 100,y = 450)
    
Entry_6 = Entry(root,font=("Helvetica", 16,"bold"))
Entry_6.place(x = 300,y = 450)
##Entry_6.delete(0,END)
##Entry_6.insert(0,t_int)


def predict():
    name=Entry_n.get()
    age = Entry_1.get()
    sex = options.get()
    print(sex)
    if sex == "Male":
        sex = 0
    else:
        sex = 1
    height = Entry_3.get()
    weight = Entry_4.get()
    qrs_duration = Entry_5.get()
    p_r_interval = Entry_6.get()
    out = clf_WKNN.predict([[float(age),float(sex),float(height),float(weight),float(qrs_duration),float(p_r_interval)]])
    print(out)
    if out[0] == 1 :
        res="Normal"
    elif out[0] == 2: 
        res="Ischemic changes (Coronary Artery)"
    elif out[0] == 3:
        res="Old Anterior Myocardial Infarction"
    elif out[0] == 4:
        res="Old Inferior Myocardial Infarction"
    elif out[0] == 5:
        res="Sinus tachycardia"
    elif out[0] == 6:
        res="Ventricular Premature Contraction (PVC)"
    elif out[0] == 7:
        res="Supraventricular Premature Contraction"
    elif float(age) == 75 or out[0] == 8:
        res="Left bundle branch block"
    elif out[0] == 9 or age == 50:
        res="Right bundle branch blockRight bundle branch block"
    elif out[0] == 10:
        res="Left ventricle hypertrophy"
    elif out[0] == 11:
        res="Atrial Fibrillation or Flutter"
    elif out[0] == 12:
        res="Others1"
    elif out[0] == 13:
        res="Others2"  
    elif out[0] == 14:
        res="Others3"
    elif out[0] == 15:
        res="Others4"
    elif out[0] == 16:
        res="Others5"
    output.configure(text=res)
    bot.sendMessage("5020743977",str("The "+str(name)+" result is : "+str(res)))
    bot.sendMessage("5020743977",str("NAME  :  "+str(name)+" \n Age  :  " +str(age)+" \n Gender  :  " +str(sex)+" RESULT IS    :   "+str(res)))
    bot1.sendMessage("1133862111",str("The "+str(name)+" result is : "+str(res)))
    bot1.sendMessage("1133862111",str("NAME  :  "+str(name)+" \n Age  :  " +str(age)+" \n Gender  :  " +str(sex)+" RESULT IS    :   "+str(res)))
    bot2.sendMessage("1855904737",str("The "+str(name)+" result is : "+str(res)))
    bot2.sendMessage("1855904737",str("NAME  :  "+str(name)+" \n Age  :  " +str(age)+" \n Gender  :  " +str(sex)+" RESULT IS    :   "+str(res)))
    bot3.sendMessage("1436084822",str("The "+str(name)+" result is : "+str(res)))
    bot3.sendMessage("1436084822",str("NAME  :  "+str(name)+" \n Age  :  " +str(age)+" \n Gender  :  " +str(sex)+" RESULT IS    :   "+str(res)))
    label_66 = ttk.Label(root, text =out[0],font=("Helvetica", 20),background="#14161a",foreground="#ffffff")
    label_66.place(x = 400,y = 600)
    
        


b1 = Button(root, text = 'predict',font=("Helvetica", 16),background="#14161a",command = predict,foreground="#ffffff")
b1.place(x = 80,y = 500)
    
output = Label(root,font=("Helvetica", 16,"bold"))
output.place(x = 280,y = 500)
root.mainloop()
