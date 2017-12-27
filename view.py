import tkinter as tk
import controller,model

class view(object):
    window=tk.Tk()
    window.title('Tetris Battle')
    window.geometry('400x500')
    tetrisController=controller()
    state=''
    play=tk.Button(window,text='play',commond=tetrisController.input('PLAY'))
    setting=tk.Button(window,text='setting',commond=tetrisController.input('SET'))
    pause=tk.Button(window,text='pause',commond=tetrisController.input('PAUSE'))
    esc=tk.Button(window,text='end',commond=tetrisController.input('ESC'))
    def __init__(self):
        self.newState = 'IDLE'

    def stateHasChanged(self,model,newState):
        self.gameModel=model
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
    
    def getUserInput(self):
        self.tetrisController.input(self.state)
       
    
    def start(self):
        l=tk.Label(self.window,text='Tetris Soft.Engi')
        self.l.pack()
        self.play.pack()
        self.setting.pack()
        self.esc.pack() 
    def setting(self):
        
        self.setting.pack()
    def pause(self):
       
        self.esc.pack()
    def play(self):    
        self.play.pack()
        
        
    window.mainloop()    
a=view()
a.getUserInput()

    