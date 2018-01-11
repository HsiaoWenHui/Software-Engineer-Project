# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:20:11 2018

@author: vincentS
"""

import view

class View1(view.ParentView):
    def __init__(self, master, model):
        super().__init__(master, model)

        self.playImage=view.PhotoImage(file='./play1.png')
        self.setImage=view.PhotoImage(file='./set1.png')
        self.setImage2=view.PhotoImage(file='./settings2.png')
        self.logoImage=view.PhotoImage(file='./logo1.png')
        self.pauseImage=view.PhotoImage(file='./pause1.png')
        self.cancelImage=view.PhotoImage(file='./cancel1.png')
        self.restartImage=view.PhotoImage(file='./restart.png')
        self.master.config(bg="white")
        
        self.playButton=view.tkinter.Button(master,image=self.playImage,text='PLAY',width=50,height=50,command=self.play,bg="white")
        self.inputText = view.tkinter.Label(master,image=self.logoImage,text="tetris",bg="black")    
        self.settingButton=view.tkinter.Button(master,image=self.setImage,text='SET',width=50,height=50,command=self.set,bg="white")
        self.pauseButton=view.tkinter.Button(master,image=self.pauseImage,text='PAUSE',width=30,height=30,command=self.pause,bg="white")
        
        
        self.score=view.tkinter.Label(master,font=('Arial,80'),width=15,height=2,text="score : "+self.scoreText,bg="black",fg="white")
        self.restartButton=view.tkinter.Button(master,image=self.restartImage,text='RESTART',width=80,height=80,command=self.restart,bg="#0096E6")
        self.cancelButton=view.tkinter.Button(master,image=self.cancelImage,text='CANCEL',width=80,height=80,command=self.cancel,bg="#0096E6")
        self.canvas=view.tkinter.Canvas(width=320,height=600,bg="#FFFFF3")
                                   
        self.panel=view.tkinter.StringVar()
        self.panel1=view.tkinter.Radiobutton(text='1',font=('Arial,100'),variable=self.panel,value='1',command=self.panelchange,bg="black",fg="white")
        self.panel2=view.tkinter.Radiobutton(text='2',font=('Arial,100'),variable=self.panel,value='2',command=self.panelchange,bg="black",fg="white")
        self.panel3=view.tkinter.Radiobutton(text='3',font=('Arial,100'),variable=self.panel,value='3',command=self.panelchange,bg="black",fg="white")
        self.changPanel=view.tkinter.Label(master,font=('Arial,80'),width=15,height=2,text="Choose Panel",bg="black",fg="white")
        
        
        self.startFrame()
    
    def startFrame(self):
        self.playButton.place(x=176,y=300,anchor='center')
        self.settingButton.place(x=176,y=400,anchor='center')
        self.inputText.place(x=176,y=100,anchor='n')
        
    def updateGame(self):
        #print("update")
        self.canvas.destroy()
        canvas=view.tkinter.Canvas(width=320,height=600,bg="#FFFFF3")
        canvas.place(x=18,y=45,width=320,height=600,anchor='nw')
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
    
        
    def panelchange(self):
        print (self.view.get()+" button pressed")