# -*- coding: utf-8 -*-

import view
import model
import tkinter
import time

class Control():    
    
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Tetris")
        self.model = model.GameModel()
        self.view = view.Application(self.root, self.model)
        self.viewflag = 1
        self.input = False
        self.state = "NULL"
        
        
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

    def start(self):
        
        self.setstate("IDLE")
        
        while True:
            
        
            button = self.getbuttoninput()
            if self.state != button:
                self.setstate(button)
                if button == "PLAY":
                    timer = time.time()
                if button == ("IDLE"):
                    self.model.__init__()
                    self.view.__init__(self.root, self.model) 
                
            elif self.state == "PLAY":  
                timepass = float(time.time()-timer)
                
                
                if timepass > (0.5): #掉落計時器
                    
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
                                self.setstate("OVER")
                            
                                
                        elif key == "LEFT":
                            self.model.Move(-1)
                        elif key == "RIGHT":
                            self.model.Move(1)
                        self.view.clear_key()
                    self.view.updateGame()
               
            elif self.state == "SET":#更改使用viewclass
                if self.viewflag != self.view.viewflag:
                    print("nowchange" + str(self.viewflag))
                    if self.view.viewflag == 1:
                        self.view.clear()
                        self.view = view.Application(self.root,self.model)
                        self.viewflag = 1
                        print ("viewflag"+str(self.viewflag))
                    elif self.view.viewflag == 2:
                        self.view.clear()
                        self.view = view.View2(self.root,self.model)
                        self.viewflag = 2
                        print ("viewflag"+str(self.viewflag))
                    elif self.view.viewflag == 3:
                        self.view.clear()
                        self.view = view.View_HU(self.root,self.model)
                        self.viewflag = 3
                        print ("viewflag"+str(self.viewflag))
                    elif self.view.viewflag == 4:
                        self.view.clear()
                        self.view = view.View4(self.root,self.model)
                        self.viewflag = 4
                        print ("viewflag"+str(self.viewflag))
            
            self.root.update()

c=Control()
c.start()
