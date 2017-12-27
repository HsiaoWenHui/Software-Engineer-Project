import tkinter as tk


class view(object):
    window=tk.Tk()
    window.title('Tetris Battle')
    window.geometry('400x500')
    
    def __init__(self):
        self.state = 'IDLE'
        
    def stateHasChanged(self,model,newState):
        self.gameModel=model
        self.changeView(newState)
        
    def changView(self,newState):
        if(newState==self.gameModel.start_STATE):
            idle=tk.Label(self.window,text='menu')
            idle.pack()
        elif(newState==self.gameModel.setting_STATE):
            idle=tk.Label(self.window,text='setting')
            idle.pack()
        elif(newState==self.gameModel.play_STATE):
            idle=tk.Label(self.window,text='play')
            idle.pack()
        elif(newState==self.gameModel.pause_STATE):
            idle=tk.Label(self.window,text='pause')
            idle.pack()
    
    def getUserInput(self):
        
        play=tk.Button(self.window,text='play')
        play.pack()
        setting=tk.Button(self.window,text='setting')
        setting.pack()
        esc=tk.Button(self.window,text='end')
        esc.pack()
        self.window.mainloop()
        
a=view()
a.getUserInput()
    