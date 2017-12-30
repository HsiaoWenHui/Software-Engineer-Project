from tkinter import *
import tkinter as tk
import pygame,controller,model
from sys import exit  
from pygame.locals import *


class view(Frame):
  # def __init__(self,"""model,controller,""" master=None):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        pygame.init()
        self.setting()
        self.inputText = Label(text="tetris")
        self.play = Button(text="play",command=self.getUserInput('PLAY'))
        self.setting = Button(text="setting",command=self.getUserInput('SET'))
        self.pause = Button(text="pause",command=self.getUserInput('PAUSE'))
        self.ovsr = Button(text="over",command=self.getUserInput('OVER'))
        self.cancel = Button(text="cancel",command=self.getUserInput('CANCEL'))
        self.confirm = Button(text="confirm",command=self.getUserInput('CONFIRM'))
        self.replay = Button(text="replay",command=self.getUserInput('REPLAY'))

        
        self.model=model
        self.controller=controller
        self.grid()
        self.newState = 'IDLE'
        

    def stateHasChanged(self,newState):
        
        self.changeView(newState)
        
    def changView(self,newState):
        if(newState==self.gameModel.start_STATE):
            self.start
        elif(newState==self.gameModel.setting_STATE):
            self.setting
        elif(newState==self.gameModel.play_STATE):
            self.play
        elif(newState==self.gameModel.pause_STATE):
            self.pause
    
    def getUserInput(self,state=''):
        if(state=='PLAY'):
            return('PLAY')
        if(state=='SETTING'):
            return('PLAY')
        if(state=='PAUSE'):
            return('PAUSE')
        if(state=='OVER'):
            return('OVER')
        else:
         for event in pygame.event.get():  
            if event.type == QUIT:  
                exit()  
            if event.type == KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    self.controller.input('LEFT')
                if event.key ==pygame.K_RIGHT:
                    self.controller.input('RIGHT')
                if event.key ==pygame.K_DOWN:
                    self.controller.input('DOWN')
                if event.key ==pygame.K_LEFT:
                    self.controller.input('LEFT')
                if event.key ==pygame.K_SPACE:
                    self.controller.input('ROTATE')
             
    def start(self):
        self.inputText.grid(row=0, column=0)
        self.play.grid(row=50, column=50)
        self.setting.grid(row=100, column=50)
        
        
    def setting(self):
        self.canvas=tk.Canvas(self,width=400,height=400)
        self.canvas.create_rectangle(500,500,0,0,fill='gray')
        
        self.canvas.grid()
        
    def pause(self):
       
        self.esc.pack()
    def play(self):    
        self.play.pack()
        
        
   
if __name__ == '__main__':
    #model=model()
    #controller=controller() 
    
    
    window = Tk()
    window.title('Tetris Battle')
    window.geometry('400x500')
    game = view(master=window)
    game.mainloop()


    