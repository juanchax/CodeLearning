# Sal's Shipping
# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers.
# Sal wants to make sure that every single one of his customers has the best,
# and most affordable experience shipping their packages. In this project, you’ll
# build a program that will take the weight of a package and determine the cheapest
# way to ship that package using Sal’s Shippers.
#
# Sal’s Shippers has several different options for a customer to ship their package.
# They have ground shipping, which is a small flat charge plus a rate based on the
# weight of your package. Premium ground shipping, which is a much higher flat
# charge, but you aren’t charged for weight. They recently also implemented drone
# shipping, which has no flat charge, but the rate based on weight is triple the
# rate of ground shipping.
#
# Here are the prices:
#
# Ground Shipping
#
# Weight of Package	                      Price per Pound 	  Flat Charge
# 2 lb or less	                            $1.50	            $20.00
# Over 2 lb but less than or equal to 6 lb	$3.00              	$20.00
# Over 6 lb but less than or equal to 10 lb	$4.00	            $20.00
# Over 10 lb                              	$4.75	            $20.00
#
#
# Drone Shipping
#
# Weight of Package	                      Price per Pound	  Flat Charge
# 2 lb or less	                            $4.50	            $0.00
# Over 2 lb but less than or equal to 6 lb	$9.00	            $0.00
# Over 6 lb but less than or equal to 10 lb	$12.00             	$0.00
# Over 10 lb	                                $14.25	            $0.00
#
#
# Premium Ground Shipping
#
# Flat charge: $125.00
#
# Write a program that asks the user for the weight of their package and then tells
# them which method of shipping is cheapest and how much it will cost to ship their
# package using Sal’s Shippers.

premium_ground_shipping = 125.0

def ground_shipping_cost(weight):
  flat_rate = 20.0

  less_2 = 1.5 # 23
  bet_2_6 = 3.0 # 38 <<<<
  bet_6_10 = 4.0 # 60 <<<
  over_10 = 4.75 # 67.7 and up <<<

  if (weight <= 2):
    return weight * less_2 + flat_rate
  elif (weight > 2) and (weight <= 6):
    return weight * bet_2_6 + flat_rate
  elif (weight > 6) and (weight <= 10):
    return weight * bet_6_10 + flat_rate
  else:
    return weight * over_10 + flat_rate


#print(ground_shipping_cost(8.4))

def drone_shipping_cost(weight):
  flat_rate = 0.0

  less_2 = 4.5 # 9 <<<
  bet_2_6 = 9.0 # 54
  bet_6_10 = 12.0 # 120
  over_10 = 14.25 # 142.5 and up

  if (weight <= 2):
    return weight * less_2 + flat_rate
  elif (weight > 2) and (weight <= 6):
    return weight * bet_2_6 + flat_rate
  elif (weight > 6) and (weight >= 10):
    return weight * bet_6_10 + flat_rate
  else:
    return weight * over_10 + flat_rate


#print(drone_shipping_cost(1.5))

def cheapest_shipping(weight):
    if (weight <= 2):
        return "Drone Shipping", drone_shipping_cost(weight)
    elif (weight > 2) and (weight < 22.106):
        return "Ground Shipping", ground_shipping_cost(weight)
    else:
        return "Premium Ground Shipping", premium_ground_shipping


#print(cheapest_shipping(41.5))
