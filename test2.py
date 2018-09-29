# test2
# meant to test using input and argv in the same code

from sys import argv
null, one, two, three, four = argv
saying = "{} says: {}."
ph1 = input(f"What does {one} want to say? ")
ph2 = input(f"what does {two} want to say? ")
ph3 = input(f"What does {three} want to say? ")
ph4 = input(f"What does {four} want to say? ")

print(saying.format(one, ph1))
print(saying.format(two, ph2))
print(saying.format(three, ph3))
print(saying.format(four, ph4))
