class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def sit(self):
        print(f'the{self.name} is sitting down')

    def lying(self ):
        print(f'the {self.name} is lying down')




my_dog= Dog('Jack',3)


print(f'my name is {my_dog.name}')