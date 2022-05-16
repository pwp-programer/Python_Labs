import time
import random




# Базовый класс 1 уровня
class base():
    def __init__(self, damage=10, defends=5, health=50, player="Воин"):
        self.damage, self.defends, self.health = damage, defends, health
        self.name = input("Введите имя персонажа: \n")


    def write_info_about_your_hero(self, name=""):
            self.player = input("Выберите свой класс:\nВоин, Чародей, Знахарь\n")

            if self.player == "1" or self.player == "Воин":
                self.player = "Воин"

            elif self.player == "2" or self.player == "Чародей":
                self.player = "Чародей"

            else:
                self.player = "Знахарь"

            print(f"Ваш класс: {self.player}")
            print(self.name)


    def show_statistic_about_hero(self, damage=1, defends=1, health=1):
        print(f'''
Характеристики вашего персонажа:
{self.damage} - урона
{self.defends} - брони
{self. health} - здоровья
''')


    def return_class_info(self):
        return self.player

    def error_update(self):
        print("Некорректный ввод. Произошла отмена улучшения")



# Дочерний класс 1 уровня
class mage(base):
    def __init__(self, damage=10, defends=5, health=50, player="Воин"):
        self.damage, self.defends, self.health = damage, defends, health

    def info(self):
        print("Вы выбрали класс мага")


    def change_base_class(self, damage=1, defends=1, health=1, name="Bogdan"):
        print("Ваш урон увеличен:")
        self.damage *= 1.2
        print(self.damage)
        base.show_statistic_about_hero(self)

        value = input("Вы хотите улучшить вашего персонажа: ")
        if value == "y" or value == "Y" or value == "Да" or value == "да" or value == "1":
            improved_base.__init__(self)
            improved_base.show_statistic_about_hero(self)
            improved_base.choosing_element(self)


            improved_mage.__init__(self)
            improved_mage.upgrade_skills(self)
            improved_mage.show_statistic_about_hero(self)

        else:
            base.error_update(self)



# Дочерний класс 1 уровня
class warrior(base):
    def __init__(self, damage=10, defends=5, health=50, player="Воин"):
        self.damage, self.defends, self.health = damage, defends, health

    def info(self):
        print("Вы выбрали класс Воин")


    def change_base_class(self, damage=1, defends=1, health=1, name="Bogdan"):
        print(f"Количество очков здоровья увеличено с {self.health} ", end="")
        self.health *= 1.5
        print(f"до {self.health}")
        base.show_statistic_about_hero(self)

        value = input("Вы хотите улучшить вашего персонажа: ")
        if value == "y" or value == "Y" or value == "Да" or value == "да" or value == "1":
            improved_base.__init__(self)
            improved_base.show_statistic_about_hero(self)
            improved_base.choosing_element(self)


            improved_warrior.__init__(self)
            improved_warrior.upgrade_skills(self)
            improved_warrior.show_statistic_about_hero(self)

        else:
            base.error_update(self)



# Дочерний класс 1 уровня
class medicine_man(base):
    def __init__(self, damage=10, defends=5, health=50, player="Воин"):
        self.damage, self.defends, self.health = damage, defends, health

    def info(self):
        print("Вы выбрали класс Знахарь")


    def change_base_class(self, damage=1, defends=1, health=1):
        print(f"Количество очков защиты увеличено с {self.defends} ", end="")
        self.defends *= 1.1
        print(f"до {self.defends}")
        base.show_statistic_about_hero(self)

        value = input("Вы хотите улучшить вашего персонажа: ")
        if value == "y" or value == "Y" or value == "Да" or value == "да" or value == "1":
            improved_base.__init__(self)
            improved_base.show_statistic_about_hero(self)
            improved_base.choosing_element(self)


            improved_medicine_man.__init__(self)
            improved_medicine_man.upgrade_skills(self)
            improved_medicine_man.show_statistic_about_hero(self)

        else:
            base.error_update(self)




# Дочерний класс 2 уровня
class improved_base(base):
    def __init__(self, damage=25, defends=20, health=100, critical_damage=0.1, miss=0.2, player="", element=""):
        self.damage, self.defends, self.health, self.critical_damage, self.miss = damage, defends, health, critical_damage, miss


    def show_statistic_about_hero(self, damage=1, defends=1, health=1):
        print(f'''
Характеристики вашего персонажа:
{self.damage} - урона
{self.defends} - брони
{self. health} - здоровья
{self.critical_damage} - шанс критического урона
{self.miss} - шанс уклонения от атаки
''')


    def choosing_element(self, element=""):
        print("Возможные стихии: Каменная, Воздушная, Огненная, Водная")
        element = input("Выберите стихию: ")
        self.element = element


    def returner_element(self):
        return self.element

    def enemy_creation(self, class_enemy_value):
        value = input("Вы хотите начать бой?\n").lower()
        if value == "1" or value == "y" or value == "да":
            for i in range(3):
                print(f"Бой начинается через {i+1}")
                time.sleep(1)
            list_random_value = [1, 2, 3, 4]
            random_value = random.choice(list_random_value)
            if random_value == 1:
                class_enemy_value = "воин"

            elif random_value == 2:
                class_enemy_value = "чародеев"

            elif random_value == 3:
                class_enemy_value = "знахарей"

            print(f"Ваш противник принадлежит к классу {class_enemy_value}")

        else:
            print("Вы сбежали с поля боя...")


    def fight(self):
        pass





