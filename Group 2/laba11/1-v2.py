class Pasport: 
# Конструктор 
    def __init__(self,FIO,Sir,Num): 
        self.FIO=FIO 
        self.Sir=Sir 
        self.Num=Num 
    def return_shoy(self): 
        print("ФИО:""\n"+self.FIO) 
        print("Серия:""\n"+self.Sir) 
        print("Номер:""\n"+self.Num) 
        print("------------------------------------") 
 
    def __del__(self): 
        print("Объект удален:") 
Use=Pasport("Данила Чикатило","2342342ddfsdf","1234567") 
Use.return_shoy() 
Use.FIO="FJINJE" 
Use.Sir="123" 
Use.Num="56478392" 
Use.return_shoy()