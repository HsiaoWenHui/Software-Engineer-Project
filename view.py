# -*- coding: utf-8 -*-

import tkinter
from distutils.dist import command_re
from tkinter.constants import ANCHOR
from PIL.ImageTk import PhotoImage
from django.utils.termcolors import background



    
class Application(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.master.minsize(width=500, height=500)
        self.master.config()
        
        
        self.playImage=PhotoImage(file='./play.png')
        self.setImage=PhotoImage(file='./settings.png')
        self.setImage2=PhotoImage(file='./settings2.png')
        self.logoImage=PhotoImage(file='./logo.png')
        self.pauseImage=PhotoImage(file='./pause.png')
        self.cancelImage=PhotoImage(file='./cancel.png')
        self.restartImage=PhotoImage(file='./restart.png')
        self.comfirmImage=PhotoImage(file='./comfirm.png')
        
        self.inputText = tkinter.Label(image=self.logoImage,text="tetris")
        self.score=tkinter.Label(font=('Arial,80'),width=15,height=2,text="score")
        self.playButton=tkinter.Button(image=self.playImage,text='PLAY',width=150,height=80,command=self.play)
        self.settingButton=tkinter.Button(image=self.setImage,text='SET',width=150,height=80,command=self.set)
        self.pauseButton=tkinter.Button(image=self.pauseImage,text='PAUSE',width=40,height=40,command=self.pause)
        self.restartButton=tkinter.Button(image=self.restartImage,text='RESTART',width=100,height=60,command=self.restart)
        self.overButton=tkinter.Button(text='OVER',width=15,height=2,command=self.over)
        self.comfirmButton=tkinter.Button(image=self.comfirmImage,text='COMFIRM',width=15,height=40,command=self.comfirm)
        self.cancelButton=tkinter.Button(image=self.cancelImage,text='CANCEL',width=60,height=60,command=self.cancel)
        
        self.vol=tkinter.StringVar()
        self.volLarge=tkinter.Radiobutton(text='Large',variable=self.vol,value='large',command=self.voltune)
        self.volMid=tkinter.Radiobutton(text='Mid',variable=self.vol,value='mid',command=self.voltune)
        self.volLow=tkinter.Radiobutton(text='Low',variable=self.vol,value='low',command=self.voltune)
        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)
        self.setFrame()

    def changeView(self,state):
            if(state=='IDLE'):{
                self.startFrame()
                }
            elif(state=='PLAY'):{
                self.playFrame()
                }
            elif(state=='SET'):{
                self.setFrame()
                }
            elif(state=='PAUSE'):{
                self.pauseFrame()
                }
            else:{
                self.startFrame()
                }
    def startFrame(self):
        startFrame=tkinter.Frame(self)
        startFrame.place()
        self.playButton.place(x=250,y=200,anchor='center')
        self.settingButton.place(x=250,y=300,anchor='center')
        self.inputText.place(x=250,y=50,anchor='n')
    def playFrame(self):
        playFrame=tkinter.Frame(self)
        playFrame.place()
        self.score.place(x=0,y=0,anchor='nw')
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
        
        
        
        
    def voltune(self):
        print (self.vol.get()+" button pressed")
        
    def cancel(self):
        self.inputText.config(text="cancel")
        print ( " cancel button pressed") 
    def comfirm(self):
        self.inputText.config(text="restart")
        print ( " comfirm button pressed")     
    def over(self):
        self.inputText.config(text="over")
        print ( " over button pressed")  
    def pause(self):
        self.inputText.config(text="pause")
        print ( " pause button pressed")
    def restart(self):
        self.inputText.config(text="restart")
        print ( " restart button pressed")
    def set(self):
        self.inputText.config(text="set")
        print ( " set button pressed")
    def play(self):
        self.inputText.config(text="play")
        print ( " play button pressed")
    def left_key(self,event):
        self.inputText.config(text="left")
        print ( " left key pressed")
    
    def right_key(self,event):
        self.inputText.config(text="right")
        print (" right key pressed")
    
    def up_key(self,event):
        self.inputText.config(text="up")
        print (" up key pressed")
   
    def down_key(self,event):
        self.inputText.config(text="down")
        print (" down key pressed")
root = tkinter.Tk()
app = Application(root)
app.mainloop()