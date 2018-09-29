name = 'Zed A. Shaw'
age = 35
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

weight_kilos = round(weight * 0.453592)
height_centimeters = height * 2.54

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_centimeters} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_kilos} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
