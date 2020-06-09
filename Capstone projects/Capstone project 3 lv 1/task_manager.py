### Create a program for a small buisiness.
### The program should help manage tasks assigned to each memeber of the team

### Create username and password text file
### Create Task text file

userfile = open("user.txt", "w+")
tasks = open("tasks.txt", "w+")

### Set admin name and password to admin, adm1n

name = userfile.write("Admin: admin")
password = userfile.write(", adm1n")


### Create a login section
### Ensure user name is correct. If not ask for it again till correct.

login = input("Enter user name: ")
while login != "admin":
    if login != "admin":
        login = input("Error try again: ")

### Ensure password is correct, if not ask for it again till correct.

login_password = input("Enter your password: ")
while login_password != "adm1n":
    if login_password != "adm1n":
        login_password = input("Error try again: ")
        

### Once user answers correctly open menu.
print("\nPlease select one of the following: \nr - register user \na - add task \nva - view all tasks \nvm - view my tasks \ne - exit")        

### If user chooses r

user_choice = input("Enter choice here: ")

if user_choice == "r":
    name1 = input("Please enter new user name: ")
    password1 = input("Enter password here:")
    password_c = input("Please confirm password: ")
    if password_c == password1:

### Add name and password to user.txt

        userfile.write("\nRegistered Users:\n")
        userfile.write(name1)
        userfile.write(", ")
        userfile.write(password1)
          
        
### If user chooses a

if user_choice == "a":
    task_who = input("Enter the person the task is for: ")
    task_name = input("\nEnter Task title: ")
    task_desc = input("\nEnter Task desciption: ")
    task_due = input("\nEnter Due date: ")
    current_date = input("\nEnter the date today?: ")
    tasks.write("\nThis task is for:")
    tasks.write(task_who)
    tasks.write("\nTask title: ")
    tasks.write(task_name)
    tasks.write("\nTask description: ")
    tasks.write(task_desc)
    tasks.write("\nTask due date: ")
    tasks.write(task_due)
    tasks.write("\nTask assigned on: ")
    tasks.write(current_date)
    tasks.write("\nTask complete?: No")
    
    
### If user chooses va

if user_choice == "va":
    for line in tasks:
        print(line)
        

### If user chooses vm

if user_choice == "vm":
    for line in task_display:
        print(line)

userfile.close()
tasks.close()
    
### I know this is not quite complete but I could do with some help. Getting a bit confused and need to move onto other tasks.

#################################### END PROGRAM #################################
    
    
    
        









        
        
 

    
        
        
    
    

