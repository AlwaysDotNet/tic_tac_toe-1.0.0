from PyQt6.QtWidgets import QPushButton

class Game:
    
    def __init__(self, btns=[QPushButton]) -> None:
        self.btn_list = btns
    
    def __check(self,a:QPushButton, b:QPushButton, c:QPushButton):
        txt = a.text() + b.text() + c.text()
        txt = txt.lower()
        if txt == 'xxx':
            return 'x'
        elif txt == 'ooo':
            return 'o'
        return False
    
    def __check_rows(self):
        ans = self.__check(self.btn_list[0], self.btn_list[1], self.btn_list[2])
        if ans != False:
            return ans
        ans = self.__check(self.btn_list[3], self.btn_list[4], self.btn_list[5])
        if ans != False:
            return ans
        ans = self.__check(self.btn_list[6], self.btn_list[7], self.btn_list[8])
        if ans != False:
            return ans
        return False
    
    def __check_cols(self):
        ans = self.__check(self.btn_list[0], self.btn_list[3], self.btn_list[6])
        if ans != False:
            return ans
        ans = self.__check(self.btn_list[1], self.btn_list[4], self.btn_list[7])
        if ans != False:
            return ans
        ans = self.__check(self.btn_list[2], self.btn_list[5], self.btn_list[8])
        if ans != False:
            return ans
        return False
    
    def __check_diagonals(self):
        ans = self.__check(self.btn_list[0], self.btn_list[4], self.btn_list[8])
        if ans != False:
            return ans
        ans = self.__check(self.btn_list[2], self.btn_list[4], self.btn_list[6])
        if ans != False:
            return ans
        return False
    
    def check_all(self):
        ans = self.__check_rows()
        if ans != False:
            return ans
        ans = self.__check_cols()
        if ans != False:
            return ans
        ans = self.__check_diagonals()
        if ans != False:
            return ans
        return False
    
        