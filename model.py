# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:07:48 2017

@author: Danny
"""
import random
import time

# 定義磚塊.
brick_dict = {
        10: [ 4, 8, 9,13], 11: [ 9,10,12,13],   # N1.
        20: [ 5, 8, 9,12], 21: [ 8, 9,13,14],   # N2.
        30: [ 8,12,13,14], 31: [ 4, 5, 8,12], 32: [8,  9, 10, 14], 33: [5,  9, 12, 13], # L1.
        40: [10,12,13,14], 41: [ 4, 8,12,13], 42: [8,  9, 10, 12], 43: [4,  5,  9, 13], # L2.
        50: [ 9,12,13,14], 51: [ 4, 8, 9,12], 52: [8,  9, 10, 13], 53: [5,  8,  9, 13], # T.
        60: [ 8, 9,12,13],    # O.
        70: [12,13,14,15], 71: [ 1, 5, 9,13]    #I.
}
# 方塊編號(1~7).
brick_id = 1
# 方塊狀態(0~3).
brick_state = 0
# 下一個磚塊編號(1~7).
brick_next_id = 1

class Model:
    speed = 5
    def __init__(self, lv = 5):
        self.speed = lv
        self.state = "IDLE"
        
    def Set_State(self, newState):
        if newState == "PLAY":
            self.state = "PLAY"
            if self.Play():
                self.Set_State("Check")
            
        elif newState =="Check":
            self.state = "Check"
            if self.Check_Frozen():
                self.Set_State("PLAY")
            else:
                self.Set_State("OVER")
            
        elif newState == "IDLE":
            self.state = "IDLE"
            
        elif newState == "SET":
            self.state = "SET"
            self.Change_Speed()
            
        elif newState == "PAUSE":
            self.state = "PAUSE"
            
        elif newState == "OVER":
            self.state = "OVER"
            
        else:
            return
    def Change_Speed(self, lv):
        self.speed = lv
        
    def Get_Speed(self):
        return self.speed
    
class GameModel(Model):
    def __init__(self, lv = 5):
        super().__init__(lv)
        self.falling_block = []
        self.falling_class = 0
        
        self.board = (8,15)# x,y
        self.board_state = []#print mode
        self.frozen_board = []#frozen check
        
        #all board state
        size = self.board[0] * self.board[1]
        for i in range(0,size):
            self.board_state.append(0)#nothing
            self.frozen_board.append(0)
            
        self.New_Block()
        self.Play()
        
    def Turn(self):
        if self.falling_class == 1:
            print(1)

        elif self.falling_class == 2:
            print(2)

        elif self.falling_class == 3:
            print(3)

        elif self.falling_class == 4:
            print(4)

        elif self.falling_class == 5:
            print(5)

        elif self.falling_class == 6:
            print(6)

        elif self.falling_class == 7:
            print(7)

        else:
            print("error")
            
    def Move(self):
        
        if not self.Check_Frozen():
            return "Lose"
            
    def Check_Frozen(self, temp):
        flag = False
        for i in temp:
            if self.frozen_board[i] != 0:#hit
                flag = True
                
        if flag:# hit and then store falling block into frozen board
            state = int(self.falling_class / 10)
            for blc in self.falling_block:
                self.frozen_board[blc] = state
                
            return True
        
        return False
        
    
    
               
    def Check_Erase(self):
        chk_rowStart = []
        for block in self.falling_block:
            x = block % self.board[0]
            start = block - x
            if not (start in chk_rowStart):
                chk_rowStart.append(start)#store all row start need to check
                
        erase_row = []
        for x in chk_rowStart:
            i = 0
            tmp = x
            while not (self.frozen_board[tmp] == 0):
                i += 1
                tmp = x + i
            
                if i >= self.board[0]:
                    erase_row.append(x)
                    break
            
                
            
        print("Erase")
        

    def Check_End(self):
        #改state
        
        print("Check_End")
        return False
        

    def New_Block(self):
        self.falling_class = random.choice([10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43, 50, 51, 52, 53, 60, 70, 71])
        self.falling_block = brick_dict[self.falling_class]
        
        state = int(self.falling_class / 10)
        for x in self.falling_block:
            self.board_state[x] = state#print something exist
            
    def Fall_Down(self):
        exist = True
        temp = []#next place
        temp.append(self.falling_block[0] + self.board[0])
        temp.append(self.falling_block[1] + self.board[0])
        temp.append(self.falling_block[2] + self.board[0])
        temp.append(self.falling_block[3] + self.board[0])
        
        #hit
        if self.Check_Frozen(temp):#T hit , F not hit
            self.Check_Erase()
            self.board_state = self.frozen_board
            exist = self.Check_End()# T exist, F die
            if exist:
                self.New_Block()
            else:
                #die
        
        #not hit
        else:
            #delete privious falling block
            for i in self.falling_block:
                self.board_state[i] = 0
                
            #move down    
            self.falling_block = temp
            state = int(self.falling_class / 10)
            for i in self.falling_block:
                self.board_state[i] = state#print something exist
                
        return exist
        
    def Play(self):
        exact_Speed = 1 / self.speed
        time.sleep(exact_Speed)
        return self.Fall_Down()
        
a = GameModel()
a.Fall_Down()
