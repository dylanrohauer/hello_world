#there are 100 cars
cars = 100
#there are 4 seats in each car
space_in_a_car = 4.0
#there are 30 people with drivers licences
drivers = 30
#there are 90 people who won't drive
passengers = 90
#there are 70 cars not drove
cars_not_driven = cars - drivers
#there are 30 driven cars
cars_driven = drivers
#there is space for 120 people
carpool_capacity = cars_driven * space_in_a_car
#the cars need to be this full
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


# Error from learnpythonthehardway
# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#       average_passengers_per_car = carpool_capacity / passengers
# NameError: name 'car_pool_capacity' is not defined

# The reason for this error is that car_pool_capacity is not the same variable
# as carpool_capacity
