# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:07:48 2017

@author: Danny
"""
import random
import time

# 定義磚塊.
brick_dict = {
    "10": ( 4, 8, 9,13), "11": ( 9,10,12,13),   # N1.
    "20": ( 5, 8, 9,12), "21": ( 8, 9,13,14),   # N2.
    "30": ( 8,12,13,14), "31": ( 4, 5, 8,12), "32": (8,  9, 10, 14), "33": (5,  9, 12, 13), # L1.
    "40": (10,12,13,14), "41": ( 4, 8,12,13), "42": (8,  9, 10, 12), "43": (4,  5,  9, 13), # L2.
    "50": ( 9,12,13,14), "51": ( 4, 8, 9,12), "52": (8,  9, 10, 13), "53": (5,  8,  9, 13), # T.
    "60": ( 8, 9,12,13),    # O.
    "70": (12,13,14,15), "71": ( 1, 5, 9,13)    #I.
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
        self.frozen_block = []#block [x,y,color]
        self.falling_block = []
        
        #0改隨機
        self.falling_class = random.randint(1,8) # 1 -> 長條,2 -> L,3 -> 反L,4 -> z,5 -> 反z,6 -> T,7 -> 田
        self.board = (8,15)
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
            
    def Check_Frozen(self):
#        for ... 所有:
#            if 有接觸:
#                self.New_Block()
#                self.Check_Erase()
#                return self.Check_End()
        return True#遊戲未結束
               
    def Check_Erase(self):
        print("Erase")
        

    def Check_End(self):
        #改state
        print("Check_End")
        return False
        

    def New_Block(self):
        self.falling_class = 0
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
            
    def Fall_Down(self):
        self.falling_block = [[1,1,1],[1,2,1],[1,3,1],[1,4,1]]
        temp_block =[]
        for index in self.falling_block:
            temp_block.append([index[0], index[1] + 1, index[2]])
        self.falling_block = temp_block
        return True
        
    def Play(self):
        exact_Speed = 1 / self.speed
        #while self.state == "PLAY":
        time.sleep(exact_Speed)
        return self.Fall_Down()
        
a = GameModel()
a.Fall_Down()
