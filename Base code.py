# from Printnamesofmatch import match
from Createnewaccount import createnewaccount
from authPassword import checkPassword
from authEmail import checkEmail

print( "Welcome to ......." )

ender = 0
while ender==0:

    print( "Main Menu" )
    choice = int(input("1.) Log in to Profile\n" "2.)Create New Profile\n" "3.) Exit\n"))

    if ( choice>3 or choice<1 ):
        print( "Invalid input.Please try again" )
        ender = 0
    if ( choice == 1 ):
        email = input( "Enter email: " )
        
        #if email does not exist
        while checkEmail(email)=="False":
            email = input( "Email does not exist\n" "Please try again: " )
        #if email passes
        password = input( "Enter Password: " )
        while checkPassword(email, password)=="False":
            password = input( "Incorrect password\n" "Try again: " )
            

        #if log in works
        #call function to check file of group type
        #use data found from type function to print names and emails of matching users
        print( match())
        



    if ( choice == 2 ):
        print( "Creating new profile" )
        #call jonahs function
        print (createnewaccount())
        print( "Your new account has been created!" )
        #return to menu
        ender = 0

    if( choice == 3 ):
        print( "Goodbye!" )
        ender = 1
        
