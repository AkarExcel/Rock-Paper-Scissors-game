
#import Useful library
from tkinter import *
import random

#initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Akar Excel-Rock,Paper,Scissors')
root.config(bg ='seashell3')


#heading
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'seashell2').pack()


##user choice
user_take = StringVar()
Label(root, text = 'choose any one: rock, paper ,scissors' , font='arial 15 bold', bg = 'seashell2').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=90 , y = 130)



#computer choice
def comp():
    comp_pick = random.randint(1,3)
    if comp_pick == 1:
        comp_pick = 'rock'
    elif comp_pick ==2:
        comp_pick = 'paper'
    else:
        comp_pick = 'scissors'
    return comp_pick
    



##function to play
Result = StringVar()

def play():
    user_pick = user_take.get()
    comp_pick = comp()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you lose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set(' Congratulation you won,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you lose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set(' Congratulation you won,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you lose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set(' Congratulation you won ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
    
        
    
##run to reset
def Reset():
    Result.set("") 
    user_take.set("")
    

##run to exit
def Exit():
    root.destroy()


###### button
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='gray' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='gray' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='gray' ,command = Exit).place(x=250,y=310)

root.mainloop()
