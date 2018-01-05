# -*- coding: utf-8 -*-

import tkinter


class Application(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.master.minsize(width=100, height=100)
        self.master.config()
        self.inputText = tkinter.Label(self, text="tetris")
        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)
        self.main_frame = tkinter.Frame()
        self.main_frame.pack(fill='both', expand=True)
        self.inputText.pack()
        self.pack()

    @staticmethod
    def left_key(event):
        print ( " left key pressed")

    @staticmethod
    def right_key(event):
        print (" right key pressed")
    @staticmethod
    def up_key(event):
        print (" up key pressed")
    @staticmethod
    def down_key(event):
        print (" down key pressed")
root = tkinter.Tk()
app = Application(root)
app.mainloop()