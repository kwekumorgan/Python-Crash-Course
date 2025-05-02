#passing information into function 
def greet_user(username):
    print(f'hello,{username}')

greet_user('kwame')


#TRY WORK

def display_message():
    print("parameter is the variable in a defined function and argument is the value of the variable that is passed into function ")

display_message()

def favourite_book(title,producer):
    print(f"My favourite book is {title.title()} is from {producer}")

favourite_book(producer="Sony Pictures",title='Lion king',)



#Default value 

def favourite_movie(name,company=''):
    print(f'{name} is my favourite movie is by {company}')


favourite_movie(name="spider:Homecoming")


#TRY Work 2

def make_shirt(size,message):
    print(f'This shirt wants {message} printed on it and the shirt size should be {size}')

make_shirt("large","'Be the change you want to see in the world!'")

make_shirt(size='medium',message="'Have some faith, papi!'")



def make_shirts(message,size="large",):
    print(f'This shirt wants {message} printed on it and the shirt size should be {size}')


make_shirts(message="If you're playing me, I will kill you!")
make_shirts(size="small",message="If you save everyone, who saves you")


def describe_city(city='', country=''):
    print(f"{city.title()} is in {country.title()}")

describe_city("tema","Ghana")
describe_city("New York city","united states of america")
describe_city("Nairobi","Kenya")



#RETURNING VALUES
def student_name(first_name,last_name):
    St_name= f"My full name is {first_name.title()} {last_name.title()}"
    return St_name


student_rollcall= student_name('Godwin', 'Morgan')


print(student_rollcall)


#Returning Dictionaries

def build_person(first_name,last_name,Age:None):
    person={'first':first_name,'last':last_name}
    if Age:
        person['Age']= Age
    return person["Age"]



musician= build_person("james","bond",5)

print(musician)



#Using function with whileloop          
while True:
    print("I you want to quit enter 'q'")
    
    lname=input("What is your last name?")
    if lname=="q":
        break
    fname=input("what is your first name?")
    if fname=="q":
        break
    identification= student_name(first_name=fname,last_name=lname)
    print(identification)
    

#Try Work 2

def city_country(city,country):

    location=f'city,country'
    return location.title()

city_country(city="real madrid",country='Espanyol')
city_country(city="Accra",country='Ghana')
city_country(city="Monaco",country='Italy') 


def make_album(artist_name,album_name,songs:None):
    person={'artist name':artist_name, 'album name':album_name}
    if songs:
        person['songs']=songs
    return person

album_info=make_album('Sarkodie','Mary',5)
print(album_info)

album_info_2=make_album('King promise','Five Star',5)
print(album_info_2)



while True:
    print("enter 'q' to quit:")
    artist_name= input("Enter Artist name?")
    if artist_name=='q':
        break

    album_name= input('Enter album name?')
    if  album_name=='q':
        break

    songs=int(input('Enter number of songs on the album?'))
    new_album=make_album(artist_name,album_name,songs)
    print(new_album)