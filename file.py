#file.py
from sys import argv

script, filename = argv

rewrite = open(filename, 'w')

content = input("Enter somethin' good: ")
rewrite.write(content + "\n")
print("Saving...")
rewrite.close()

input("Reading...")
reread = open(filename)
print(reread.read())

print("all done!")
reread.close()
