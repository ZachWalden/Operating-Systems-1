import subprocess

#TODO ##########

# Run "dir" command, which prints the diretory contects
def dir():
   output = subprocess.check_output("dir", shell=True)
   print(output)

####
#TODO ##################
#Print the current working directory
def cd():
   
   #Run CD Shell command
   output = subprocess.check_output("cd", shell=True)
   print(output)

#Use mkdir to create a a new directory is the user's present directory.
def mkdir():
    new_dir = input("Enter name of directory to be made: ")
    try:
        output = subprocess.check_output(f"mkdir {new_dir}", shell=True)
        print(f"Directory {new_dir} created in your current directory.")
    except: 
        print("Error: Invalid directory name.\nPlease try again.")

#Use echo to print a user's inputted message
def echo():
    message = input("Input your message to be 'echoed', or printed by the system: ")
    try:
        #Run ECHO shell command with the user's inputted message
        output = subprocess.run(f"echo {message}", shell=True)
    except: 
        print("Error outputting")

#Recieve two file inputs, the resulting file name, and print the result. Done using "type"
def type():
    file_chosen1 = input("Input file 1 to be concatenated: ")
    file_chosen2 = input("Input file 2 to be concatenated: ")
    new_file_name = input("Input the name of the resulting concatenated file, INCLUDING FILE EXTENSION: ")
    try: 
        #Run the type command to concatenate 
        output = subprocess.check_output(f"type {file_chosen1} {file_chosen2} > {new_file_name}", shell=True)
        print(output)
    except:
        print("Error: Input file not found.")
