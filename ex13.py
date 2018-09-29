# imports variables that you enter when running program from command line
# > python ex13.py argv1 argv2 argv3
from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
