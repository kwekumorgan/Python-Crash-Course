#
cars=["toyota supra","aventador","lambourghini","bmw m5","Range Rover"]

for car in cars:
    if car.lower()=="bmw m5":
        print(car.upper())
    else:
        print(car.lower())


# CONDITIONAL TESTS

requested_toppings=["Onion","mushrooms","Pineapple"]
 




car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

upper_car= car.upper()

print("Is car == SUBARU? " )

print(upper_car==car.lower())




#Task 1
kwame_age=24
afia_age=32


if (kwame_age<=36) and (afia_age<40):
    print("Both Afia and Kwame are in range ")


name_person1="James ward "
name_person2="Fifii Prat"


if name_person1=="James ward " or name_person2=="jungle":
    print("We found one of them ")


if "Onion" in requested_toppings:
    print("Confirmed Onion is part of the ingredient ")


if "Banana" not in requested_toppings:
    print("Banana is not in the ingredient")



#Task 2
alien_colour= "green"


if (alien_colour=="green"):
    print("You earned 5 points")

else:
    print(" you earned 10 points")




# Task 3 
alien_colour="yellow"

if (alien_colour=="green"):
    print("You earned 5 points!")
elif (alien_colour=="yellow"):
    print("You earned 10 points!")
elif (alien_colour=="red"):
    print("You earned 15 points!")




person_age=90


if (person_age<2):
    print("The person is a baby")
elif ( person_age >=2) and (person_age<4):
    print("The person is a toddler")
elif (person_age>=4) and (person_age<13):
    print("The person is a kid")
    

elif (person_age>=13) and (person_age<20):
    print("The person is a teenager")

elif (person_age>=20) and (person_age<65):
    print("The person is an adult")

elif (person_age>=65):
    print("The person is an elder")




favourite_fruit=["apple","pineapple","orange","strawberry","coconut"]

if "coconut" in favourite_fruit:
    print("You really like coconut")

if "apple" in favourite_fruit:
    print("You really like apple")


if "pineapple" in favourite_fruit:
    print("You really like pineapple")


if "tangerine" in favourite_fruit:
    print("You really like coconut")


if "banana" in favourite_fruit:
    print("You really like coconut")