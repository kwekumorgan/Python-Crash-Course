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



username=["admin","user1","user2","user3","user4","user5"]

if username:
    for user in username:
        if user=="admin":
            print(f"Hello {user}, would like to see youtr status report")
        else:
            print(f"hello {user}, thank you for logging in again")
else:
    print("We have some present users")



current_users=["username1","Username2","username3","username4","username5"]

new_users=["username6","username2","username7","username8","username5"]


for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} already exist, use a diffirent username")
    else:
        print(f"{new_user} is available")
        