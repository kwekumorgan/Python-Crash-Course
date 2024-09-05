# A list bicycle that print out the item in uppercase
bicycles=["bmx","buzanga","Ponkoafaha"]
print(bicycles[-1].upper())

###using individual values from a list
info=f"Kwame owns a {bicycles[2].title()}"

print(info)




### try


#A list of name 
name=["Joshua","Sconi","Kyrie","Iris","Kiki"]

# takes name and print out a message
for i in range(len(name)):
    print(f'How are you doing {name[i]}')

# a list of cars
cars=["toyota supra","aventador","lambourghini","bmw m5","Range Rover"]

# message
message= "  will like to own a"

#  takes name and car and print out with the message 
for i in range(len(cars)):
    print(f'{name[i]} {message} {cars[i]}')



### Modifying List


# Intiliazed list
church_members=[]

# store user input
member_size=int(input("Enter member number size:"))

# store member's names 
for i in range(member_size):
    member_name=input("enter member name:")
    church_members.append(member_name)

# print stored member's name 
for j in range(len(church_members)):
    print(church_members[j])

# insert new item
new_cars=cars.insert(6,"honda")


# deleting item with index 2
del cars[2]

#removed a cars the last car item
popped_car=cars.pop() 

# deleted a name cars item
removed_car =cars.remove('Range Rover')
print(cars)
print(popped_car)
print(removed_car)



### Try 2
# names of guest
dinner_guest=["Joshua","Sconi","Kyrie","Iris","Kiki"]

#named guest removed
removed_guest= "Kiki"
dinner_guest.remove(removed_guest)
print(removed_guest)

# new guest name added
dinner_guest.append("Maame Sika")

# guest names printed with a message 
for i in range(len(dinner_guest)):
    print(f'Dear {dinner_guest[i]}, we have found a bigger table  ')

# new guest added
dinner_guest.insert(0,"Eugene")
dinner_guest.insert(3,"Caleb")
dinner_guest.append("Selina")
for i in range(len(dinner_guest)):
    print(f'Dear {dinner_guest[i]}, You are invited to the opening of the Morgan Corp car launch at Movenpick 4pm prompt ')

# initialized new list
reduced_guest=[""]

# some guest names removed
for y in range(len(dinner_guest)-2):
    reduced_guest=dinner_guest.pop()
    print(f'{reduced_guest}, We sorry for the inconvenience')



   
#remaining name output
for x in range(len(dinner_guest)):

    print(f'{dinner_guest[x]}, You are stil invited and make it on time ')




    ### Organising a list 

cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)






### Try work 3

location=["accra","jamestown","legon","cantoment","ada"]
tempo_sorted=sorted(location)

print(location)
tempo_sorted.reverse()
print(tempo_sorted)