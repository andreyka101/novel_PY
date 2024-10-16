# создание класса
class Dogs():
    # __init__ - срабатывает при вызове класса
    def __init__(self , name_in):
        print("hello" , name_in)
        создание переменной
        self.name = name_in
        print("self.name =", self.name)

        # приветная переменная
        self.__privNum2 = 56

    # создание метода
    def super_name(self):
        print("super name =", self.name)

    def name_3(self):
        self.name *= 3

    def new_num(self):
        self.num =50
        self.super_name()

    def get_privNum2(self):
        return self.__privNum2
    
        

# использование класса
dog_s1 = Dogs("fif")
print(dog_s1.name)
dog_s1.super_name()
# print(Dogs("opo").name)


dog_s1.name_3()
dog_s1.super_name()


print("*************")
dog_s1.new_num()
print(dog_s1.num)
dog_s1.num = 9
print(dog_s1.num)


dog_s1.__privNum2 = 5
print(dog_s1.__privNum2)
print(dog_s1.get_privNum2())



# номер 1
# Создать класс, описывающий автомобиль (производитель, 
# модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации об автомобиле.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# номер 2
# создать класс колькулятор 
# в конструкторе нужно в писать 2 числа
# создать 4 метода: умножение , деление , сумма , вычитание
# создать метод для добавления числа (его можно вызвать много раз и подучить много чисел)

# https://okpython.net/python/python_zadachnik/python_zadachnik.html#ex_13