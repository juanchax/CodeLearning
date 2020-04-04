# create a variable cars and assign the integer vañue 100
cars = 100

# create a variable space_in_a_car and assign the float value 4.0
space_in_a_car = 4.0

# create the variable drivers and assign it the integer value 30
drivers = 30

# create the variable passengers and assign it the integer value 90
passengers = 90

# create the variable cars_not_driven and assign the result of cars - drivers as the value
cars_not_driven = cars - drivers

# create a variable cars_driven and assign the number of drivers as the value
cars_driven = drivers

# create a variable carpool_capacity and assign the RESULT of the
# cars_driven multiplied by the space_in_a_car as the value
carpool_capacity = cars_driven * space_in_a_car

# create a variable average_passengers_per_car and assign the RESULT of
# the number of passengers divided by the cars driven as the value
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
