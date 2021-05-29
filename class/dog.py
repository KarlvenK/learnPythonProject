class Dog():
    #__init__ 中的self必须在形参最前面，且无需我们传递
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = 'unknow'
    
    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over")

    def show_his_type(self):
        print()

my_dog = Dog('tom\'s friend', 6)

print("my dog " + my_dog.name + " is " + str(my_dog.age) + " years old")

my_dog.sit()
my_dog.roll_over()

print(my_dog.type)