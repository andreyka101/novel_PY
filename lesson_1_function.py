# создание функции 
def fun_1():
    print("hello")
    print("hello2")
    print("hello3")

# вызов функции
# print("hi 1")
# fun_1()
# print("hi 2")



# функция возвращает значение
# def fun_2():
#     print("start fun 2")
#     return 9

# num_1 = fun_2() +1
# print(num_1)



# использование глобальной переменной
# num_2_global = 5
# def fun_3():
#     print("start fun 3")
#     print(num_2_global)
#     return num_2_global + 9

# print(fun_3())



# изменение глобальной переменной
num_3_global = 5
def fun_4():
    print("start fun 4")
    num_3_global = 0
    print(num_3_global)
    return num_3_global + 9

print("num_3_global =", num_3_global)
print(fun_4())
print("num_3_global =", num_3_global)
    


# создание локальной переменной
# def fun_5():
#     print("start fun 5")
#     num_4_local = 1
#     print(num_4_local)
#     return num_4_local + 9

# print(fun_5())
## print("num_4_local =", num_4_local)



# функция принимает значение
# def fun_6(num):
#     print("num =" , num)
#     return num * 3

# print(fun_6(4))



# функция принимает несколько значений
# def fun_7(x , y):
#     return x * y

# print(fun_7(4 , 9))



# значение по умолчанию
# def fun_8(x = 5):
#     return x + 3.7

# print(fun_8(10))



# функция принимает несколько значений с значением по умолчанию
# def fun_9(x , y , z = 5):
#     print("x = ",x)
#     print("y = ",y)
#     print("z = ",z)
#     return x * y * z

# print(fun_9(10 , 3))



# вызов функции в функции
# def fun_10():
#     print("start fun 10")
#     fun_1()

# fun_10()



# создание функция в функции
# def fun_11():
#     def fun_local():
#         print("start fun_local")
#     print("start fun 11")
#     fun_local()

# fun_11()



# глобальная переменная в функции
# num_4_global = 1
# def fun_12():
#     global num_4_global
#     num_4_global = 5
#     return num_4_global * 4

# print(fun_12())
# print(num_4_global)
    


# у каждой функции переменная имеет свой жизненный цикл 
# num_4_global = 1
# def fun_13():
#     num_4_global = 2
#     def fun_local():
#         num_4_global = 3
#         print("fun_local() =" , num_4_global)
#     fun_local()
#     print("fun_13() =" , num_4_global)

# fun_13()
# print("num_4_global =" , num_4_global)





# дз
# Задание 1. 
# Написать функцию, выводящую на экран 
# прямоугольник с высотой N и шириной K.

# Задание 2. 
# Написать функцию, вычисляющую факториал 
# переданного ей числа.

# Задание 3. 
# Написать функцию, которая проверяет, является ли переданное ей число простым? Число называется 
# простым, если оно делится без остатка только на себя 
# и на единицу.

# Задание 4. 
# Написать функцию, которая возвращает куб 
# числа.

# Задание 5. 
# Написать функцию для нахождения наибольшего из двух чисел.

# Задание 6. 
# Написать функцию, которая возвращает истину, если передаваемое значение положительное и ложь, 
# если отрицательное.


# обычное деление 
print("10 / 3 =" , 10 / 3)
# деление без остатка
print("10 // 3 =" , 10 // 3)
# остаток от деление
print("10 % 3 =" , 10 % 3)


