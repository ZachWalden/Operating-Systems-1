import commands

use_shell = True
command_list = ['dir', 'cd', 'mkdir', 'echo', 'type']
while use_shell:
    print("""Select a command to run: 
    1. List directory contents (dir)
    2. Print working directory (cd)
    3. Create a new directory (mkdir)
    4. Display a message (echo)
    5. Concatenate and display content of a file (type)
    6. Exit""")
        
    user_in = input("Command Number: ")
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
            #Concatenate two files, output the result
            commands.type() 
        case 6: 
            use_shell = False
        case _:
            print("Invalid Input, please try again.")
            continue

