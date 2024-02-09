#Zach Walden
#w989j327
#Operating Systems Assignment 1 - Running dir, cd, mkdir, echo, & type commands.

import commands

use_shell = True

#Display this menu & read in input until the user decides to exit
while use_shell:
    print("""\nSelect a command to run: 
    1. List directory contents (dir)
    2. Print working directory (cd)
    3. Create a new directory (mkdir)
    4. Display a message (echo)
    5. Concatenate and display content of a file (type)
    6. Exit""")
        
    user_in = input("Command Number: ")
    print("\n")
    #Run desired command:
    match int(user_in):
        case 1:
            commands.dir()
        case 2:
            commands.cd()
        case 3:
            commands.mkdir()
        case 4: 
            commands.echo()
        case 5: 
            commands.type() 
        case 6: 
            use_shell = False
        case _:
            print("Invalid Input, please try again.")
            continue

