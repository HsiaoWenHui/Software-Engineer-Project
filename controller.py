# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:37:58 2017

@author: vincentS
"""
from enum import Flag
import time
class Control():    
    #state {NULL, IDLE, PLAY, CHECK, SET, PAUSE, OVER}
    def __init__(self, view):
        #self.model = model
        self.view = view
        self.flag = False
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

#    def setinput(self. event):

    def setstate(self, state):
        self.state = state
        self.view.changeView(self.state)
        print (self.state)

 #       self.model.Set_State(self.state)

    #檢查掉落結束
#    def finishcheck(self):
 #       return self.model.finishflag()
    def finishcheck(self):
        return True
    def finish(self):
        return self.flag

    def start(self):
        self.setstate("IDLE")
    
    def play(self):
        self.setstate("PLAY")
        print("while playing")
        """while self.state == "PLAY":
            if self.finishcheck():
                print ("checking")
                self.setstate("CHECK")
                while self.state == "CHECK":
                    if self.finishcheck():
                        self.setstate("PLAY")
#            if self.model.Check_Frozen():
            if self.finish():
                self.setstate("OVER")
            time.sleep(10)"""

    def pause(self):
        self.setstate("PAUSE")
        
    def setting(self):
        self.setstate("SET")



