
# def fun_1(x):
#     x += 1
#     print("x =" , x)
#     return x

# def fun_2(y):
#     y += 1
#     print("y =" , y)
#     return fun_1(y)

# print(fun_2(4))


# def fun_3():
#     global num_1
#     num_1 = 4
#     print("fun_3 =", num_1)
# fun_3()
# print(num_1)


num_2 = 1
def fun_4():
    global num_2
    print("num_2 =" , num_2)
    num_2 +=1
    if(num_2 <= 10):
        return fun_4()

fun_4()