prompt="if you tell us who you are we personalize the message you see."
prompt +="\nWhat is your name?"


name=input(prompt)
print(f"hello,{name}")






#Example1

car_rental=input("Which car will like to rent today?")
print(f"Let me see if I can get a {car_rental}!")


#Example2

number_guest= input("How many people are in your dinner table?")
number_guest= int(number_guest)

if number_guest <8:
    print ("Your dinner table is ready!")
else:
    print("You will have to wait a bit longer!")


#Example3

user_number=input("Input any between 0 and 100")
user_number= int(user_number)

user_number_check= user_number%10

if user_number==0:
    print(f"{user_number} is a multiple of 10")
else:
    print(f"{user_number} is not a multiple of 10")



