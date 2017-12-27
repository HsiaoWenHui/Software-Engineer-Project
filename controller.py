# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:37:58 2017

@author: vincentS
"""

class Control(object):
    state='NULL'
    
    def _init_(self, model, view):
        self.model = model
        self.view = view
        self.state = 'NULL'
    
    def input(self, event):
        if self.state == 'PLAY':
            self.model.gameinput(event)
        elif self.state == 'SET':
            self.model.input(event)
    
    def start(self):
        self.state = 'IDLE'
        self.view.stateHasChange(self.state)