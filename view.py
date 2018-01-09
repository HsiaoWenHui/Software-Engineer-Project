# -*- coding: utf-8 -*-

import tkinter
import ttk
from distutils.dist import command_re
from tkinter.constants import ANCHOR
from PIL.ImageTk import PhotoImage
from django.utils.termcolors import background
import controller
from doctest import master
import numpy as np
    
class Application(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.master.minsize(width=352, height=660)
        
        self.state=""
        self.bg=PhotoImage(file='./back.jpeg')
        self.playImage=PhotoImage(file='./play.png')
        self.setImage=PhotoImage(file='./settings.png')
        self.setImage2=PhotoImage(file='./settings2.png')
        self.logoImage=PhotoImage(file='./logo.png')
        self.pauseImage=PhotoImage(file='./pause.png')
        self.cancelImage=PhotoImage(file='./cancel.png')
        self.restartImage=PhotoImage(file='./restart.png')
        self.master.config()
        
        self.inputText = tkinter.Label(master,image=self.logoImage,text="tetris")
        self.score=tkinter.Label(master,font=('Arial,80'),width=15,height=2,text="score")
        self.playButton=tkinter.Button(master,image=self.playImage,text='PLAY',width=150,height=80,command=self.play)
    
        self.settingButton=tkinter.Button(master,image=self.setImage,text='SET',width=150,height=80,command=self.set)
        self.pauseButton=tkinter.Button(master,image=self.pauseImage,text='PAUSE',width=30,height=30,command=self.pause)
        self.restartButton=tkinter.Button(master,image=self.restartImage,text='RESTART',width=100,height=60,command=self.restart)
        self.cancelButton=tkinter.Button(master,image=self.cancelImage,text='CANCEL',width=60,height=60,command=self.cancel)
        self.canvas=tkinter.Canvas(borderwidth=2,width=330,height=610)
        self.panel=tkinter.StringVar()
        self.panel1=tkinter.Radiobutton(text='1',variable=self.panel,value='1',command=self.panelchange)
        self.panel2=tkinter.Radiobutton(text='2',variable=self.panel,value='2',command=self.panelchange)
        self.panel3=tkinter.Radiobutton(text='3',variable=self.panel,value='3',command=self.panelchange)
        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)
        self.startFrame()

    def changeView(self,state):
            self.state=state
            if state=="IDLE":
                self.clear()
                self.startFrame()
            
            elif(state=="PLAY"):
                self.clear()
                self.playFrame()
                
            elif(state=='SET'):
                self.clear()
                self.setFrame()
                
            elif(state=='PAUSE'):
                self.clear()
                self.pauseFrame()
                
            elif(state=='OVER'):
                self.overFrame()
                
            else:
                self.startFrame()
                
    def startFrame(self):
        
        
        self.playButton.place(x=176,y=300,anchor='center')
        self.settingButton.place(x=176,y=400,anchor='center')
        self.inputText.place(x=176,y=100,anchor='n')
    
    def playFrame(self):
        
        
        self.canvas.pack(side='bottom')
        self.score.place(x=0,y=0,anchor='nw')
        self.pauseButton.place(x=176,y=5,anchor='n')
        outside=self.canvas.create_rectangle(10,5,330,605)#每格40
        
        board= np.zeros([15,8])
      
        board[1][3]=1
        board[0][3]=1
        board[0][0]=1
        board[0][1]=1
        board[0][2]=1
        board[0][4]=1
        board[0][5]=1
        board[0][6]=1
        board[0][7]=1
        for i in range(0,15):
            board[i][0]=1
        for i in range(0,15):
            for j in range(0,8):
                if board[i][j]==1:
                    square=self.canvas.create_rectangle(j*40+10,i*40+5,j*40+50,i*40+45,fill="red")
                else:
                    continue
    
    def pauseFrame(self):
        
        self.restartButton.place(x=176,y=200,anchor='center')
        self.cancelButton.place(x=106,y=280,anchor='w')
        self.settingButton.config(image=self.setImage2,width=60,height=60)
        self.settingButton.place(x=176,y=280,anchor='w')
    
        
    def setFrame(self):
        
        self.panel1.place(x=126,y=200,anchor='center')
        self.panel2.place(x=176,y=200,anchor='center')
        self.panel3.place(x=226,y=200,anchor='center')
        self.cancelButton.place(x=176,y=250,anchor='center')
    def overFrame(self):
        
        self.inputText.config(text="over")   
        
    def clear(self):
        self.canvas.pack_forget()
        self.inputText.place_forget()
        self.playButton.place_forget()
        self.score.place_forget()
        self.settingButton.place_forget()
        self.pauseButton.place_forget()
        self.restartButton.place_forget()
        self.cancelButton.place_forget()
        self.panel1.place_forget()
        self.panel2.place_forget()
        self.panel3.place_forget()
        
    def play(self):
        control.play() 
    def set(self):
        control.setting()
    def pause(self):
        control.pause()
        
               
    def panelchange(self):
        print (self.view.get()+" button pressed")
        
    def cancel(self):
        if(self.state=="SET"):
            control.start()
        elif(self.state=="PAUSE"):
            control.play()

    def restart(self):
        control.start()

    def left_key(self,event):
        control.gameinput("LEFT")
        
    def right_key(self,event):
        control.gameinput("RIGHT")
    
    def up_key(self,event):
        control.gameinput("UP")
        
    def down_key(self,event):
        control.gameinput("DOWN")
        

root = tkinter.Tk()
app = Application(root)
control=controller.Control(app)
app.mainloop()