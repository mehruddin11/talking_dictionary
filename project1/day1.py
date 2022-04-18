import tkinter
from tkinter import *
from tkinter import messagebox
import json
import pyttsx3

engine = pyttsx3.init()

# functionality part
def exit_window():
    res = messagebox.askyesno('confirm', 'Do you wanna Exit')
    if(res == True):
       # destroy closes window
        root.destroy()

def clear_btn():
    textarea.delete(0.0, END)
    enrtyField.delete(0, END)

# speak
def Speak():
    text = enrtyField.get()
    rate = engine.setProperty('rate', 150)
    engine.say(text, rate)
    engine.runAndWait()
# textarea speak
def textAreaSpeak():
    text = textarea.get(0.0 , END)
    rate = engine.setProperty('rate', 150)
    engine.say(text, rate)
    engine.runAndWait()
def search():
    
    word = enrtyField.get().lower()
    textarea.delete(0.0 , END)
    data = json.load( open('../assets/data.json'))
    if word in data:
        listofMeaning = data[word]
        for  meaning in listofMeaning:
            textarea.insert(END , U'\u2022' +  meaning + '\n\n')
    else:
        word= enrtyField.get().lower()
       
        if(len(word) >= 2):
            arr= list(word)
            arr.pop()
            s= ""
            s =s.join(arr)
            data = json.load( open('../assets/data.json'))
            if s  in  data:
               textarea.insert(END ,  f'did you mean?  {s} ' + '\n\n')
               listofMeaning = data[s]
               for  meaning in listofMeaning:
                   textarea.insert(END , U'\u2022' +  meaning + '\n\n')

            else:
                err = f"Can't Find The Meaning : '{enrtyField.get()}'"
                textarea.insert(END ,  err)

# designing
root = tkinter.Tk()
# title
root.title("Talking Dictonary")
#

# size of window  width and height
root.geometry("1000x656+10+30")
#
# fixing window location
#
# resizing window true or false
root.resizable(False, False)

# assigning  background
bgImage = PhotoImage(file="../assets/bg.png")
bgLable = Label(root, image=bgImage)
bgLable.pack()
# bgLable.place(x=0, y=0)
# bgLable.grid(row=0, column=0)
#

# ading text
wordLabel = Label(root,  text="Enter Word ", font=(
    'sanserif', 25, 'bold'), fg='#222')
wordLabel.place(x=600, y=30)

enrtyField = Entry(root, font=('arial', 16,  'bold'), bd=6, relief=RIDGE)
enrtyField.place(x=560, y=100)

# search buton
# searchButton = Button(root, text = "Search")
# searchButton.place(x= 630, y = 130)

SearchImage = PhotoImage(file='../assets/search.png')
searchButton = Button(root, image=SearchImage, bd=0, cursor='hand2', command=search)
searchButton.place(x=600, y=170)

# mic
MicImage = PhotoImage(file='../assets/mic.png')
MicButton = Button(root, image=MicImage, bd=0, cursor='hand2',  command=Speak)
MicButton.place(x=700, y=170)
 
meaningLable = Label(root,  text="Meaning ", font=(
    'sanserif', 30, 'bold'), fg='#222')

meaningLable.place(x=590, y=250)

# textarea
textarea = Text(root, font=('Arial', 18, 'bold'), width=34,
                height=8, bd=8, relief=GROOVE, wrap='word')
textarea.place(x=460, y=330)

# microphone btn
microphoneImage = PhotoImage(file='../assets/microphone.png')
microphoneButton = Button(root, image=microphoneImage, bd=0, cursor='hand2'  , command=textAreaSpeak)
microphoneButton.place(x=530, y=590)

# claer btn
ClearImage = PhotoImage(file='../assets/clear.png')
clearButton = Button(root, image=ClearImage, bd=0,
                     cursor='hand2', command=clear_btn)
clearButton.place(x=650, y=585)

# exit btn
ExitImage = PhotoImage(file='../assets/exit.png')
exitBuuton = Button(root, image=ExitImage, bd=0,
                    cursor='hand2', command=exit_window)
exitBuuton.place(x=780, y=585)

# main loop
root.mainloop()
#
