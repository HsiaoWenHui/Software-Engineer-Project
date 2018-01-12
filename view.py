# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
#from distutils.dist import command_re
#from tkinter.constants import ANCHOR
from PIL.ImageTk import PhotoImage
import PIL
#from django.utils.termcolors import background
#from doctest import master
import numpy as np
class ParentView(tkinter.Frame):
    def __init__(self, master, model):
        self.mod=model
        tkinter.Frame.__init__(self, master)
        self.master.minsize(width=352, height=660)
        
        self.state=""
        self.gamestate=""
        self.scoreText="0"
        
        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)
        self.board= np.zeros([15,8])

        
    def changeView(self,state):
            self.clear()
            print("change"+self.state)
            self.state=state
            if state=="IDLE":
                
                self.startFrame()
            
            elif(state=="PLAY"):
             
                self.playFrame()
                
            elif(state=='SET'):
            
                self.setFrame()
                
            elif(state=='PAUSE'):
             
                self.pauseFrame()
                
            elif(state=='OVER'):
                self.over()
                
            else:
                self.startFrame()
                
    def getUserInput(self):
        return self.state
    
    def gameinput(self):
        temp=self.gamestate
        print(temp)
        self.gamestate=""
        return temp
        
    def over(self):
        self.state="IDLE"
        tkinter.messagebox.showinfo("Tetris", "Game Over")
        
    def play(self):
        print("viewPlay")
        self.state='PLAY'
        
    def set(self):
        print("viewSet")
        self.state='SET'
       
    def pause(self):
        self.state='PAUSE'
        
    def cancel(self):
        if(self.state=="SET"):
            self.state='IDLE'
            
        elif(self.state=="PAUSE"):
            self.state='PLAY'
            
    def restart(self):
        self.state="IDLE"
    def left_key(self,event):
        self.gamestate="LEFT"
    def right_key(self,event):
        self.gamestate="RIGHT"
    def up_key(self,event):
        self.gamestate="UP"
    def down_key(self,event):
        self.gamestate="DOWN"
    def clear_key(self):
        self.gamestate=""
    
# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
#from distutils.dist import command_re
#from tkinter.constants import ANCHOR
from PIL.ImageTk import PhotoImage
#from django.utils.termcolors import background
#from doctest import master
import numpy as np
class ParentView(tkinter.Frame):
    def __init__(self, master, model):
        self.mod=model
        tkinter.Frame.__init__(self, master)
        self.master.minsize(width=352, height=660)
        
        self.state=""
        self.gamestate=""
        self.scoreText="0"
        
        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)
        self.board= np.zeros([15,8])

        
    def changeView(self,state):
            self.clear()
            print("change"+self.state)
            self.state=state
            if state=="IDLE":
                
                self.startFrame()
            
            elif(state=="PLAY"):
             
                self.playFrame()
                
            elif(state=='SET'):
            
                self.setFrame()
                
            elif(state=='PAUSE'):
             
                self.pauseFrame()
                
            elif(state=='OVER'):
                self.over()
                
            else:
                self.startFrame()
                
    def getUserInput(self):
        return self.state
    
    def gameinput(self):
        temp=self.gamestate
        print(temp)
        self.gamestate=""
        return temp
        
    def over(self):
        self.state="IDLE"
        tkinter.messagebox.showinfo("Tetris", "Game Over")
        
    def play(self):
        print("viewPlay")
        self.state='PLAY'
        
    def set(self):
        print("viewSet")
        self.state='SET'
       
    def pause(self):
        self.state='PAUSE'
        
    def cancel(self):
        if(self.state=="SET"):
            self.state='IDLE'
            
        elif(self.state=="PAUSE"):
            self.state='PLAY'
            
    def restart(self):
        self.state="IDLE"
    def left_key(self,event):
        self.gamestate="LEFT"
    def right_key(self,event):
        self.gamestate="RIGHT"
    def up_key(self,event):
        self.gamestate="UP"
    def down_key(self,event):
        self.gamestate="DOWN"
    def clear_key(self):
        self.gamestate=""
    
