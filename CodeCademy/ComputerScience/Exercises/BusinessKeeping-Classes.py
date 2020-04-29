# Basta Fazoolin'
#
# You’ve started position as the lead programmer for the family-style
# Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has
# been doing fantastically and seen a lot of growth lately. You’ve been
# hired to keep things organized.
from datetime import datetime

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return '{name} menu available from {start} to {end}'.format(name=self.name, start=self.start_time, end=self.end_time)

    def calculate_bill(self, purchased_items):
        purchase_total = 0
        for item in purchased_items:
            purchase_total += self.items[item]
        return purchase_total

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        current_time = time
        if isinstance(time, str):
            current_time = int(time)
        elif isinstance(time, datetime):
            current_time = float(time.strftime('%H'))
        for menu in self.menus:
            if (float(menu.start_time) <= float(current_time)) and (float(current_time) <= float(menu.end_time)):
                for item in menu.items:
                    print(item)

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# --- Build the different Menus for our program

brunch_items = {
  'pancakes': 7.50,
  'waffles': 9.00,
  'burger': 11.00,
  'home fries': 4.50,
  'coffee': 1.50,
  'espresso': 3.00,
  'tea': 1.00,
  'mimosa': 10.50,
  'orange juice': 3.50
}
brunch = Menu('brunch', brunch_items, 11, 16)

early_bird_items = {
  'salumeria plate': 8.00,
  'salad and breadsticks (serves 2, no refills)': 14.00,
  'pizza with quattro formaggi': 9.00,
  'duck ragu': 17.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 1.50,
  'espresso': 3.00,
}
early_bird = Menu('early_bird', early_bird_items, 15, 18)

dinner_items = {
  'crostini with eggplant caponata': 13.00,
  'ceaser salad': 16.00,
  'pizza with quattro formaggi': 11.00,
  'duck ragu': 19.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 2.00,
  'espresso': 3.00,
}
dinner = Menu('dinner', dinner_items, 17, 23)

kids_items = {
  'chicken nuggets': 6.50,
  'fusilli with wild mushrooms': 12.00,
  'apple juice': 3.00
}
kids = Menu('kids', kids_items, 11, 21)

arepas_items = {
  'arepa pabellon': 7.00,
  'pernil arepa': 8.50,
  'guayanes arepa': 8.00,
  'jamon arepa': 7.50
}
arepas_menu = Menu('arepas', arepas_items, 10, 20)

# --- Build the available Franchises

arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

# --- Build our Businesses

basta_fazoolin_franchises = [flagship_store, new_installment]
basta_fazoolin = Business('Basta Fazoolin\' with my Heart', basta_fazoolin_franchises)

take_arepa_franchises = [arepas_place]
take_arepa = Business('Take a\' Arepa', take_arepa_franchises)
