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

