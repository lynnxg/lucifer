#Begin bericht
def welcome_message():
  print("LUCIFERSPEL")
  print()
  print('Welkom bij het Luciferspel.')
  print('De computer en de speler (jij dus!) nemen om de beurt 1, 2 of 3 lucifers weg.')
  print('Degene die als laatste lucifers moet pakken, heeft verloren.')
  print('Success!')

welcome_message()

import random
aantallucifers = random.randint(20 , 25)
print("We beginnen met %s lucifers." % aantallucifers)
print()


#Lopend spel

def speler_actie():
  global aantallucifers
  if aantallucifers > 0:
   print("Er zijn nog %s lucifers" % aantallucifers)
   aantalwegpakken = input("Hoeveel wil je er pakken? ")
   aantalwegpakken = int(aantalwegpakken)
   aantallucifers -= aantalwegpakken
   print("Aantal lucifers over: %s" % aantallucifers)
  turn = 1


def computer_actie():
  turn = 0


#Beurten
turn = 0

if turn == 0:
  speler_actie()
else:
  computer_actie()