class Application(ParentView):
    def __init__(self, master,model):
        super().__init__(master, model)
        
        self.playImage=PhotoImage(file='./play.png')
        self.setImage=PhotoImage(file='./settings.png')
        self.setImage2=PhotoImage(file='./settings2.png')
        self.logoImage=PhotoImage(file='./logo.png')
        self.pauseImage=PhotoImage(file='./pause.png')
        self.cancelImage=PhotoImage(file='./cancel.png')
        self.restartImage=PhotoImage(file='./restart.png')
        self.master.config(bg="black")
        
        self.inputText = tkinter.Label(master,image=self.logoImage,text="tetris",bg="black")
        self.score=tkinter.Label(master,font=('Arial,80'),width=15,height=2,text="score : "+self.scoreText,bg="black",fg="white")
        self.playButton=tkinter.Button(master,image=self.playImage,text='PLAY',width=50,height=50,command=self.play,bg="#0096E6")
    
        self.settingButton=tkinter.Button(master,image=self.setImage,text='SET',width=50,height=50,command=self.set,bg="#0096E6")
        self.pauseButton=tkinter.Button(master,image=self.pauseImage,text='PAUSE',width=30,height=30,command=self.pause,bg="black")
        self.restartButton=tkinter.Button(master,image=self.restartImage,text='RESTART',width=80,height=80,command=self.restart,bg="#0096E6")
        self.cancelButton=tkinter.Button(master,image=self.cancelImage,text='CANCEL',width=80,height=80,command=self.cancel,bg="#0096E6")
        self.canvas=tkinter.Canvas(width=320,height=600,bg="#FFFFF3")
                    
        self.panel=tkinter.StringVar()
        self.panel1=tkinter.Radiobutton(text='1',font=('Arial,100'),variable=self.panel,value='1',command=self.panelchange,bg="black",fg="white")
        self.panel2=tkinter.Radiobutton(text='2',font=('Arial,100'),variable=self.panel,value='2',command=self.panelchange,bg="black",fg="white")
        self.panel3=tkinter.Radiobutton(text='3',font=('Arial,100'),variable=self.panel,value='3',command=self.panelchange,bg="black",fg="white")
        self.panel4=tkinter.Radiobutton(text='4',font=('Arial,100'),variable=self.panel,value='4',command=self.panelchange,bg="black",fg="white")
        self.changPanel=tkinter.Label(master,font=('Arial,80'),width=15,height=2,text="Choose Panel",bg="black",fg="white")
        self.viewflag=1
        self.startFrame()
                
    def startFrame(self):
        self.playButton.place(x=176,y=300,anchor='center')
        self.settingButton.place(x=176,y=400,anchor='center')
        self.inputText.place(x=176,y=100,anchor='n')
        
    def updateGame(self):
        #print("update")
        
        canvas=tkinter.Canvas(self.canvas,width=320,height=600,bg="#FFFFF3")
        canvas.place(x=0,y=0,width=320,height=600,anchor='nw')
        outside=canvas.create_rectangle(0,0,320,600)
        self.score.config(text="score : "+str(self.mod.point))
        self.score.place(x=0,y=0,anchor='nw')
      
        col=0
        row=0
       # print(self.mod.board_state)
        for i in range(0,120):
            row=int(i/8)
            col=int(i%8)
            self.board[row][col]=self.mod.board_state[i]
            
        
        for i in range(0,15):
            for j in range(0,8):
                square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#FFFFF3")
                if self.board[i][j]==1:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#E53A40")#red
                elif self.board[i][j]==2:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#30A9DE")#blue
                elif self.board[i][j]==3:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#8CD790")#green
                elif self.board[i][j]==4:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#EFDC05")#yellow
                elif self.board[i][j]==5:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#A593E0")#purple
                elif self.board[i][j]==6:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#D4DFE6")#gray
                elif self.board[i][j]==7:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#F17F42")#orange
                else:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40)
                #print("test"+str(self.board[i][j]))
        
    def playFrame(self):
        self.canvas.place(x=18,y=45,width=320,height=600,anchor='nw')
        self.pauseButton.place(x=176,y=5,anchor='n')
        outside=self.canvas.create_rectangle(0,0,320,600)#每格40
        
        
    def pauseFrame(self):
        self.restartButton.place(x=176,y=200,anchor='center')
        self.cancelButton.place(x=176,y=300,anchor='center')
        
        
    def setFrame(self):
        self.changPanel.place(x=176,y=150,anchor='center')
        self.panel1.place(x=126,y=200,anchor='center')
        self.panel2.place(x=176,y=200,anchor='center')
        self.panel3.place(x=226,y=200,anchor='center')
        self.panel4.place(x=256,y=200,anchor='center')
        self.cancelButton.config(image='',text="back",width=5,height=5,bg="black",fg="white")
        self.cancelButton.place(x=176,y=300,anchor='center')
    
    def clear(self):
        self.settingButton.config(image=self.setImage,width=50,height=50)
        self.cancelButton.config(image=self.cancelImage,width=80,height=80,bg="#0096E6")
        self.changPanel.place_forget()
        self.canvas.place_forget()
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
        self.panel4.place_forget()
        
    def panelchange(self):
        self.viewflag=int(self.panel.get())
        print (self.panel.get()+" button pressed")
        print(self.viewflag)
        
