from PyQt6.QtWidgets import QPushButton

class Game:
    
    def __init__(self, lsBtn=[QPushButton]) -> None:
        self.btns = lsBtn
    
    def __check_wins(self,a:QPushButton, b:QPushButton, c:QPushButton):
        ans = a.text() + b.text() + c.text()
        if ans.lower() =="ooo":
            return 'O'
        elif ans.lower() =='xxx':
            return 'X'
        else:
            return None
    
    #Qatorlarni tekshirish
    def __check_rows(self):
        ans = self.__check_wins(self.btns[0], self.btns[1], self.btns[2])
        if ans != None:
            return ans
        ans = self.__check_wins(self.btns[3], self.btns[4], self.btns[5])
        if ans != None:
            return ans
        ans = self.__check_wins(self.btns[6], self.btns[7], self.btns[8])
        if ans != None:
            return ans
        return None
    #Ustunlarni tekshirish
    def __check_cols(self):
        ans = self.__check_wins(self.btns[0], self.btns[3], self.btns[6])
        if ans != None:
            return ans
        ans = self.__check_wins(self.btns[1], self.btns[4], self.btns[7])
        if ans != None:
            return ans
        ans = self.__check_wins(self.btns[2], self.btns[5], self.btns[8])
        if ans != None:
            return ans
        return None
    
    #Diagonalni 
    def __check_diagonals(self):
        ans = self.__check_wins(self.btns[0], self.btns[4], self.btns[8])
        if ans != None:
            return ans
        ans = self.__check_wins(self.btns[2], self.btns[4], self.btns[6])
        if ans != None:
            return ans
        return None
    
    def check(self):
        ans = self.__check_rows()
        if ans != None:
            return ans
        ans = self.__check_cols()
        if ans != None:
            return ans
        ans = self.__check_diagonals()
        if ans != None:
            return ans
        return None