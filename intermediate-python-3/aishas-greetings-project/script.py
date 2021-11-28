# Write your code below: 
from contextlib import contextmanager

@contextmanager
def generic(card_type, sender_name, receiver):
  card_file=open(card_type, 'r')
  new = open(f"{sender_name}_generic.txt", 'w')
  try:
    new.write('Dear {} \n \n'.format(receiver))
    new.write(card_file.read())
    new.write('\n \nSincerly, {}\n'.format(sender_name))
    yield new
  finally:
    card_file.close()
    new.close()

with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as g:
  print('hola ctm {} \n{}'.format('wn', 'ctm'))

with open('Mwenda_generic.txt', 'r') as primera:
  print(primera.read())

class Personalizada:
  def __init__(self, sender, receiver):
    self.sender = sender
    self.receiver = receiver
    self.newfile = open(f'{sender}_personalized.txt', 'w')

  def __enter__(self):
    self.newfile.write(f'Dear {self.receiver} \n \n')
    return self.newfile

  def __exit__(self, exc_type, exc_value, Traceback):
    self.newfile.write(f'\n \nSincerely, {self.sender} \n')
    self.newfile.close()

with Personalizada('Jhon', 'Michael') as newcard2:
  newcard2.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

with open('Jhon_personalized.txt', 'r') as segunda:
  print(segunda.read())

with generic('happy_bday.txt', 'Josiah', 'Remy') as otra1:
  with Personalizada('Josiah', 'Esther') as otra2:
    otra2.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")

with open('Josiah_generic.txt', 'r') as c1, open('Josiah_personalized.txt', 'r') as c2:
  print(c1.read())
  print(c2.read())


