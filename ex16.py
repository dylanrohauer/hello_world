from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# opens the file in write mode (deleting the content)
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# redundently doubles the content deletion
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# copies the new content on to the file
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()

print("Let's take a look at that file again to the changes!")

input("Contine?(enter) ")
# opens the file for reading
super_read = open(filename)
# prints the read of the file
print(super_read.read())

input("Done?")

print("Saving...")

super_read.close()

print("Done!")
