from tkinter import * # this line means that we are importing all the classes and methods present in tkinter module
import random
from ttkthemes import *
from tkinter import ttk

#GUI Part
root=ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('940x735+200+0')
root.resizable(0,0)

titleFrame=Frame(root,bg='orange',bd=4)
titleFrame.grid()

titleLabel=Label(titleFrame,text='Master Typing',font=('algerian',28,'bold'),bg='goldenrod3',fg='white',
                 width=38,bd=10)
titleLabel.grid()

paragraphFrame=Frame(root)
paragraphFrame.grid(row=1,column=0)

paragraph_list=[' I failed the first quarter of a class in middle school, so I made a fake report card. I did this every quarter that year. I forgot that they mail home the end-of-year cards, and my mom got it before I could intercept with my fake. She was PISSED—at the school for their error. The teacher also retired that year and had already thrown out his records, so they had to take my mother’s “proof” (the fake ones I made throughout the year) and “correct” the “mistake.” ',

                    ' In my junior year of high school, this guy asked me on a date. He rented a Redbox movie and made a pizza. We were watching the movie and the oven beeped so the pizza was done. He looked me dead in the eye and said, “This is the worst part.” I then watched this boy open the oven and pull the pizza out with his bare hands, rack and all, screaming at the top of his lungs. We never had a second date.Ok so then what is i cannot tell you because that didnt happen.',

                    'I went to this girl’s party the week after she beat the shit out of my friend. While everyone was getting trashed, I went around putting tuna inside all the curtain rods and so like weeks went by and they couldn’t figure out why the house smelled like festering death. They caught me through this video where these guys at the party were singing Beyonce while I was in the background with a can of tuna.This is what happened in this short funny story if you like.',

                    'One time way back in sixth grade math class I had to fart really bad. Me being the idiot that I am decided that it would be silent. Big surprise it wasn’t. The only person talking was the teacher and she was interrupted by freaking cannon fire farts. She said she was disappointed I couldn’t hold it in and proceeded to tell a story of how she taught a famous athlete who did nearly the same thing.I felt ashamed then everyone laughed and at the end I also laughed.',

                    'So a couple weeks ago, me and my friends were sitting on this cement kind of pedestal (as we called it) It’s basically the steps up to the portable. (classroom that no one uses) and this weird supply French teacher comes up to us and says: you shouldn’t be sitting on this ground, it’s too cold and it’s bad for your ovaries. I asked her how or why and she said that if children sit on cold ground their ovaries will freeze and that we won’t be able to have kids.',

                    'One of the most valuable possession of human life is its health. With good health, one can attain everything in life. In order to perform an important work effectively, one has to be in sound health. Nowadays, everyone is suffering from some sort of mental, health, chronic or physical illness, which however deprives them. Often bad habits such as smoking have brought upon diseases and weakness upon a person which he is not aware of and are of no value to their family and society.',

                    'Alcohol is taken in almost all cool and cold climates, and to a very much less extent in hot ones. It is taken by people who live in the Himalaya Mountains, but not nearly so much by those who live in the plains of India. Alcohol is not necessary in any way to anybody. The regular use of alcohol, even in small quantities, tends to cause mischief in many ways to various organs of the body. It affects the liver, it weakens the mental powers, and lessens the energy of the body.',

                    'The Computer is an automatic device that performs mathematical calculations and logical operations. They are being put to use in widely divergent fields such as book-keeping, spaceflight controls, passanger reservation service, language translation etc. There are two categories: analog and digital. The former represents numbers by some physical quantity such as length, angular relation or electric current whereas the latter represent numbers by seperate devices for each digit.'
]
random.shuffle(paragraph_list)
paragraphLabel=Label(paragraphFrame,text=paragraph_list[0],wraplength=912,justify='left',
                     font=('arial',14,'bold'))
paragraphLabel.grid()

textareaFrame=Frame(root)
textareaFrame.grid(row=2,column=0)
textarea=Text(textareaFrame,font=('arial',12,'bold'),width=100,height=7,wrap='word',bd=4,relief=GROOVE,
              state=DISABLED)
textarea.grid()

