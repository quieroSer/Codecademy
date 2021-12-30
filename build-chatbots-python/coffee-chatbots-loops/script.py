from utils import print_message, get_size, order_latte
exit_words = ['stop', 'exit', 'bye', 'chao ctm', 'sayonara', 'ciao']
import sys
def coffee_bot():
  print("Welcome to the cafe! Type your favorite exit word anytime to exit")
  order_drink = 'y'
  drinks = []
  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)
    while True:
      order_drink = input("would you like to order another drink? (y/n) \n>")
      if order_drink in exit_words:
        sys.exit("{} is my favorite exit word".format(order_drink))
      elif order_drink in ['y', 'n']:
        break
  print("ok, so I have:\n")
  for order in drinks:
    print("- {}".format(order))
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  elif res in exit_words:
    sys.exit("{} is my favorite exit word".format(res))
  else:
    print_message()
    return get_drink_type()
  
# Define new functions here!
def order_mocha():
  while True:
    res = input("Would you like to try our limited_edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n>")
    if res == "a":
      return 'peppermint mocha'
    elif res == "b":
      return 'mocha'
    elif res in exit_words:
      sys.exit("{} is my favorite exit word".format(res))
    else:
      print_message()
      order_mocha()

coffee_bot()
