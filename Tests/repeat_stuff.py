#def repeat_stuff(stuff, num_repeats=10):
#  return stuff * num_repeats

#lyrics = repeat_stuff("Row ", 3) + "Your boat. "
#print(lyrics)

#
# available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
# health_points = 20
#
# health_points += available_items.pop("stamina grains", 0)
# health_points += available_items.pop("power stew", 0)
# health_points += available_items.pop("mystic bread", 0)

# print(available_items)
# print(health_points)

s = 34r
print(type(s))

# premium_ground_shipping = 125.0
#
# def ground_shipping_cost(weight):
#   flat_rate = 20.0
#
#   less_2 = 1.5 # 23
#   bet_2_6 = 3.0 # 38 <<<<
#   bet_6_10 = 4.0 # 60 <<<
#   over_10 = 4.75 # 67.7 and up <<<
#
#   if (weight <= 2):
#     return weight * less_2 + flat_rate
#   elif (weight > 2) and (weight <= 6):
#     return weight * bet_2_6 + flat_rate
#   elif (weight > 6) and (weight <= 10):
#     return weight * bet_6_10 + flat_rate
#   else:
#     return weight * over_10 + flat_rate
#
#
# #print(ground_shipping_cost(8.4))
#
# def drone_shipping_cost(weight):
#   flat_rate = 0.0
#
#   less_2 = 4.5 # 9 <<<
#   bet_2_6 = 9.0 # 54
#   bet_6_10 = 12.0 # 120
#   over_10 = 14.25 # 142.5 and up
#
#   if (weight <= 2):
#     return weight * less_2 + flat_rate
#   elif (weight > 2) and (weight <= 6):
#     return weight * bet_2_6 + flat_rate
#   elif (weight > 6) and (weight >= 10):
#     return weight * bet_6_10 + flat_rate
#   else:
#     return weight * over_10 + flat_rate
#
#
# #print(drone_shipping_cost(1.5))
#
# def cheapest_shipping(weight):
#     if (weight <= 2):
#         return "Drone Shipping", drone_shipping_cost(weight)
#     elif (weight > 2) and (weight < 22.106):
#         return "Ground Shipping", ground_shipping_cost(weight)
#     else:
#         return "Premium Ground Shipping", premium_ground_shipping
#
#
# #print(cheapest_shipping(41.5))
