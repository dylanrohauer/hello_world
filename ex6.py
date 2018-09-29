#there are 1 and 0 types of people lol bad joke
types_of_people = 10
#first sentence
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
#first 2 string combos
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)
#third string combo
print(f"I said: {x}")
#fouth string combo
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#fith string combo
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#string is made longer because it uses math combiners to add strings
print(w + e)