outputFrame=Frame(root)
outputFrame.grid(row=3,column=0)

elapsed_time_label=Label(outputFrame,text='Elapsed Time',fg='red',font=('Tahoma',12,'bold'))
elapsed_time_label.grid(row=0,column=0,padx=5)

elapsed_timer_label=Label(outputFrame,text='0',font=('Tahoma',12,'bold'))
elapsed_timer_label.grid(row=0,column=1,padx=5)

remaining_time_label=Label(outputFrame,text='Remaining Time',fg='red',font=('Tahoma',12,'bold'))
remaining_time_label.grid(row=0,column=2,padx=5)

remaining_timer_label=Label(outputFrame,text='60 sec',font=('Tahoma',12,'bold'))
remaining_timer_label.grid(row=0,column=3,padx=5)

wpm_label=Label(outputFrame,text='WPM',fg='red',font=('Tahoma',12,'bold'))
wpm_label.grid(row=0,column=4,padx=5)

wpm_count_label=Label(outputFrame,text='0',font=('Tahoma',12,'bold'))
wpm_count_label.grid(row=0,column=5,padx=5)

accuracy_label=Label(outputFrame,text='Accuracy',fg='red',font=('Tahoma',12,'bold'))
accuracy_label.grid(row=0,column=6,padx=5)

accuracy_percent_label=Label(outputFrame,text='0%',font=('Tahoma',12,'bold'))
accuracy_percent_label.grid(row=0,column=7,padx=5)

totalwords_label=Label(outputFrame,text='Total Words',fg='red',font=('Tahoma',12,'bold'))
totalwords_label.grid(row=0,column=8,padx=5)

totalwords_count_label=Label(outputFrame,text='0',font=('Tahoma',12,'bold'))
totalwords_count_label.grid(row=0,column=9,padx=5)

wrongwords_label=Label(outputFrame,text='Wrong Words',fg='red',font=('Tahoma',12,'bold'))
wrongwords_label.grid(row=0,column=10,padx=5)

wrongwords_count_label=Label(outputFrame,text='0',font=('Tahoma',12,'bold'))
wrongwords_count_label.grid(row=0,column=11,padx=5)

buttonFrame=Frame(root)
buttonFrame.grid(row=4,column=0)

startButton=ttk.Button(buttonFrame,text='Start')
startButton.grid(row=0,column=0,padx=10)

resetButton=ttk.Button(buttonFrame,text='Reset',state=DISABLED)
resetButton.grid(row=0,column=1,padx=10)

exitButton=ttk.Button(buttonFrame,text='Exit')
exitButton.grid(row=0,column=2,padx=10)

keyboardFrame=Frame(root)
keyboardFrame.grid(row=5,column=0)

frame1to0=Frame(keyboardFrame)
frame1to0.grid(row=0,column=0)

label1=Label(frame1to0,text='1',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label1.grid(row=0,column=0)

label2=Label(frame1to0,text='2',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label2.grid(row=0,column=1)

label3=Label(frame1to0,text='3',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label3.grid(row=0,column=2)

label4=Label(frame1to0,text='4',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label4.grid(row=0,column=3)

label5=Label(frame1to0,text='5',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label5.grid(row=0,column=4)

label5=Label(frame1to0,text='5',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label5.grid(row=0,column=4)

label6=Label(frame1to0,text='6',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label6.grid(row=0,column=5)

label7=Label(frame1to0,text='7',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label7.grid(row=0,column=6)

label8=Label(frame1to0,text='8',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label8.grid(row=0,column=7)

label9=Label(frame1to0,text='9',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label9.grid(row=0,column=8)

label0=Label(frame1to0,text='0',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
label0.grid(row=0,column=9)

frameqtop=Frame(keyboardFrame)
frameqtop.grid(row=1,column=0)

labelq=Label(frameqtop,text='Q',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
labelq.grid(row=0,column=0)

labelw=Label(frameqtop,text='W',bg='black',fg='white',bd=10,width=5,height=2,
             font=('arial',10,'bold'),relief=GROOVE)
labelw.grid(row=0,column=1)



root.mainloop()