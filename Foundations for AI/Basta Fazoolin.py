from datetime import time
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"{self.name} menu is available from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
      return f"Your total is: ${total}"
 
class franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f"The address for this restaurant is: {self.address}"

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises



#Menu items and their menu hours

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('brunch', brunch_items, 1100, 1600)

eary_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('early_bird', eary_bird_items, 1500, 1800)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('dinner', dinner_items, 1700, 2300)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('kids', kids_items, 1100, 2100)

arepa_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Arepa', arepa_items, 1000, 2000)

all_menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

#franchises
flagship_store = franchise("1232 West End Road", all_menus)
new_installment = franchise("12 East Mulberry Street", all_menus)
arepas_place = franchise("189 Fitzgerald Avenue", arepas_menu)

#business
biz1 = Business("Basta Fazoolin/' with my Heart", [flagship_store, new_installment])
biz2 = Business("Take a/' Arepa", arepas_place)

#Testing the brunch menus and the calculations
#print(brunch_menu)
#print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#Testings of the franchise information
#print(flagship_store)
#print(flagship_store.available_menus(1700))
