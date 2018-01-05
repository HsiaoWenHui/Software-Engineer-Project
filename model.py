# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:07:48 2017

@author: Danny
"""
import random
import time

# 定義磚塊.
brick_dict = {
        10: [3,11,12,20], 11: [3,4,10,11],   # N1.
        20: [4,11,12,19], 21: [3,4,12,13],   # N2.
        30: [3,11,12,13], 31: [3,4,11,19], 32: [2,3,4,12], 33: [4,12,19,20], # L1.
        40: [4,10,11,12], 41: [3,11,19,20], 42: [3,4,5,11], 43: [3,4,12,20], # L2.
        50: [3,4,5,12], 51: [3,11,12,19], 52: [4,11,12,20], 53: [3,10,11,12], # T.
        60: [3,4,11,12],    # O.
        70: [3,11,19,27], 71: [2,3,4,5]    #I.
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
        self.finishflag=False;
        
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
        self.falling_class = random.choice([10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43, 50, 51, 52, 53, 60, 70, 71])
        
        self.board = (8,15)# x,y
        self.board_state = []
        
        #all board state
        size = self.board[0] * self.board[1]
        for i in range(0,size):
            self.board_state.append(False)#nothing
            
        #falling now
        for j in self.falling_block:
            self.board_state[j] = True#something exist
            
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
        for i in range(0,4):
            if self.board_state[temp[i]] == True:
                return True#hit
        return False#not hit
               
    def Check_Erase(self):
        for block in self.falling_block:
            x = block % self.board[0]
            y = block % self.board[1]
            start = block - x
        print("Erase")
        

    def Check_End(self):
        #改state
        
        print("Check_End")
        return False
        

    def New_Block(self):
        self.falling_class = random.choice([10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43, 50, 51, 52, 53, 60, 70, 71])
        self.falling_block = brick_dict[self.falling_class]
        for i in range(0,4):
            self.board_state[self.falling_block[i]] = True
            
    def Fall_Down(self):
        exist = True
        temp = []#next place
        temp.append(self.falling_block[0] + self.board[0])
        temp.append(self.falling_block[1] + self.board[0])
        temp.append(self.falling_block[2] + self.board[0])
        temp.append(self.falling_block[3] + self.board[0])
        
        if self.Check_Frozen(temp):#T hit , F not hit
            self.Check_Erase()
            exist = self.Check_End()# T exist, F die
        else:
            self.falling_block = temp#move down
            for i in self.falling_block:
                self.board_state[i] = True#something exist
            
        return exist
        
    def Play(self):
        exact_Speed = 1 / self.speed
        time.sleep(exact_Speed)
        return self.Fall_Down()
        
a = GameModel()
a.Fall_Down()
