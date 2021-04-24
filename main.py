import os

skip = False

def clear():
    os.system('clear')

my_secret = os.environ['password']

red = "\033[1;31m"
white = "\033[0;37m"

def question(): 

  password1 = int(input("Enter your password (hint, it begins with 2 and ends in 8): "))
  if password1 < 27:
    print("BEBAAWWBEREBAWW THE POpoooo is ready we used Just Eat you should use Just Eat tooooooooo ARE HERE")
  elif password1 < 29:
    clear()
    print("Congrats police are coming to buckingham palace!\n")

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
          print("congratulations you have hacked NASA")

          print(" ")
          print(" " + red + "Welcome to NASA")

        else:
          print("Ahh sorry mate, maybe next time! YOU WILL NEVER BE ACCEPTED TO NASA EVER AGAIN!")

      else:
        print("NOPE JUST NOPE")

    else:
      print("Boo ya")

  else:
  	print("NOPE JUST NOPE")

login = input("Login:")
if login == "letmein":
  skip = True

if skip == False:
  question()
else:
  print("Skipped")
