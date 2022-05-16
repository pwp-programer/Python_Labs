class worker:
    def info(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"ФИО: \n{self.FIO} \nДолжность: {self.position} \nЗаработная плата: {self.the_salary}\nСтаж: {self.internship}")


    def __init__(self, FIO="Воробьёв Яромир Алексеевич",position="Сотрудник",the_salary="123", internship="1"):
        self.FIO, self.position, self.the_salary, self.internship = FIO, position, the_salary, internship
        self.info()

    def __del__(self, text=""):
        print(f"{text}")

use = worker("Лихачёв Руслан Ярославович", "Грузчик", "100", "3")
use.FIO = "Rjpdsf"
use("Козлов Харитон Фёдорович")
use.__del__("delete")
