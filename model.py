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
        self.falling_class =random.choice([10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43, 50, 51, 52, 53, 60, 70, 71])
        for value in dict[self.falling_class].items():
            self.falling_block.append(value)
        
        self.board = (8,15)# x,y
        self.board_state = []#print mode
        self.frozen_board = []#frozen check
        self.point = 0
        
        #all board state
        size = self.board[0] * self.board[1]
        for i in range(0,size):
            self.board_state.append(0)#nothing
            self.frozen_board.append(0)
            
        self.New_Block()
        self.Play()
        
    def Turn(self):
        temp_Falling=list(self.falling_block) #複製原始block位置
        outCheck=True
        if self.falling_class == 10 :
            temp_Falling[1]=temp_Falling[1]-7
            temp_Falling[2]=temp_Falling[2]-2
            temp_Falling[3]=temp_Falling[3]-9
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in range(4):
                    if(j==i):
                        outCheck=False
            if(temp_Falling[0]%8==6)#第七行所占為七八行，無法轉入第九行
                outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class== 11:
            temp_Falling[1]=temp_Falling[1]+7
            temp_Falling[2]=temp_Falling[2]+2
            temp_Falling[3]=temp_Falling[3]+9
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in range(4):
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class-=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
             return self.falling_block[i]
            
        elif self.falling_class== 20:
            temp_Falling[0]=temp_Falling[0]-1
            temp_Falling[1]=temp_Falling[1]-7
            temp_Falling[3]=temp_Falling[3]-6
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(temp_Falling[0]%8==7)
                   outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 21:
            temp_Falling[0]=temp_Falling[0]+1
            temp_Falling[1]=temp_Falling[1]+7
            temp_Falling[3]=temp_Falling[3]+6
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class-=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]

        elif self.falling_class == 30:
            temp_Falling[1]=temp_Falling[1]-7
            temp_Falling[2]=temp_Falling[2]-1
            temp_Falling[3]=temp_Falling[3]+6
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 31:
            temp_Falling[0]=temp_Falling[0]-7
            temp_Falling[1]=temp_Falling[1]-7
            temp_Falling[2]=temp_Falling[2]-1
            temp_Falling[3]=temp_Falling[3]+6
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 32:
            temp_Falling[0]=temp_Falling[0]+2
            temp_Falling[1]=temp_Falling[1]+9
            temp_Falling[2]=temp_Falling[2]+15
            temp_Falling[3]=temp_Falling[3]+8
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 33:
            temp_Falling[0]=temp_Falling[0]-1
            temp_Falling[1]=temp_Falling[1]+1
            temp_Falling[2]=temp_Falling[2]+7
            temp_Falling[3]=temp_Falling[3]-7
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class-=3
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 40:
            temp_Falling[0]=temp_Falling[0]-1
            temp_Falling[1]=temp_Falling[1]+1
            temp_Falling[2]=temp_Falling[2]+8
            temp_Falling[3]=temp_Falling[3]+8
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 41:    
            temp_Falling[1]=temp_Falling[1]-7
            temp_Falling[2]=temp_Falling[2]-14
            temp_Falling[3]=temp_Falling[3]-9
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 42:
            temp_Falling[2]=temp_Falling[2]+7
            temp_Falling[3]=temp_Falling[3]+9
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 43:
            temp_Falling[0]=temp_Falling[0]+1
            temp_Falling[1]=temp_Falling[1]-6
            temp_Falling[2]=temp_Falling[2]-1
            temp_Falling[3]=temp_Falling[3]-8
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class-=3
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 50:
            temp_Falling[1]=temp_Falling[1]+7
            temp_Falling[2]=temp_Falling[2]+7
            temp_Falling[3]=temp_Falling[3]+7
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 51:
            temp_Falling[0]=temp_Falling[0]+1
            temp_Falling[3]=temp_Falling[3]+1
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 52:
            temp_Falling[0]=temp_Falling[0]-1
            temp_Falling[1]=temp_Falling[1]-1
            temp_Falling[2]=temp_Falling[2]-1
            temp_Falling[3]=temp_Falling[3]-8
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]

        elif self.falling_class == 53:
            temp_Falling[1]=temp_Falling[1]-6
            temp_Falling[2]=temp_Falling[2]-6
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 60:
            return self.falling_class
        
        elif self.falling_class == 70:
            temp_Falling[0]=temp_Falling[0]-1
            temp_Falling[1]=temp_Falling[1]-8
            temp_Falling[2]=temp_Falling[2]-15
            temp_Falling[3]=temp_Falling[3]-22
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class+=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]
            
        elif self.falling_class == 71:
            temp_Falling[0]=temp_Falling[0]+1
            temp_Falling[1]=temp_Falling[1]+8
            temp_Falling[2]=temp_Falling[2]+15
            temp_Falling[3]=temp_Falling[3]+22
            for i in self.frozen_board: #檢查是否在冷凍版上
                for j in temp_Falling:
                    if(j==i):
                        outCheck=False
            if(outCheck):#若沒有撞到frozen或是邊緣則可進行旋轉
                for i in range(4):
                        self.falling_class-=1
                        self.falling_block[i]=temp_Falling[i] #將假定值帶入
            return self.falling_block[i]

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

        #some row need to erase, move down upper block
        if erase_row:
            temp_board = self.frozen_board
            for rowX in erase_row:
                i = 0
                while i < rowX:
                    temp_board[i+self.board[0]] = temp_board[i]

        if len(erase_row) == 1:
            self.point += 10
        elif len(erase_row) == 2:
            self.point += 30
        elif len(erase_row) == 3:
            self.point += 70
        else:
            self.point += 150
        

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
