#Begin bericht
def welcome_message():
  print("LUCIFERSPEL")
  print()
  print('Welkom bij het Luciferspel.')
  print('De computer en de speler (jij dus!) nemen om de beurt 1, 2 of 3 lucifers weg.')
  print('Degene die als laatste lucifers moet pakken, heeft verloren.')
  print('Success!')

welcome_message()

#Aantal lucifers waar het spel mee begint
import random
aantallucifers = random.randint(20 , 25)
print("We beginnen met %s lucifers." % aantallucifers)
print()


#Lopend spel
def speler_actie():
  global aantallucifers
  global turn
  if aantallucifers > 0:
   print("Er zijn nog %s lucifers" % aantallucifers)
   aantalwegpakken = input("Hoeveel wil je er pakken? ")
   aantalwegpakken = int(aantalwegpakken)
   aantallucifers -= aantalwegpakken
   print("Aantal lucifers over: %s" % aantallucifers)
   print()
   turn = 1


def computer_actie():
  global aantallucifers
  global turn
  if aantallucifers > 0:
    if aantallucifers > 3:
      aantalwegpakken2  = random.randint(1 , 3)
      print("De computer pakt %s lucifers weg" % aantalwegpakken2)
      aantallucifers -= aantalwegpakken2
    elif aantallucifers == 3:
      aantallucifers -= 2
      print("De computer pakt 2 lucifers weg")
    elif aantallucifers == 2:
      aantallucifers -=1
      print("De computer pakt 1 lucifer weg")
    else:
      aantallucifers -=1
      print("De computer pakt 1 lucifer weg")
    turn = 0


#Beurten
turn = 0

while aantallucifers > 0:
  if turn == 0:
   speler_actie()
  elif turn == 1:
   computer_actie()


#Eind bericht
if aantallucifers <= 0:
  if turn == 0:
   print("1")
  if turn == 1:
   print("2")