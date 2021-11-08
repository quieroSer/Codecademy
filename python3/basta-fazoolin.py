from datetime import time

#menu class
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name=name
    self.items=items
    self.start_time=start_time
    self.end_time=end_time
  
  def __repr__(self):
    frase="{} menu is available from {} to {}".format(self.name, self.start_time, self.end_time)
    return frase

  def calculate_bill(self, purchased_items):
    total=0
    for item in purchased_items:
      if(item in self.items):
        total+=self.items[item]
        print(total)
    return total

brunch=Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, time(11, 0, 0), time(16, 0, 0))

early_bird=Menu("early bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, time(15, 0, 0), time(18, 0, 0))

dinner=Menu("dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, time(17, 0, 0), time(21, 0, 0))

kids=Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, time(11, 0, 0), time(21, 0, 0))

arepas_menu=("Take a´Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, time(10, 0, 0), time(20, 0, 0))

#franchise class
class Franchise:
  def __init__(self, address, menus):
    self.address=address
    self.menus=menus
  
  def __repr__(self):
    return "This restaurant is located at {}".format(self.address)

  def available_menus(self, timegiven):
    for menu in self.menus:
      if(menu.start_time.hour <= timegiven.hour and menu.end_time.hour >= timegiven.hour):
        print(menu.name +" is available!!")
      else:
        print(menu.name +" is not available")

flagship_store=Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment=Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place=Franchise("189 Fitzgerald Avenue", [arepas_menu])

flagship_store.available_menus(time(20, 0, 0))

#business class
class Business:
  def __init__(self, name, franchises):
    self.name=name
    self.franchises=franchises

firstBusiness=Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
newBusiness=Business("Take a' Arepa", [arepas_place])


