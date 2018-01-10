# -*- coding: utf-8 -*-

import random

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
board_long=14
class Model:
    speed = 5
    def __init__(self, lv = 5):
        self.speed = lv
        self.state = "IDLE"
        
    def Set_State(self, newState):
        if newState == "PLAY":
            self.state = "PLAY"
            
        elif newState == "IDLE":
            self.state = "IDLE"
            
        elif newState == "SET":
            self.state = "SET"
            
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
        self.falling_class =0
        
        self.board = (8,15)# x,y
        self.board_state = []#print mode
        self.frozen_board = []#frozen check
        self.point = 0
        
        #all board state
        size = 120
        for i in range(0,size):
            self.board_state.append(0)
            self.frozen_board.append(0)
            
        self.New_Block()
        
    def Turn(self):
        temp_Falling = list(self.falling_block) #複製原始block位置
        outCheck = True
        if self.falling_class == 10 :
            if(temp_Falling[0] % 8 == 6):
                outCheck = False              
            temp_Falling[1] = temp_Falling[1] - 7
            temp_Falling[2] = temp_Falling[2] - 2
            temp_Falling[3] = temp_Falling[3] - 9
            
            #檢查是否在冷凍版上
            for i in self.frozen_board: 
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False
                        
            #若沒有撞到frozen或是邊緣則可進行旋轉
            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i] #將假定值帶入
            
        
        elif self.falling_class == 11:
            temp_Falling[1] = temp_Falling[1] + 7
            temp_Falling[2] = temp_Falling[2] + 2
            temp_Falling[3] = temp_Falling[3] + 9
            
            
            for i in self.frozen_board: 
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class -= 1
                    self.falling_block[i] = temp_Falling[i] 
            
        elif self.falling_class == 20:
            if(temp_Falling[0] % 8 == 7):
                outCheck = False
            temp_Falling[0] = temp_Falling[0] - 1
            temp_Falling[1] = temp_Falling[1] - 7
            temp_Falling[3] = temp_Falling[3] - 6


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False
            
            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i] 

                        
        elif self.falling_class == 21:
            temp_Falling[0] = temp_Falling[0] + 1
            temp_Falling[1] = temp_Falling[1] + 7
            temp_Falling[3] = temp_Falling[3] + 6


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False
                    
                    
            if(outCheck):
                for i in range(4):
                    self.falling_class -= 1
                    self.falling_block[i] = temp_Falling[i] 


        elif self.falling_class == 30:
            temp_Falling[1] = temp_Falling[1] - 7
            temp_Falling[2] = temp_Falling[2] - 1
            temp_Falling[3] = temp_Falling[3] + 6


            for i in self.frozen_board: 
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i] 
            
            
        elif self.falling_class == 31:
            if(temp_Falling[0] % 8 == 0):
                outCheck = False
            temp_Falling[0] = temp_Falling[0] - 7
            temp_Falling[1] = temp_Falling[1] - 7
            temp_Falling[2] = temp_Falling[2] - 1
            temp_Falling[3] = temp_Falling[3] + 6


            for i in self.frozen_board: 
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i]
            return self.falling_block[i]

            
        elif self.falling_class == 32:
            temp_Falling[0] = temp_Falling[0] + 2
            temp_Falling[1] = temp_Falling[1] + 9
            temp_Falling[2] = temp_Falling[2] + 15
            temp_Falling[3] = temp_Falling[3] + 8


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i]
            

        elif self.falling_class == 33:
            if(temp_Falling[0] % 8 == 7):
                outCheck = False
            temp_Falling[0] = temp_Falling[0] - 1
            temp_Falling[1] = temp_Falling[1] + 1
            temp_Falling[2] = temp_Falling[2] + 7
            temp_Falling[3] = temp_Falling[3] - 7


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class -= 3
                    self.falling_block[i] = temp_Falling[i]

            
        elif self.falling_class == 40:
            temp_Falling[0] = temp_Falling[0] - 1
            temp_Falling[1] = temp_Falling[1] + 1
            temp_Falling[2] = temp_Falling[2] + 8
            temp_Falling[3] = temp_Falling[3] + 8


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i]
            

        elif self.falling_class == 41:
            if(temp_Falling[0] % 8 == 6):
                outCheck = False
            temp_Falling[1] = temp_Falling[1] - 7
            temp_Falling[2] = temp_Falling[2] - 14
            temp_Falling[3] = temp_Falling[3] - 9


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i]

            
        elif self.falling_class == 42:
            temp_Falling[2] = temp_Falling[2] + 7
            temp_Falling[3] = temp_Falling[3] + 9


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i]
            

        elif self.falling_class == 43:
            if(temp_Falling[0] % 8 == 0):
                outCheck = False
            temp_Falling[0] = temp_Falling[0] + 1
            temp_Falling[1] = temp_Falling[1] - 6
            temp_Falling[2] = temp_Falling[2] - 1
            temp_Falling[3] = temp_Falling[3] - 8


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class -= 3
                    self.falling_block[i] = temp_Falling[i]

            
        elif self.falling_class == 50:
            temp_Falling[1] = temp_Falling[1] + 7
            temp_Falling[2] = temp_Falling[2] + 7
            temp_Falling[3] = temp_Falling[3] + 7


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i]

            
        elif self.falling_class == 51:
            if(temp_Falling[0] % 8 == 1):
                outCheck = False
            elif(temp_Falling[0] % 8 == 0):
                outCheck = False
            temp_Falling[0] = temp_Falling[0] + 1
            temp_Falling[3] = temp_Falling[3] + 1


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i]
            
            
        elif self.falling_class == 52:
            temp_Falling[0] = temp_Falling[0] - 1
            temp_Falling[1] = temp_Falling[1] - 1
            temp_Falling[2] = temp_Falling[2] - 1
            temp_Falling[3] = temp_Falling[3] - 8


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i]


        elif self.falling_class == 53:
            if(temp_Falling[0] % 8 == 6):
                outCheck = False
            elif(temp_Falling[0] % 8 == 7):
                outCheck = False
            temp_Falling[1] = temp_Falling[1] - 6
            temp_Falling[2] = temp_Falling[2] - 6


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i] 

        
        elif self.falling_class == 70:
            if(temp_Falling[0] % 8 == 0):
                outCheck = False
            elif(temp_Falling[0] % 8 == 6):
                outCheck = False
            elif(temp_Falling[0] % 8 == 7):
                outCheck = False

            temp_Falling[0] = temp_Falling[0] - 1
            temp_Falling[1] = temp_Falling[1] - 8
            temp_Falling[2] = temp_Falling[2] - 15
            temp_Falling[3] = temp_Falling[3] - 22


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class += 1
                    self.falling_block[i] = temp_Falling[i]
            

        elif self.falling_class == 71:
            temp_Falling[0] = temp_Falling[0] + 1
            temp_Falling[1] = temp_Falling[1] + 8
            temp_Falling[2] = temp_Falling[2] + 15
            temp_Falling[3] = temp_Falling[3] + 22


            for i in self.frozen_board:
                for j in temp_Falling:
                    if(j == i):
                        outCheck = False
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                for i in range(4):
                    self.falling_class -= 1
                    self.falling_block[i] = temp_Falling[i] 
            
    def Move(self, lorr):
        print(self.board_state)
        tmp = []
        
        if lorr == 1:#right
        #check hit
            for x in self.falling_block:
                var = x + 1
                place = var % 8
                if place == 0:
                    return True#hit boarder, do nothing 
                else:
                    tmp.append(var)                
                    
        elif lorr == -1:#left
            #check hit
            for x in self.falling_block:
                var = x - 1
                place = var % 8
                if place == 7:
                    return True#hit boarder, do nothing
                else:
                    tmp.append(var)
                    
                    
        if self.Check_Frozen(tmp):#T hit, F not hit
            self.board_state = self.frozen_board[:]#not hit
                
        else:#not hit, add frozen and falling into board
            self.board_state = self.frozen_board[:]
                
            self.falling_block = tmp
            state = int(self.falling_class / 10)
            for blc in self.falling_block:
                self.board_state[blc] = state
        print(self.board_state)
            
    def Check_Frozen(self, temp):
        flag = False
        for i in temp:
            try:
                #hit block
                if self.frozen_board[i] != 0:
                    flag = True
                    break
            #hit boarder
            except:
                flag = True
                break
        if flag:
            state = int(self.falling_class / 10)
            for blc in self.falling_block:
                self.frozen_board[blc] = state
            return True
        
        else:
            return False
    
               
    def Check_Erase(self):
        chk_rowStart = []
        for block in self.falling_block:
            x = block % 8
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
            temp_board = self.frozen_board[:]
            for rowX in erase_row:
                i = 0
                while i < rowX:
                    temp_board[i + 8] = temp_board[i]


        if len(erase_row) == 1:
            self.point += 10
        elif len(erase_row) == 2:
            self.point += 30
        elif len(erase_row) == 3:
            self.point += 70
        elif len(erase_row) == 4:
            self.point += 150
        else:
            return

    def New_Block(self):
        self.falling_class = random.choice([10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43, 50, 51, 52, 53, 60, 70, 71])
        self.falling_block.clear()
        self.falling_block = brick_dict[self.falling_class]
        
        for i in self.falling_block:
            if not (self.frozen_board[i] == 0):# die
                return False
            
        state = int(self.falling_class / 10)
        for x in self.falling_block:
            self.board_state[x] = state#print something exist
        return True
            
    
    def Fall_Down(self):
        print(self.board_state)
        temp = []#next place
        temp.append(self.falling_block[0] + 8)
        temp.append(self.falling_block[1] + 8)
        temp.append(self.falling_block[2] + 8)
        temp.append(self.falling_block[3] + 8)
        
        #hit
        if self.Check_Frozen(temp):#T hit , F not hit
            #self.Check_Erase()
            self.board_state = self.frozen_board[:]
            return self.New_Block()
        
        #not hit
        else:
            #delete privious falling block, add frozen
            self.board_state = self.frozen_board[:]
            
            #move down    
            self.falling_block = temp
            state = int(self.falling_class / 10)
            for i in self.falling_block:
                self.board_state[i] = state#print something exist
            return True
