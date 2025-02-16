import os, sys

print("This is a demo script.")
command = input("Do you want open scripts folder? [y/n]: ")
if (command == "y"):
    os.startfile(filepath="resources/scripts")
else:
    sys.exit()
