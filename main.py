from tkinter import *
import ctypes,os,shutil
import pickle
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
import tkinter.scrolledtext as tkscrolled
home = Tk()
img = Image.open("images/home.png")
img = ImageTk.PhotoImage(img)
panel = Label(home, image=img)
panel.pack(side="top", fill="both", expand="yes")
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-610)
b= str(lt[1]//2-383)
def Exit():
    global home
    result = tkMessageBox.askquestion(
        'FAKE NEWS DETECTION', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        home.destroy()
        exit()
    else:
        tkMessageBox.showinfo(
            'Return', 'You will now return to the main screen')

def pred():
    global txt
    var = txt.get("1.0",END)
    #function to run for prediction
    def detecting_fake_news(var):    
    #retrieving the best model for prediction call
        load_model = pickle.load(open('final_model.sav', 'rb'))
        prediction = load_model.predict([var])
        prob = load_model.predict_proba([var])
        out = "The given statement is "+str(prediction[0])+'\n'+"The truth probability score is "+str(prob[0][1])
        tkMessageBox.showinfo('FAKE NEWS DETECTION', out)
    detecting_fake_news(var)
    
home.title("FAKE NEWS DETECTION")
home.geometry("900x566+"+a+"+"+b)
home.resizable(0,0)
photo = Image.open("images/3.png")
img2 = ImageTk.PhotoImage(photo)
b1=Button(home, highlightthickness = 0, bd = 0,activebackground="white", image = img2,command=Exit)
b1.place(x=634,y=420)
photo = Image.open("images/2.png")
img8 = ImageTk.PhotoImage(photo)
b6=Button(home, highlightthickness = 0, bd = 0,activebackground="white", image = img8,command=pred)
b6.place(x=634,y=360)

txt = tkscrolled.ScrolledText(home, width=17,font=('',14), height=10, wrap='word',bd=2,relief='solid')
txt.place(x=634,y=100)
home.mainloop()
