#Black Jack Game on Terminal

import random

#returns the value of the card
def card_value(card):
  if card[0] == ["Ace"]:
    return 11
  elif card[0] in ['Jack', 'Queen', 'King']:
    return 10
  else:
    return int(card[0])

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
#create a deck of cards
deck_cards = []
for cat in card_categories:
  for card in card_list:
    deck_cards.append((card, cat))
#shuffle the deck of cards
random.shuffle(deck_cards)

while True:
  print("Player has blank cards")
  print("Player total: ")
  print("Dealer has blank cards")
  print("Dealer total: ")
  print()
  choice = input("Would you like to Deal(D) or Stand(S)? ")
  if choice == "D":
    #Recieves Another Card
    print("Grabs Another Card")
  elif choice == "S":
    #Stands
    break
  else:
    #Incorrect Input
    print("Invalid Choice. Please try again.")
    continue

  print("Testing")