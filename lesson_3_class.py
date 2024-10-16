class Dogs():
    def __init__(self , name_in):
        print("hello" , name_in)
        self.name = name_in
        print("self.name =", self.name)

        self.__privNum2 = 56

    def super_name(self):
        print("super name =", self.name)

    def name_3(self):
        self.name *= 3

    def new_num(self):
        self.num =50
        self.super_name()

    def get_privNum2(self):
        return self.__privNum2
    
        

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