class View2(ParentView):
    def __init__(self, master, model):
        super().__init__(master, model)
        
        self.canvas=tkinter.Canvas(width=320,height=600,bg="#FFFFF3")
        self.playImage=PhotoImage(file='./play1.png')
        self.setImage=PhotoImage(file='./set1.png')
        self.setImage2=PhotoImage(file='./set1.png')
        self.logoImage=PhotoImage(file='./logo1.png')
        self.pauseImage=PhotoImage(file='./pause1.png')
        self.cancelImage=PhotoImage(file='./cancel1.png')
        self.restartImage=PhotoImage(file='./home1.png')
        self.master.config(bg="white")

        self.settingButton=tkinter.Button(master,image=self.setImage,text='SET',width=80,height=80,command=self.set,bg="white")        
        self.playButton=tkinter.Button(master,image=self.playImage,text='PLAY',width=80,height=80,command=self.play,bg="white")
        self.inputText = tkinter.Label(master,image=self.logoImage,text="tetris",bg="white")    

        self.pauseButton=tkinter.Button(master,image=self.pauseImage,text='PAUSE',width=30,height=30,command=self.pause,bg="white")
        
        
        self.score=tkinter.Label(master,font=('Arial,80'),width=10,height=2,text="score : "+self.scoreText,bg="white",fg="black")
        self.restartButton=tkinter.Button(master,image=self.restartImage,text='RESTART',width=80,height=80,command=self.restart,bg="white")
        self.cancelButton=tkinter.Button(master,image=self.cancelImage,text='CANCEL',width=80,height=80,command=self.cancel,bg="white")
        
                                   
        self.panel=tkinter.StringVar()
        self.panel1=tkinter.Radiobutton(text='1',font=('Arial,100'),variable=self.panel,value='1',command=self.panelchange,bg="white",fg="black")
        self.panel2=tkinter.Radiobutton(text='2',font=('Arial,100'),variable=self.panel,value='2',command=self.panelchange,bg="white",fg="black")
        self.panel3=tkinter.Radiobutton(text='3',font=('Arial,100'),variable=self.panel,value='3',command=self.panelchange,bg="white",fg="black")
        self.panel4=tkinter.Radiobutton(text='4',font=('Arial,100'),variable=self.panel,value='4',command=self.panelchange,bg="white",fg="black")
        self.changPanel=tkinter.Label(master,font=('Arial,80'),width=15,height=2,text="Choose Panel",bg="white",fg="black")
        self.viewflag=2        
        
        self.startFrame()
    
                
    def startFrame(self):
        self.playButton.place(x=176,y=300,anchor='center')
        self.settingButton.place(x=176,y=450,anchor='center')
        self.inputText.place(x=176,y=100,anchor='n')
        
    def updateGame(self):
        #print("update")
        
        canvas=tkinter.Canvas(self.canvas,width=320,height=600,bg="#FFFFF3")
        canvas.place(x=0,y=0,width=320,height=600,anchor='nw')
        outside=canvas.create_rectangle(0,0,320,600)
        self.score.config(text="score : "+str(self.mod.point))
        self.score.place(x=0,y=0,anchor='nw')
      
        col=0
        row=0
       # print(self.mod.board_state)
        for i in range(0,120):
            row=int(i/8)
            col=int(i%8)
            self.board[row][col]=self.mod.board_state[i]
            
        
        for i in range(0,15):
            for j in range(0,8):
                square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#FFFFF3")
                if self.board[i][j]==1:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#E53A40")#red
                elif self.board[i][j]==2:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#30A9DE")#blue
                elif self.board[i][j]==3:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#8CD790")#green
                elif self.board[i][j]==4:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#EFDC05")#yellow
                elif self.board[i][j]==5:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#A593E0")#purple
                elif self.board[i][j]==6:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#D4DFE6")#gray
                elif self.board[i][j]==7:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#F17F42")#orange
                else:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40)
                #print("test"+str(self.board[i][j]))
        
    def playFrame(self):
        self.canvas.place(x=18,y=45,width=320,height=600,anchor='nw')
        self.pauseButton.place(x=176,y=5,anchor='n')
        outside=self.canvas.create_rectangle(0,0,320,600)#每格40
        
        
    def pauseFrame(self):
        self.restartButton.place(x=176,y=200,anchor='center')
        self.cancelButton.place(x=176,y=300,anchor='center')
        
        
    def setFrame(self):
        self.changPanel.place(x=176,y=150,anchor='center')
        self.panel1.place(x=106,y=200,anchor='center')
        self.panel2.place(x=156,y=200,anchor='center')
        self.panel3.place(x=206,y=200,anchor='center')
        self.panel4.place(x=256,y=200,anchor='center')
        self.cancelButton.config(image='',text="back",width=5,height=5,bg="white",fg="black")
        self.cancelButton.place(x=176,y=300,anchor='center')
    
    def clear(self):
        self.settingButton.config(image=self.setImage,width=80,height=80)
        self.cancelButton.config(image=self.cancelImage,width=80,height=80,bg="white")
        self.changPanel.place_forget()
        self.canvas.place_forget()
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
        self.panel4.place_forget()
        
    def panelchange(self):
        self.viewflag=int(self.panel.get())
        print (self.panel.get()+" button pressed")
        print(self.viewflag)
        
        
        
