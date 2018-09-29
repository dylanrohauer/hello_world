# escapes and formats
# asks for an adjective as an input
verb = input("Please input an adjective: ")
# string w/ empty format
red = "Retired and Extremely {}"
# inro w/ empty fomrat
intro = "This Month\nComes The New Action Thriller\n{}"
# prints the intro with the red format w/ the verb as the red's format
print(intro.format(red.format(verb)))
