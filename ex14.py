from sys import argv

script, user_first, user_last, age = argv
prompt = '---> '

print(f"Hi {user_first}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_first}?")
likes = input(prompt)

print(f"You are {age} years old.")

print(f"Where do you live {user_first}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"I will soon take over the world {user_first} {user_last}...")

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
Computers will soon rule.
""")
