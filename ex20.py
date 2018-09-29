from sys import argv
# imports the script name and anther file name
script, input_file = argv

def print_all(f):
    # prints a reading of a file it receives
    print(f.read())

def rewind(f):
    # returns the reading or writing position back to the begining of the file
    f.seek(0)

def print_a_line(line_count, f):
    # prints the line count number as well as the line's text
    # read line returns the '\n' so if you dont want 2x spacing
    # put , end = '' at the end
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")
# inputs the open file and runs through commands in the print_all funct
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# inputs the open file and runs through current_file funct
rewind(current_file)

print("Let's print three lines:")

current_line = 1
# enters the file line number and the file to print a line
print_a_line(current_line, current_file)
# reassigns the value of current line 2
current_line +=  1
print_a_line(current_line, current_file)
# value 3
current_line += 1
print_a_line(current_line, current_file)
