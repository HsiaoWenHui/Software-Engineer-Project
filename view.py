from tkinter import *


class view(Frame):
  
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.grid()
        self.newState = 'IDLE'
        self.start()
        #self.stateHasChanged()

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
        self.inputText = Label(self,text="tetris")
        self.inputText.grid(row=0, column=0)
        
        self.play = Button(self,text="play")
        self.play.grid(row=0, column=0)
        self.setting = Button(self,text="setting")
        self.setting.grid()
         
    def setting(self):
        
        self.setting.pack()
    def pause(self):
       
        self.esc.pack()
    def play(self):    
        self.play.pack()
        
        
   
if __name__ == '__main__':
    window = Tk()
    window.title('Tetris Battle')
    window.geometry('400x500')
    game = view(master=window)
    game.mainloop()


    