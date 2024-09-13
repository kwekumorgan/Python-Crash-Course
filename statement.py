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