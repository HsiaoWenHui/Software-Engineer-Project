# -*- coding: utf-8 -*-

import random
import copy

# 定義磚塊.
brick_dict = {
        10: [3,11,12,20], 11: [3,4,10,11],   # N1.
        20: [4,11,12,19], 21: [3,4,12,13],   # N2.
        30: [3,11,12,13], 31: [3,4,11,19], 32: [2,3,4,12], 33: [4,12,19,20], # L1.
        40: [4,10,11,12], 41: [3,11,19,20], 42: [3,4,5,11], 43: [3,4,12,20], # L2.
        50: [4,11,12,13], 51: [4,12,13,20], 52: [11,12,13,20], 53: [4,11,12,20], # T.
        60: [3,4,11,12],    # O.
        70: [3,11,19,27], 71: [2,3,4,5]    #I.
}
board_long=14
class Model:
    speed = 5
    def __init__(self, lv = 5):
        self.speed = lv
        self.state = "IDLE"
        # Let controller call and change state
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
        #call parent's constructure
        super().__init__(lv)
        
        #store the type of falling block and its place
        self.falling_block = []
        self.falling_class =0
        
        #store the play ground, initial size to 8 * 15 and value for print initial to 0
        self.board = (8,15)# x,y
        self.board_state = []#print mode
        self.frozen_board = []#frozen check
        self.point = 0
        
        #all board state initial
        size = 120
        for i in range(0,size):
            self.board_state.append(0)
            self.frozen_board.append(0)
            
        #create first block 
        self.New_Block()
        
    def Turn(self):
        temp_Falling = copy.deepcopy(self.falling_block) #複製原始block位置
        outCheck = True
        #判斷型別
        if self.falling_class == 10 :
            #判斷無法旋轉的位置
            if(temp_Falling[0] % 8 == 0):
                outCheck = False
            #若可以旋轉的實際位置
            temp_Falling[1] = temp_Falling[1] - 7
            temp_Falling[2] = temp_Falling[2] - 2
            temp_Falling[3] = temp_Falling[3] - 9
            
            #檢查是否在冷凍版上
            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
                
            #如果小於零則無法改位置    
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                
            #檢查是否超出底線
            for i in temp_Falling:  
                if((i / 8) > board_long):
                    outCheck = False
                        
            #若沒有撞到frozen或是邊緣則可進行旋轉
            if(outCheck):
                #將板子跟冷凍版同步
                self.board_state = list(self.frozen_board)
                #將複製版複製回真實運作中的
                self.falling_block = list(temp_Falling)
                #算出是哪一種
                state = int(self.falling_class / 10)
                #把位置填上是哪一種型態
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist
                #改變板子編號
                self.falling_class += 1
            
            
        
        elif self.falling_class == 11:
            temp_Falling[1] = temp_Falling[1] + 7
            temp_Falling[2] = temp_Falling[2] + 2
            temp_Falling[3] = temp_Falling[3] + 9
            
            
            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
               
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist      
                self.falling_class -= 1           
        
        elif self.falling_class == 20:
            if(temp_Falling[0] % 8 == 7):
                outCheck = False
            temp_Falling[0] = temp_Falling[0] - 1
            temp_Falling[1] = temp_Falling[1] - 7
            temp_Falling[3] = temp_Falling[3] - 6


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False
            
            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class += 1
                        
        elif self.falling_class == 21:
            temp_Falling[0] = temp_Falling[0] + 1
            temp_Falling[1] = temp_Falling[1] + 7
            temp_Falling[3] = temp_Falling[3] + 6


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False
                    
                    
            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist   
                self.falling_class -= 1


        elif self.falling_class == 30:
            temp_Falling[1] = temp_Falling[1] - 7
            temp_Falling[2] = temp_Falling[2] - 1
            temp_Falling[3] = temp_Falling[3] + 6


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class += 1
            
            
        elif self.falling_class == 31:
            if(temp_Falling[0] % 8 == 0):
                outCheck = False
            temp_Falling[0] = temp_Falling[0] - 1
            temp_Falling[1] = temp_Falling[1] - 1
            temp_Falling[2] = temp_Falling[2] - 7
            temp_Falling[3] = temp_Falling[3] - 7


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False

            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class += 1

            
        elif self.falling_class == 32:
            temp_Falling[0] = temp_Falling[0] + 2
            temp_Falling[1] = temp_Falling[1] + 9
            temp_Falling[2] = temp_Falling[2] + 15
            temp_Falling[3] = temp_Falling[3] + 8


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False

            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class += 1
            

        elif self.falling_class == 33:
            if(temp_Falling[0] % 8 == 7):
                outCheck = False
            temp_Falling[0] = temp_Falling[0] - 1
            temp_Falling[1] = temp_Falling[1] - 1
            temp_Falling[2] = temp_Falling[2] - 7
            temp_Falling[3] = temp_Falling[3] - 7


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class -= 3

            
        elif self.falling_class == 40:
            temp_Falling[0] = temp_Falling[0] - 1
            temp_Falling[1] = temp_Falling[1] + 1
            temp_Falling[2] = temp_Falling[2] + 8
            temp_Falling[3] = temp_Falling[3] + 8


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False

            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist    
                self.falling_class += 1
            

        elif self.falling_class == 41:
            if(temp_Falling[0] % 8 == 6):
                outCheck = False
            temp_Falling[1] = temp_Falling[1] - 7
            temp_Falling[2] = temp_Falling[2] - 14
            temp_Falling[3] = temp_Falling[3] - 9


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class += 1
            
        
        elif self.falling_class == 42:
            temp_Falling[2] = temp_Falling[2] + 7
            temp_Falling[3] = temp_Falling[3] + 9


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class += 1
            

        elif self.falling_class == 43:
            if(temp_Falling[0] % 8 == 0):
                outCheck = False
            temp_Falling[0] = temp_Falling[0] + 1
            temp_Falling[1] = temp_Falling[1] + 6
            temp_Falling[2] = temp_Falling[2] - 1
            temp_Falling[3] = temp_Falling[3] - 8


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class -= 3

            
        elif self.falling_class == 50:
            temp_Falling[1] = temp_Falling[1] + 1
            temp_Falling[2] = temp_Falling[2] + 1
            temp_Falling[3] = temp_Falling[3] + 7

            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False

            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class += 1

            
        elif self.falling_class == 51:
            if(temp_Falling[0] % 8 == 0):
                outCheck = False
            temp_Falling[0] = temp_Falling[0] + 7


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False

            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist   
                self.falling_class += 1
            
            
        elif self.falling_class == 52:
            temp_Falling[0] = temp_Falling[0] - 7
            temp_Falling[1] = temp_Falling[1] - 1
            temp_Falling[2] = temp_Falling[2] - 1

            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist   
                self.falling_class += 1


        elif self.falling_class == 53:
            if(temp_Falling[0] % 8 == 7):
                outCheck = False
            temp_Falling[3] = temp_Falling[3] - 7

            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False


            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class -= 3

        
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


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
             
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                          
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False

            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class += 1
            

        elif self.falling_class == 71:
            temp_Falling[0] = temp_Falling[0] + 1
            temp_Falling[1] = temp_Falling[1] + 8
            temp_Falling[2] = temp_Falling[2] + 15
            temp_Falling[3] = temp_Falling[3] + 22


            if(self.frozen_board[temp_Falling[0]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[1]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[2]]>0):
                outCheck = False
            elif(self.frozen_board[temp_Falling[3]]>0):
                outCheck = False
            
            for i in range(4): 
                if(temp_Falling[i] < 0):
                    outCheck = False
                           
            for i in temp_Falling:
                if((i / 8) > board_long):
                    outCheck = False

            if(outCheck):
                self.board_state = list(self.frozen_board)
                self.falling_block = list(temp_Falling)
                state = int(self.falling_class / 10)
                for i in self.falling_block:
                    self.board_state[i] = state#print something exist  
                self.falling_class -= 1
                
                
    #call Move() to move block        
    def Move(self, lorr):
        # tmp store the place you'd like to move, and then we will check if it is ok or not
        tmp = []
        flag = False#flag to check if block hit or not
        
        if lorr == 1:#right
        #check hit
            for x in self.falling_block:
                var = x + 1#the place we check for block hit
                place = var % 8#the place we check for boarder hit
                if (place == 0) or (self.frozen_board[var] != 0):
                    flag = True
                    break#hit boarder or blocks, do nothing 
                else:
                    tmp.append(var)#add next place into tmp               
                    
        elif lorr == -1:#left
            #check hit
            for x in self.falling_block:
                var = x - 1
                place = var % 8
                if (place == 7) or (self.frozen_board[var] != 0):
                    flag = True
                    break#hit boarder, do nothing
                else:
                    tmp.append(var)
        else:
            return
                    
        if not flag:# not hit, so move it to next place
            self.falling_block = tmp
        self.board_state = self.frozen_board[:]#store frozen block into view board
        
        #add all falling block into view board
        state = int(self.falling_class / 10)
        for blc in self.falling_block:
            self.board_state[blc] = state
    
    #check if block frozen or not        
    def Check_Frozen(self, temp):
        flag = False#flag to check if the place is hitting(then the falling block need to frozen) or not
        for i in temp:
            try:
                #hit block
                if self.frozen_board[i] != 0:
                    flag = True
                    break
            #hit lower boarder
            except:
                flag = True
                break
        if flag:#hit and store falling block into frozen board
            state = int(self.falling_class / 10)
            for blc in self.falling_block:
                self.frozen_board[blc] = state
            return True
        
        else:
            return False
    
    #check if you got some row full and get points           
    def Check_Erase(self):
        erase_number = 0# number of row you erase
        erase_row_start = []#store row start
        temp_board = self.frozen_board[:]# store frozen into tmp to check erase
        state = int(self.falling_class / 10)
        for blc in self.falling_block:
            temp_board[blc] = state
            
        i = 0#row num
        flag = False
        for i in range(15):
            j = 0#col num
            flag = False
            for j in range(8):
                plc = i * 8 + j
                if temp_board[plc] == 0:
                    flag = True#empty board at row exist, then swap to next row to check
                    break
                
            #store erase row
            if not flag:
                erase_number += 1
                erase_row_start.append(i * 8)
        
        #type of erasing row        
        if erase_number == 1:
            s = erase_row_start[0]
            i = s - 1
            while i >= 0:#block swap down for different distance
                tmp = temp_board[i]
                temp_board[i + 8] = tmp
                i -= 1
            bu = 0
            while bu < 8:# add empty to top
                temp_board[bu] = 0
                bu += 1
            
            self.point += 10#add points
                
        elif erase_number == 2:
            s_1 = erase_row_start[1]
            s_0 = erase_row_start[0]
            
            i_0 = s_1 - 1
            i_1 = s_0 + 8
            i_2 = s_0 - 1
            
            while i_0 >= i_1:
                tmp = temp_board[i_0]
                temp_board[i_0 + 8] = tmp
                i_0 -= 1
            while i_2 >= 0:
                tmp = temp_board[i_2]
                temp_board[i_2 + 16] = tmp
                i_2 -= 1
            bu = 0
            while bu < 16:
                temp_board[bu] = 0
                bu += 1
                
            self.point += 30
                
        elif erase_number == 3:
            s_0 = erase_row_start[0]
            s_1 = erase_row_start[1]
            s_2 = erase_row_start[2]
            
            i_0 = s_2 - 1
            i_1 = s_1 + 8
            i_2 = s_1 - 1
            i_3 = s_0 + 8
            i_4 = s_0 - 1
            
            while i_0 >= i_1:
                tmp = temp_board[i_0]
                temp_board[i_0 + 8] = tmp
                i_0 -= 1
            while i_2 >= i_3:
                tmp = temp_board[i_2]
                temp_board[i_2 + 16] = tmp
                i_2 -= 1
            while i_4 >= 0:
                tmp = temp_board[i_4]
                temp_board[i_4 + 24] = tmp
                i_4 -= 1
            bu = 0
            while bu < 24:
                temp_board[bu] = 0
                bu += 1
                
            self.point += 70
                
        elif erase_number == 4:
            s_0 = erase_row_start[0]
            s_1 = erase_row_start[1]
            s_2 = erase_row_start[2]
            s_3 = erase_row_start[3]
            
            i_0 = s_3 - 1
            i_1 = s_2 + 8
            i_2 = s_2 - 1
            i_3 = s_1 + 8
            i_4 = s_1 - 1
            i_5 = s_0 + 8
            i_6 = s_0 - 1
            
            while i_0 >= i_1:
                tmp = temp_board[i_0]
                temp_board[i_0 + 8] = tmp
                i_0 -= 1
            while i_2 >= i_3:
                tmp = temp_board[i_2]
                temp_board[i_2 + 16] = tmp
                i_2 -= 1
            while i_4 >= i_5:
                tmp = temp_board[i_4]
                temp_board[i_4 + 24] = tmp
                i_4 -= 1
            while i_6 >= 0:
                tmp = temp_board[i_6]
                temp_board[i_6 + 32] = tmp
                i_6 -= 1
            bu = 0
            while bu < 32:
                temp_board[bu] = 0
                bu += 1
            
            self.point += 150
        else:
            return
        
        self.frozen_board = temp_board[:]# store the board after erased into frozen
    #new block initiate
    def New_Block(self):
        self.falling_class = random.choice([10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43, 50, 51, 52, 53, 60, 70, 71])
        self.falling_block = brick_dict[self.falling_class]
        
        for i in self.falling_block:
            if not (self.frozen_board[i] == 0):# create block and hit at the same time -> die
                return False
            
        state = int(self.falling_class / 10)
        for x in self.falling_block:
            self.board_state[x] = state#store into view board
        return True
            
    
    def Fall_Down(self):
        temp = []#next place
        temp.append(self.falling_block[0] + 8)
        temp.append(self.falling_block[1] + 8)
        temp.append(self.falling_block[2] + 8)
        temp.append(self.falling_block[3] + 8)
        
        #hit
        if self.Check_Frozen(temp):#check if next place would hit something or not, (T hit , F not hit)
            self.Check_Erase()# if we hit something, and then we need to check if some row is full or not
            self.board_state = self.frozen_board[:]#Only store the frozen board into view board, the falling is store into frozen exactly
            return self.New_Block()# call new block and check if you still alive or not
        
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
