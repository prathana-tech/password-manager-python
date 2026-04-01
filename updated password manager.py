import random
import string
try:
    file=open("user_data.txt","r")
    file.close()
    user_exists=True
except:
    user_exists=False
if user_exists==False:
    print("first time setup")
    userset_pin=input("Set the Pin :")
    print("we need some security questions for recovery of pin")
    print("please answer them correctly")
    ques1=input("enter your favourite colour")
    ques2=input("enter your pet name")
    print("your answers are successfully saved")
    print("your pin is set \n  hope  for your good experience")
    with open ("user_data.txt","w")as file:
        file.write(userset_pin +"\n")
        file.write(ques1+"\n")
        file.write(ques2+"\n")
else:
    print("welcome back")
    with open("user_data.txt","r")as file:
        data=file.readlines()
    stored_pin=data[0].strip()
    stored_ans1=data[1].strip()
    stored_ans2=data[2].strip()
attempts=3
while attempts>0:
    user_pin=input("enter your  pin please you only have limited attempts :")
    if user_pin==stored_pin:
        print("access granted")
        break
    elif user_pin!=stored_pin:
        print("the pin you entered is incorrect")
        attempts=attempts-1
        print("Now you have ",attempts," attempts left please make sure to enter the correct pin ")
if attempts==0:
      print("too many wrong attempts,access is denied")
      print("do you want to recover the pin ?")
      want_recovery=input("IF  yes then please type yes , if no please type no")
      if want_recovery=="yes"or "Yes":
            print("okay \n please answer the security questions")
            ans1=input("Question 1: enter your favourite colour")
            if ans1==stored_ans1:
                    print("this is right")
                    ans2=input("Question2: enter your pet name :")
                    if ans2==stored_ans2:
                        print("Perfect! you can now set your new pin ")
                        userset2_pin=input("please enter your new pin")
                        userset2_pin==stored_pin
                        print("Your new pin is set")
            else:
                print("the answer you entered is incorrect")
                print("we cannot take you further")
                exit()
      else:
          print("okay")
          exit()
# Function to generate password
def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password


# Function to save password
def save_password(website, username, password):
    with open("passwords.txt", "a") as file:
        file.write(f"Website: {website} | Username: {username} | Password: {password}\n")
#Function to search feature
def search_feature():
    found=False
    website=input("enter your website to serach the password")
    with open("passwords.txt","r")as file:
        for line in file:
            if website.lower() in line.lower():
                print(line)
                found=True
        if found==False:
            print("no record found")            
# Function to view saved passwords
def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            data = file.read()
            if data == "":
                print("No passwords saved yet.")
            else:
                print("\nSaved Passwords:\n")
                print(data)
    except FileNotFoundError:
        print("No file found. Save a password first.")


# Main program
while True:
    print("\n===== Password Manager =====")
    print("1. Generate Password")
    print("2. Save Password")
    print("3. View Passwords")
    print("4.Search feature")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Generated Password:", password)

    elif choice == "2":
        website = input("Enter website name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        save_password(website, username, password)
        print("Password saved successfully!")

    elif choice == "3":
        view_passwords()
    elif choice=="4":
        search_feature()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
