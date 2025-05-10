class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def sit(self):
        print(f'{self.name} is sitting down')

    def lying(self ):
        print(f' {self.name} is lying down')




my_dog= Dog('Jack',3)


print(f'my name is {my_dog.name}')


my_dog.sit()



# try work


class restaurant:
    def __init__(self,restaurant_name,restaurant_cuisine_type):
        self.restaurant_name = restaurant_name
        self.restaurant_cuisine_type = restaurant_cuisine_type

    def describe_restaurant():
        print('This restaurant is an Italian based restaurant')

    def open_restaurant():
        print('We open at 8Am everyday')




my_restaurant= restaurant('La famille','Fastfood') 
print(my_restaurant.restaurant_name)

