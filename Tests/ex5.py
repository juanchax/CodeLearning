name = 'Zed A. Shaw'
age = 35 # not a lie
height_inches = 74 # inches
weight_lbs = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_inches} inches tall.")
print(f"He's {weight_lbs} pounds heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_inches + weight_lbs
print(f"If I add {age}, {height_inches}, and {weight_lbs} I get {total}.")
height_cm = height_inches * 2.54
weight_kg = weight_lbs * 0.45
total_cm_kg = age + height_cm + weight_kg
print(f"But if I add {age}, {height_cm}, and {weight_kg} I get {total_cm_kg}")
