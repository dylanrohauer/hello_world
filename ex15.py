# imports language from the command prompt into the argv
from sys import argv
# script = ex15.py and filename = ex15_sample.txt
script, filename = argv
# opens the content values of filename; assigns to txt
txt = open(filename)

print(f"Here's your file {filename}:")
# prints the internal values of txt using read
print(txt.read())
txt.close()
print("Type the filename again:")
# asks for a file to read again
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
