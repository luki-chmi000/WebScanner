import subprocess
import os
import prog_functions
home_dir = os.path.expanduser("~")
mainloop = True

print("Pretty simple (and crude) scanner for local networks")

while mainloop:

    print(home_dir, end = ' ')
    command_input = input("> ")

    prog_functions.parseInput(command_input)
    





