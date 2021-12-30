exit_words = ['stop', 'exit', 'bye', 'chao ctm', 'sayonara', 'ciao']
import sys
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')
  
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  elif res in exit_words:
    sys.exit("{} is my favorite exit word".format(res))
  else:
    print_message()
    return get_size()

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  elif res in exit_words:
    sys.exit("{} is my favorite exit word".format(res))
  else:
    print_message()
    return order_latte()
