def fun_1():
    print("hello")
    print("hello2")
    print("hello3")

# print("hi 1")
# fun_1()
# print("hi 2")



# def fun_2():
#     print("start fun 2")
#     return 9

# num_1 = fun_2() +1
# print(num_1)



# num_2_global = 5
# def fun_3():
#     print("start fun 3")
#     print(num_2_global)
#     return num_2_global + 9

# print(fun_3())



# num_3_global = 5
# def fun_4():
#     print("start fun 4")
#     # num_3_global = 0
#     print(num_3_global)
#     return num_3_global + 9

# print("num_3_global =", num_3_global)
# print(fun_4())
# print("num_3_global =", num_3_global)
    


# def fun_5():
#     print("start fun 5")
#     num_4_local = 1
#     print(num_4_local)
#     return num_4_local + 9

# print(fun_5())
## print("num_4_local =", num_4_local)



# def fun_6(num):
#     print("num =" , num)
#     return num * 3

# print(fun_6(4))



# def fun_7(x , y):
#     return x * y

# print(fun_7(4 , 9))



# def fun_8(x = 5):
#     return x + 3.7

# print(fun_8(10))



# def fun_9(x , y , z = 5):
#     print("x = ",x)
#     print("y = ",y)
#     print("z = ",z)
#     return x * y * z

# print(fun_9(10 , 3))



# def fun_10():
#     print("start fun 10")
#     fun_1()

# fun_10()



# def fun_11():
#     def fun_local():
#         print("start fun_local")
#     print("start fun 11")
#     fun_local()


# fun_11()



# num_4_global = 1
# def fun_12():
#     global num_4_global
#     num_4_global = 5
#     return num_4_global * 4

# print(fun_12())
# print(num_4_global)
    



num_4_global = 1
def fun_12():
    num_4_global = 2
    def fun_local():
        num_4_global = 3
        print("fun_local() =" , num_4_global)
    fun_local()
    print("fun_12() =" , num_4_global)


fun_12()
print("num_4_global =" , num_4_global)



