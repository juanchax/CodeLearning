# The Boredless Tourist
#
# Welcome to The Boredless Tourist, an online application giving you
# the power to find the parts of the city that fit the pace of your
# life. We at The Boredless Tourist run a recommendation engine using
# Python. We first evaluate what a person’s interests are and then give
# them recommendations in their area to venues, restaurants, and historical
# destinations that we think they’ll be engaged by. Let’s get started!

destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  index = destinations.index(destination)
  return index

# test get_get_destination()
#get_destination_index('Paris, France')

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)

attractions = [[] for dest in destinations]

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = []
  attractions_for_destination.append(attraction)
  try:
    attractions[destination_index] = attractions_for_destination
    # print(attractions_for_destination)
    return attractions_for_destination
    # some_thing = can_trigger_a_syntax_errror()
  except SyntaxError:
    return

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
# print(attractions)

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]

  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = possible_attraction[1]

    for interest in interests:
      if attraction_tags.count(interest) > 0:
        attractions_with_interest.append(possible_attraction[0])

  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ['art'])
# print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

  interest_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": the "

  for attraction in traveler_attractions:
    interest_string += attraction + ", "

  #interest_string += ". "
  return interest_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
