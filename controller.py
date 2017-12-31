# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:37:58 2017

@author: vincentS
"""

class Control(object):    
    #state {NULL, IDLE, PLAY, CHECK, SET, PAUSE, OVER}
    def __init__(self):
#        self.model = model
#        self.view = view
        self.flag = False
        self.state = "NULL"
    
#    def input(self, event):
#        if self.state == "PLAY":
#            self.model.gameinput(event)
#        elif self.state == "SET":
#            self.model.input(event)

    def setstate(self, state):
        self.state = state
        print (self.state)
 #       self.model.Set_State(self.state)

    def finishcheck(self):
        return True
#        return self.model.finishflag()

    def start(self):
        self.setstate("IDLE")
        
    def finish(self):
        return self.flag
    
    def play(self):
        self.setstate("PLAY")
        while self.state == "PLAY":
            if self.finishcheck:
                self.setstate("CHECK")
                while self.state == "CHECK":
                    if self.finishcheck:
                        self.setstate("PLAY")
#            if not self.model.Check_Frozen():
            if self.finish():
                self.setstate("OVER")

    def pause(self):
        self.setstate("PAUSE")
        
    def setting(self):
        self.setstate("SET")



a = Control()
state = a.state
a.start()
while a.state != "OVER":
    b = input("input:")
    print (b)
    if int(b) == 1:
        a.play()
    if int(b) == 2:
        a.pause()
    if int(b) == 3:
        a.setting()
    if int(b) == 4:
        a.flag = True
    if int(b) == 5:
        break