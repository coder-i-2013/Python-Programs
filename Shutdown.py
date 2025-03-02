import sys
shut= input("do you want to shut down the computer \n click Y for yes\n click N for no")
def shutdown_program():
    if shut == 'n' or 'N':
        print ("you chose not to shut down")
    if shut == 'y' or 'Y':
        print("Shutting down the program...")
        sys.exit()
    shutdown_program()