# Дочерний класс 3 уровня
class improved_mage(improved_base):
    def __init__(self, damage=30, defends=20, health=100, critical_damage=0.1, miss=0.2, absorption = 0,player=""):
        self.damage, self.defends, self.health, self.critical_damage, self.miss, self.vampirism = damage, defends, health, critical_damage, miss, absorption


    def upgrade_skills(self):
        if improved_base.returner_element(self) == "Каменная" or improved_base.returner_element(self) == "1":
            self.health = 125
            print(f"Количество здоровья после улучшения: {self.health}")

        elif improved_base.returner_element(self) == "Воздушная" or improved_base.returner_element(self) == "2":
            self.miss = 0.4
            print(f"Шанс уклонения после улучшения: {self.miss}")

        elif improved_base.returner_element(self) == "Огненная" or improved_base.returner_element(self) == "3":
            self.damage = 50
            print(f"Урон после улучшения: {self.damage}")

        else:
            self.vampirism = 0.2
            print(f"Шанс вампризима после улучшения: {self.vampirism}")

    def show_statistic_about_hero(self):
        print(f'''
Характеристики вашего персонажа:
{self.damage} - урона
{self.defends} - брони
{self. health} - здоровья
{self.critical_damage} - шанс критического урона
{self.miss} - шанс уклонения от атаки
{self.vampirism} - шанс восстановить здоровье нанеся урон
''')
        improved_base.enemy_creation(self, "воин")




# Дочерний класс 3 уровня
class improved_warrior(improved_base):
    def __init__(self, damage=25, defends=20, health=150, critical_damage=0.1, miss=0.2, absorption = 0,player=""):
        self.damage, self.defends, self.health, self.critical_damage, self.miss, self.vampirism = damage, defends, health, critical_damage, miss, absorption


    def upgrade_skills(self):
        if improved_base.returner_element(self) == "Каменная" or improved_base.returner_element(self) == "1":
            self.health = 125
            print(f"Количество здоровья после улучшения: {self.health}")

        elif improved_base.returner_element(self) == "Воздушная" or improved_base.returner_element(self) == "2":
            self.critical_damage = 0.4
            print(f"Шанс критической атаки после улучшения: {self.critical_damage}")

        elif improved_base.returner_element(self) == "Огненная" or improved_base.returner_element(self) == "3":
            self.damage = 50
            print(f"Урон после улучшения: {self.damage}")

        else:
            self.vampirism = 0.2
            print(f"Шанс вампризима после улучшения: {self.vampirism}")

    def show_statistic_about_hero(self):
        print(f'''
Характеристики вашего персонажа:
{self.damage} - урона
{self.defends} - брони
{self. health} - здоровья
{self.critical_damage} - шанс критического урона
{self.miss} - шанс уклонения от атаки
{self.vampirism} - шанс восстановить здоровье нанеся урон
''')
        improved_base.enemy_creation(self, "воин")




# Дочерний класс 3 уровня
class improved_medicine_man(improved_base):
    def __init__(self, damage=25, defends=20, health=150, critical_damage=0.1, miss=0.2, absorption = 0,player=""):
        self.damage, self.defends, self.health, self.critical_damage, self.miss, self.vampirism = damage, defends, health, critical_damage, miss, absorption


    def upgrade_skills(self):
        if improved_base.returner_element(self) == "Каменная" or improved_base.returner_element(self) == "1":
            self.health = 125
            print(f"Количество здоровья после улучшения: {self.health}")

        elif improved_base.returner_element(self) == "Воздушная" or improved_base.returner_element(self) == "2":
            self.critical_damage = 0.4
            print(f"Шанс критической атаки после улучшения: {self.critical_damage}")

        elif improved_base.returner_element(self) == "Огненная" or improved_base.returner_element(self) == "3":
            self.damage = 50
            print(f"Урон после улучшения: {self.damage}")

        else:
            self.vampirism = 0.2
            print(f"Шанс вампризима после улучшения: {self.vampirism}")

    def show_statistic_about_hero(self):
        print(f'''
Характеристики вашего персонажа:
{self.damage} - урона
{self.defends} - брони
{self. health} - здоровья
{self.critical_damage} - шанс критического урона
{self.miss} - шанс уклонения от атаки
{self.vampirism} - шанс восстановить здоровье нанеся урон
''')
        improved_base.enemy_creation(self, "воин")




# Вызов базового класса
use = base()
use.write_info_about_your_hero()
use.show_statistic_about_hero()


# Вызов подклассов
if use.return_class_info() == "Воин":
    use1 = warrior()
    use1.info()
    use1.change_base_class()


elif use.return_class_info() == "Чародей":
    use2 = mage()
    use2.info()
    use2.change_base_class()

else:
    use3 = medicine_man()
    use3.info()
    use3.change_base_class()