class View_HU(ParentView):
    def __init__(self, master,model):
        super().__init__(master, model)
        self.playImage=PhotoImage(file='./HU_play.png')
        self.setImage=PhotoImage(file='./HU_set.png')
        self.setImage2=PhotoImage(file='./HU_set.png')
        self.logoImage=PhotoImage(file='./HU_logo.png')
        self.pauseImage=PhotoImage(file='./HU_pause.png')
        self.cancelImage=PhotoImage(file='./cancel.png')
        self.restartImage=PhotoImage(file='./restart.png')
        self.master.config(bg="gray")
        
        self.inputText = tkinter.Label(master,image=self.logoImage,text="tetris",bg="gray")
        self.score=tkinter.Label(master,font=("Helvetica", 12,"bold"),width=11,height=2,text="score : "+self.scoreText,bg="gray",fg="#E53A40")
        self.playButton=tkinter.Button(master,image=self.playImage,text='PLAY',width=50,height=50,command=self.play,bg="gray")
    
        self.settingButton=tkinter.Button(master,image=self.setImage,text='SET',width=50,height=50,command=self.set,bg="gray")
        self.pauseButton=tkinter.Button(master,image=self.pauseImage,text='PAUSE',width=30,height=30,command=self.pause,bg="gray")
        
        self.cancelButton=tkinter.Button(master,image=self.cancelImage,text='CANCEL',width=80,height=80,command=self.cancel,bg="#E53A40")
        self.restartButton=tkinter.Button(master,image=self.restartImage,text='RESTART',width=80,height=80,command=self.restart,bg="#4169E1")
        
        self.canvas=tkinter.Canvas(width=320,height=600,bg="#E53A40")
                    
        
        self.panel=tkinter.StringVar()
        self.panel1=tkinter.Radiobutton(text='1',font=('Arial',13),variable=self.panel,value='1',command=self.panelchange,bg="gray",fg="white")
        self.panel2=tkinter.Radiobutton(text='2',font=('Arial',13),variable=self.panel,value='2',command=self.panelchange,bg="gray",fg="white")
        self.panel3=tkinter.Radiobutton(text='3',font=('Arial',13),variable=self.panel,value='3',command=self.panelchange,bg="gray",fg="white")
        self.panel4=tkinter.Radiobutton(text='4',font=('Arial',13),variable=self.panel,value='4',command=self.panelchange,bg="gray",fg="white")
        self.changPanel=tkinter.Label(master,font=('Arial',20),width=15,height=2,text="Choose Panel",bg="gray",fg="white")
        self.viewflag=3
        self.startFrame()
                
    def startFrame(self):
        self.playButton.place(x=176,y=300,anchor='center')
        self.settingButton.place(x=176,y=400,anchor='center')
        self.inputText.place(x=176,y=100,anchor='n')
        
    def updateGame(self):
        #print("update")
        
        canvas=tkinter.Canvas(self.canvas,width=320,height=600,bg="#FFFFF3")
        canvas.place(x=0,y=0,width=320,height=600,anchor='nw')
        outside=canvas.create_rectangle(0,0,320,600)
        self.score.config(text=str(self.mod.point) + " Ps!")
        self.score.place(x=0,y=0,anchor='nw')
      
        col=0
        row=0
       # print(self.mod.board_state)
        for i in range(0,120):
            row=int(i/8)
            col=int(i%8)
            self.board[row][col]=self.mod.board_state[i]
            
        
        for i in range(0,15):
            for j in range(0,8):
                square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#FFFAFA")
                if self.board[i][j]==1:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#4169E1")#red#B0C4DE
                elif self.board[i][j]==2:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#DAA520")#blue#30A9DE
                elif self.board[i][j]==3:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#B0C4DE")#green#8CD790
                elif self.board[i][j]==4:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#48D1CC")#yellow#EFDC05
                elif self.board[i][j]==5:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#6B8E23")#purple#A593E0
                elif self.board[i][j]==6:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#98FB98")#gray#D4DFE6
                elif self.board[i][j]==7:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#DC143C")#orange#F17F42
        
    def playFrame(self):
        self.canvas.place(x=18,y=45,width=320,height=600,anchor='nw')
        self.pauseButton.place(x=176,y=5,anchor='n')
        outside=self.canvas.create_rectangle(0,0,320,600)#每格40
        
        
    def pauseFrame(self):
        self.restartButton.place(x=100,y=250,anchor='center')
        self.cancelButton.place(x=250,y=250,anchor='center')
        
        
    def setFrame(self):
        self.changPanel.place(x=176,y=150,anchor='center')
        self.panel1.place(x=100,y=200,anchor='center')
        self.panel2.place(x=150,y=200,anchor='center')
        self.panel3.place(x=200,y=200,anchor='center')
        self.panel4.place(x=250,y=200,anchor='center')
        self.cancelButton.place(x=176,y=300,anchor='center')
    
    def clear(self):
        self.settingButton.config(image=self.setImage,width=50,height=50)
        self.cancelButton.config(image=self.cancelImage,width=80,height=80,bg="#E53A40")
        self.changPanel.place_forget()
        self.canvas.place_forget()
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
        self.panel4.place_forget()
    
        
    def panelchange(self):
        self.viewflag=int(self.panel.get())
        print (self.panel.get()+" button pressed")
        print(self.viewflag)

        
