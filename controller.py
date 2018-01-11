# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:37:58 2017

@author: vincentS
"""
import view
import model
import tkinter
import time
from _overlapped import NULL

class Control():    
    #state {NULL, IDLE, PLAY, CHECK, SET, PAUSE, OVER}
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Tetris")
        self.model = model.GameModel()
        self.view = view.Application(self.root,self.model)
        self.fflag = False
        self.flag = False
        self.input = False
        self.state = "NULL"
        
        #self.start()
    def gameinput(self, event):
        if event == "LEFT":
            self.model.Move()
        if event == "RIGHT":
            self.model.Move()
        if event == "DOWN":
            self.model.Move()
        if event == "ROTATE":
            self.model.Turn()

    def setstate(self, state): 
        self.state = state
        self.view.changeView(self.state)
        print (self.state)
        self.model.Set_State(self.state)

    def getbuttoninput(self):
        return self.view.getUserInput()
    
    def getkeyinput(self):
        return self.view.gameinput()
    #檢查掉落結束
#    def finishcheck(self):
 #       return self.model.finishflag()
    def finishcheck(self):
        return self.flag
    def finish(self):
        return self.fflag

    def start(self):
        
        self.setstate("IDLE")
        #print("IDLE")
        while True:
            #print(self.state)
            button = self.getbuttoninput()
            if self.state != button:
                self.setstate(button)
                if button == "PLAY":
                    timer = time.time()
                if button == ("IDLE"):
                    self.model.__init__()
                    self.view.mod = self.model
                
            elif self.state == "PLAY":  
                timepass = float(time.time()-timer)
                #print (timepass)
                
                if timepass > (1):
                    #s(self.model.frozen_board)
                    if self.model.Fall_Down():                        
                        timer = time.time()
                        self.view.updateGame()
                    else:
                        self.setstate("OVER")
                        self.view.state = "IDLE"
    
                    
                else:
                    key = self.getkeyinput()
                    if key != "":
                        print(key)
                        if key == "UP":
                            self.model.Turn()
                        elif key == "DOWN":
                            if not self.model.Fall_Down():
                                self.view.state = "OVER"
                                self.setstate("IDLE")
                            
                                
                        elif key == "LEFT":
                            self.model.Move(-1)
                        elif key == "RIGHT":
                            self.model.Move(1)
                        self.view.clear_key()
                    self.view.updateGame()
                #if self.getkeyinput()!="NULL":
                   # self.model.move()
               # if not self.model.Play():
                  #  self.setstate("OVER")
            
            self.root.update()
                    

    
    def check(self):
        self.setstate("CHECK")

    def pause(self):
        self.setstate("PAUSE")
        
    def setting(self):
        self.setstate("SET")

"""
root = tkinter.Tk()
root.title("Tetris")
m=model.GameModel()
v=view.Application(root,m)

c=Control(m,v)
root.mainloop()
"""
c=Control()
c.start()