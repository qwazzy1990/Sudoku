import sys 
import os 

class Solver:

    def __init__(self, matrix):
        self.matrix = matrix
    

    ##returns a sector of the matrix given the row and column
    ##corresponding to that sector. Sectors are numbered left to right, top down. Sector 1 is in top left
    ##and sector 9 is bottom right
    def getSector(self, row, col)->list:
        sector = []
        

        ##if curr square is in first sector, copy the first sector
        if row >= 0 and row <= 2 and col >= 0 and col <= 2:
            self.copySector(sector, 0, 0)

        ##secnd sector
        if row >=0 and row <=2 and col >=3 and col <=5:
            self.copySector(sector, 0, 3)
        
        ##third sector
        if row >= 0 and row <= 2 and col >= 6 and col <= 8:
            self.copySector(sector, 0, 6)
        
        ##fourth sectir 
        if row >= 3 and row <=5 and col >= 0 and col <= 2:
            self.copySector(sector, 3, 0)

        ##fifth sector
        if row >= 3 and row <= 5 and col >= 3 and col <=5:
            self.copySector(sector, 3, 3)
        
        ##sixth sector
        if row >= 3 and row <= 5 and col >=6 and col <= 8:
            self.copySector(sector, 3, 6)

        ##seventh sector
        if row >= 6 and row <= 8 and col >= 0 and col <= 2:
            self.copySector(sector, 6, 0)
        
        ##eigth sector
        if row >= 6 and row <= 8 and col >= 3 and col <= 5:
            self.copySector(sector, 6, 3)
        
        #ninth sector
        if row >= 6 and row <=8 and col >=6 and col <= 8:
            self.copySector(sector, 6, 6)
        

        return sector

    ##copiers
    def copySector(self, sector, row, col):

        for i in range(row, row+3):
            temp = []
            for j in range(col, col+3):
                temp.append(self.matrix[i][j])

            sector.append(temp)


    #To string/printers
    def toString(self):
        s = ""
        for i in range(0, 9):
            s += str(self.matrix[i])
            s+="\n"
        
        return s

    def sectorToString(self, sector):
        s = ""
        for i in range (0, 3):
            for j in range(0, 3):
                s+= str(sector[i][j])
                s+=" "
            s+="\n"
        return s
    
    ##validators

    ##checks if val is in the current row or not.
    ##if not then return true, else return false
    def canBeAddedToRow(self, val, row)->bool:
        for i in range(0, 9):
            if self.matrix[row][i] == val:
                return False
        
        return True
    
    ##checks if val is in the current col or not.
    ##if not then return true, else return false
    def canBeAddedToCol(self, val, col)->bool:
        for i in range(0, 9):
            if self.matrix[i][col] == val:
                return False
        
        return True 

    def canBeAddedToSector(self, val, sector)->bool:
        for i in range(0, 3):
            for j in range(0, 3):
                if sector[i][j] == val:
                    return False
        
        return True
    
    ##checks if the val can be added by checking if 
    ##the val can be added to the row, col and sector
    def canBeAdded(self, val, row, col, sector)->bool:
        if self.canBeAddedToRow(val, row) == True and self.canBeAddedToCol(val, col) == True and self.canBeAddedToSector(val, sector) == True:
            return True

        return False 

    def isComplete(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.matrix[i][j] == 0:
                    return False
        return True
    ##the back tracking algorithm for solving the sudoku
    def driver(self)->bool:
        
        if self.isComplete():
            print(self.toString())
            return True
        
        for i in range(0, 9):
            for j in range(0, 9):
                ##if the matrix at that cell is empty then
                if self.matrix[i][j] == 0:
                    #for values 1 to 9 check if the value can be added-
                    for k in range(1, 10):
                        if self.canBeAdded(k, i, j, self.getSector(i, j)):
                            self.matrix[i][j] = k
                            if self.driver()==True:
                                return True
                            else:
                                self.matrix[i][j] = 0
                    #endfor
                    return False
                

