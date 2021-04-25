import os
from replit import db

keys = db.keys()

print(keys)


skip = False

def clear():
  os.system('clear')

my_secret = os.environ['password']

red = "\033[1;31m"
white = "\033[0;37m"

def backdoor():


  SecurityCode = input("Input your security code: ")

  if SecurityCode == "ILOVEBUNNIES":
    clear()
    Password2 = input("Input your reason for being in NASA: ")

    if Password2 == "FireArms":
      clear()
      BotDetector2000 = input("Are you a bot: ")

      if BotDetector2000 == "Oui":
        clear()
        loginsystem()
       
      else:
        print("Hmmm thats a bit sus!")
    else:
      print("you are a bot")
  else:
    print("you are a bot")




def loginsystem():
  print("Welcome to NASA")


  username = input("Username: ")
  if username != 'Admin':
    value = db[username]
    if value == "reset":
      firstimepassword = input("It appears this is your first time logging in as "+username+". Please type in the password you would like to sign in with\n--> ")
    
      db[username] = firstimepassword

    
  password = input("Password: ")
        
  if username == "Admin":
          
    exitadmin = 0
    while exitadmin == 0:
      clear()
      admin = int(input("Welcome to NASA, Admin\n Here, you can:\n1. Add a user\n2. Remove a user\n\n--> "))
      if admin == 1:
        clear()
        print("Here are the list of users:\n")
        print(keys)
        user = input("Please enter the name of the user you would like to create\n--> ")
        db[user] = "reset"
        clear()
        print("Here is the updated list of users:\n")
        print(keys)
        admin = input("All done! The first time "+user+" signs in, they will be prompted to add a password\nWould you like to exit admin?\n\n--> ")
        if admin == "yes":
          exitadmin = 1
          clear()
          loginsystem()
        else:
          exitadmin = 0
          
              
      if admin == 2:
        clear()
        print("Here are the list of users:\n")
        print(keys)
        user = input("Please enter the name of the user you would like to remove\n--> ")
        del db[user]
        clear()
        print("Here is the updated list of users:\n")
        print(keys)
        admin = input("All done! "+user+" has been removed.\nWould you like to exit admin?\n\n--> ")
        if admin == "yes":
          exitadmin = 1
          clear()
          loginsystem()
        else:
          exitadmin = 0
            
  else:
    value = db[username]
    if value == password:
      print("Welcome to NASA, " + username)

    else:
      print("I am so sorry, but it appears that your username or password is incorrect")
  

def question(): 


  password1 = input("Enter your password (hint, it begins with 2 and ends in 8): ")
  if password1 == "letmein":
    backdoor()
  elif password1 == "topsecretcookies":
    clear()
    loginsystem()
  elif password1 == "28":
    print("BEBAAWWBEREBAWW THE POpoooo is ready we used Just Eat you should use Just Eat tooooooooo ARE HERE")

    password2 = int(
      input("Enter your password (hint it is one " + red + "number" + white + " long and is a multiple \nof 6): "))
    if password2 < 5:
      print("Blimey mate its hot outside")
    elif password2 < 7:
      clear()
      print("You've done just fine!\n")

      botdetector2000 = input("If you are a computer then please type yes if not then type no: ")
      if botdetector2000 == "Oui":
        clear()
        password3 = input("Final question, what is the super duper secret key that nobody knows execpt NASA: ")
                
        if password3 == my_secret:
          clear()
          loginsystem()

        else:
          print("Ahh sorry mate, maybe next time! YOU WILL NEVER BE ACCEPTED TO NASA EVER AGAIN!")

      else:
        print("NOPE JUST NOPE, I mean why even ")

    else:
      print("Boo ya")

  else:
  	print("NOPE JUST NOPE")

question()