class View4(ParentView):
    def __init__(self, master,model):
        super().__init__(master, model)
        
        self.playImage=PhotoImage(file='./play4.png')
        self.setImage=PhotoImage(file='./set4.png')
        self.setImage2=PhotoImage(file='./set4.png')
        self.logoImage=PhotoImage(file='./logo4.png')
        self.pauseImage=PhotoImage(file='./pause4.png')
        self.cancelImage=PhotoImage(file='./cancel.png')
        self.restartImage=PhotoImage(file='./restart.png')
        self.master.config(bg="blue")
        
        self.inputText = tkinter.Label(master,image=self.logoImage,text="tetris",bg="gray")
        self.score=tkinter.Label(master,font=("Arial", 15,"bold"),width=11,height=2,text="score : "+self.scoreText,bg="blue",fg="white")
        self.playButton=tkinter.Button(master,image=self.playImage,text='PLAY',width=50,height=50,command=self.play,bg="blue")
    
        self.settingButton=tkinter.Button(master,image=self.setImage,text='SET',width=50,height=50,command=self.set,bg="blue")
        self.pauseButton=tkinter.Button(master,image=self.pauseImage,text='PAUSE',width=30,height=30,command=self.pause,bg="blue")
        
        self.cancelButton=tkinter.Button(master,image=self.cancelImage,text='CANCEL',width=80,height=80,command=self.cancel,bg="#0096E6")
        self.restartButton=tkinter.Button(master,image=self.restartImage,text='RESTART',width=80,height=80,command=self.restart,bg="#0096E6")
        
        self.canvas=tkinter.Canvas(width=320,height=600,bg="#E53A40")
                    
        
        self.panel=tkinter.StringVar()
        self.panel1=tkinter.Radiobutton(text='1',font=('Arial',20),variable=self.panel,value='1',command=self.panelchange,bg="blue",fg="white")
        self.panel2=tkinter.Radiobutton(text='2',font=('Arial',20),variable=self.panel,value='2',command=self.panelchange,bg="blue",fg="white")
        self.panel3=tkinter.Radiobutton(text='3',font=('Arial',20),variable=self.panel,value='3',command=self.panelchange,bg="blue",fg="white")
        self.panel4=tkinter.Radiobutton(text='4',font=('Arial',20),variable=self.panel,value='4',command=self.panelchange,bg="blue",fg="white")
        self.changPanel=tkinter.Label(master,font=('Arial',20),width=15,height=2,text="Choose Panel",bg="blue",fg="white")
        self.viewflag=4
        self.startFrame()
                
    def startFrame(self):
        self.playButton.place(x=176,y=300,anchor='center')
        self.settingButton.place(x=176,y=400,anchor='center')
        self.inputText.place(x=176,y=100,anchor='n')
        
    def updateGame(self):
        #print("update")
        
        canvas=tkinter.Canvas(self.canvas,width=320,height=600,bg="#FFFFF3")
        canvas.place(x=0,y=0,width=320,height=600,anchor='nw')
        outside=canvas.create_rectangle(0,0,320,600)
        self.score.config(text=str(self.mod.point) + " Ps!")
        self.score.place(x=0,y=0,anchor='nw')
      
        col=0
        row=0
       # print(self.mod.board_state)
        for i in range(0,120):
            row=int(i/8)
            col=int(i%8)
            self.board[row][col]=self.mod.board_state[i]
            
        
        for i in range(0,15):
            for j in range(0,8):
                square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#FFFAFA")
                if self.board[i][j]==1:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#4169E1")#red#B0C4DE
                elif self.board[i][j]==2:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#DAA520")#blue#30A9DE
                elif self.board[i][j]==3:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#B0C4DE")#green#8CD790
                elif self.board[i][j]==4:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#48D1CC")#yellow#EFDC05
                elif self.board[i][j]==5:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#6B8E23")#purple#A593E0
                elif self.board[i][j]==6:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#98FB98")#gray#D4DFE6
                elif self.board[i][j]==7:
                    square=canvas.create_rectangle(j*40,i*40,j*40+40,i*40+40,fill="#DC143C")#orange#F17F42
        
    def playFrame(self):
        self.canvas.place(x=18,y=45,width=320,height=600,anchor='nw')
        self.pauseButton.place(x=176,y=5,anchor='n')
        outside=self.canvas.create_rectangle(0,0,320,600)#每格40
        
        
    def pauseFrame(self):
        self.restartButton.place(x=100,y=250,anchor='center')
        self.cancelButton.place(x=250,y=250,anchor='center')
        
        
    def setFrame(self):
        self.changPanel.place(x=176,y=150,anchor='center')
        self.panel1.place(x=100,y=200,anchor='center')
        self.panel2.place(x=150,y=200,anchor='center')
        self.panel3.place(x=200,y=200,anchor='center')
        self.panel4.place(x=250,y=200,anchor='center')
        self.cancelButton.place(x=176,y=300,anchor='center')
    
    def clear(self):
        self.settingButton.config(image=self.setImage,width=50,height=50)
        self.cancelButton.config(image=self.cancelImage,width=80,height=80,bg="#E53A40")
        self.changPanel.place_forget()
        self.canvas.place_forget()
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
        self.panel4.place_forget()
    
        
    def panelchange(self):
        self.viewflag=int(self.panel.get())
        print (self.panel.get()+" button pressed")
        print(self.viewflag)
