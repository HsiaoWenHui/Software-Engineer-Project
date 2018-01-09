# -*- coding: utf-8 -*-

import tkinter
from distutils.dist import command_re
from tkinter.constants import ANCHOR
from PIL.ImageTk import PhotoImage
from django.utils.termcolors import background
import controller
from doctest import master


    
class Application(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.master.minsize(width=500, height=500)
        self.master.config()
        self.state=""
        
        self.playImage=PhotoImage(file='./play.png')
        self.setImage=PhotoImage(file='./settings.png')
        self.setImage2=PhotoImage(file='./settings2.png')
        self.logoImage=PhotoImage(file='./logo.png')
        self.pauseImage=PhotoImage(file='./pause.png')
        self.cancelImage=PhotoImage(file='./cancel.png')
        self.restartImage=PhotoImage(file='./restart.png')
        
        
        self.inputText = tkinter.Label(master,image=self.logoImage,text="tetris")
        self.score=tkinter.Label(master,font=('Arial,80'),width=15,height=2,text="score")
        self.playButton=tkinter.Button(master,image=self.playImage,text='PLAY',width=150,height=80,command=self.play)
        self.settingButton=tkinter.Button(master,image=self.setImage,text='SET',width=150,height=80,command=self.set)
        self.pauseButton=tkinter.Button(master,image=self.pauseImage,text='PAUSE',width=40,height=40,command=self.pause)
        self.restartButton=tkinter.Button(master,image=self.restartImage,text='RESTART',width=100,height=60,command=self.restart)
        
        self.cancelButton=tkinter.Button(master,image=self.cancelImage,text='CANCEL',width=60,height=60,command=self.cancel)
        
        self.vol=tkinter.StringVar()
        self.volLarge=tkinter.Radiobutton(text='Large',variable=self.vol,value='large',command=self.voltune)
        self.volMid=tkinter.Radiobutton(text='Mid',variable=self.vol,value='mid',command=self.voltune)
        self.volLow=tkinter.Radiobutton(text='Low',variable=self.vol,value='low',command=self.voltune)
        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)
        self.startFrame()

    def changeView(self,state):
            self.state=state
            if(state=="IDLE"):{
                self.startFrame()
                }
            elif(state=="PLAY"):{
                self.playFrame()
                }
            elif(state=='SET'):{
                self.setFrame()
                }
            elif(state=='PAUSE'):{
                self.pauseFrame()
                }
            elif(state=='OVER'):{
                self.overFrame()
                }
            else:{
                self.startFrame()
                }
    def startFrame(self):
        
        startFrame=tkinter.Frame(self)
        startFrame.place()
        #self.playButton.config(startFrame)
        
        self.playButton.place(x=250,y=200,anchor='center')
       # self.settingButton.config(startFrame)
        self.settingButton.place(x=250,y=300,anchor='center')
        self.inputText.place(x=250,y=50,anchor='n')
    def playFrame(self):
        self.pack_forget()
        #playFrame=tkinter.Frame(self)
       #playFrame.place()
       # self.score.config(playFrame)
        self.score.place(x=0,y=0,anchor='nw')
       # self.pauseButton.config(playFrame)
        self.pauseButton.place(x=250,y=0,anchor='n')
    
    def pauseFrame(self):
        pauseFrame=tkinter.Frame(self)
        pauseFrame.place()
        
        self.restartButton.place(x=250,y=200,anchor='center')
        self.cancelButton.place(x=180,y=280,anchor='w')
        self.settingButton.config(image=self.setImage2,width=60,height=60)
        self.settingButton.place(x=250,y=280,anchor='w')
    
        
    def setFrame(self):
        self.volLarge.place(x=200,y=200,anchor='center')
        self.volMid.place(x=250,y=200,anchor='center')
        self.volLow.place(x=300,y=200,anchor='center')
    def overFrame(self):
        self.inputText.config(text="over")   
        
        
    def play(self):
        control.play() 
    def set(self):
        control.setting()
    def pause(self):
        control.pause()
        
               
    def voltune(self):
        print (self.vol.get()+" button pressed")
        
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