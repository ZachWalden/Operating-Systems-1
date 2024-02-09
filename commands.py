import subprocess

#TODO ##########

# Run "dir" command, which prints the diretory contects
def dir():
   subprocess.run("dir", shell=True)

####
#TODO ##################
#Print the current working directory
def cd():
   #Run CD Shell command
   print("Printing the current working directory... \n")
   subprocess.run("cd", shell=True)

#Use mkdir to create a a new directory is the user's present directory.
def mkdir():
    new_dir = input("Enter name of directory to be made: ")
    print("Creating new directory... \n")
    try:
        output = subprocess.check_output(f"mkdir {new_dir}", shell=True)
        print(f"Directory '{new_dir}' has been created in your current directory. Running 'dir' should reflect this change.")
    except: 
        print("Error creating the directory...")

#Use echo to print a user's inputted message
def echo():
    message = input("Input your message to be 'echoed', or printed by the system: ")
    print("Message outputted from Shell: \n")
    subprocess.run(f"echo {message}", shell=True)


#Recieve two file inputs, the resulting file name, and print the result. Done using "type"
def type():
    print("Input your files to be concatenated. (example_file1.txt & example_file2.txt included)")
    
    #Read in the user's files to concatenate & the resulting file name.
    file_chosen1 = input("Input file 1 to be concatenated (INCLUDING FILE EXTENSION): ")
    file_chosen2 = input("Input file 2 to be concatenated (INCLUDING FILE EXTENSION): ")
    new_file_name = input("Input the name of the resulting concatenated file, being placed in your current directory (INCLUDING FILE EXTENSION): ")
    subprocess.run(f"type {file_chosen1} {file_chosen2} > {new_file_name}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    #Run 'type' on the new file to display the file contents:
    print("Running 'type' command to display your concatenated file's contents:\n")
    subprocess.run(f"type {new_file_name}", shell=True)