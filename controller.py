# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:37:58 2017

@author: vincentS
"""
import view
import model

class Control():    
    #state {NULL, IDLE, PLAY, CHECK, SET, PAUSE, OVER}
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.fflag = False
        self.flag = False
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
    #檢查掉落結束
#    def finishcheck(self):
 #       return self.model.finishflag()
    def finishcheck(self):
        return self.flag
    def finish(self):
        return self.fflag

    def start(self):
        self.setstate("IDLE")
        while True:
            if self.state != self.getbuttoninput():
                self.setstate(self.getbuttoninput())
            if self.state == "PLAY":                
                if self.getkeyinput()!="NULL":
                    self.modle.move()
                if not self.modle.Play():
                    self.setstate("OVER")
            self.view.changeView()    
                    

    
    def check(self):
        self.setstate("CHECK")

    def pause(self):
        self.setstate("PAUSE")
        
    def setting(self):
        self.setstate("SET")



