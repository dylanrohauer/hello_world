# defines a string that includes four places for a variable to be inserted into the format
formatter = "{} {} {} {}"

# expresses the result of entering 1 2 3 4 into the formatter via pritn funct
print(formatter.format(1, 2, 3, 4))
# enters 'one' 'two' 'three' 'four' into the string
print(formatter.format("one", "two", "three", "four"))
# enters T F F T into the string
print(formatter.format(True, False, False, True))
# enters the string "{} {} {} {}" into the string four times
print(formatter.format(formatter, formatter, formatter, formatter))
# enters 4 seperate strings into the formatter string
print(formatter.format(
  "Maybe",
  "One Day",
  "I Won't Be Afraid",
  "Of the things I Fear"
))
