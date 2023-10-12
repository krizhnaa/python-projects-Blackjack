############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

game = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def drawcard():
  return random.choice(cards)

# dc = drawcard()

usercardlist = []
compcardlist = []

usercardlist.append(drawcard())
usercardlist.append(drawcard())
usertot = 0

compcardlist.append(drawcard())
compcardlist.append(drawcard())
comptot = 0

for x in usercardlist:
  usertot+=x

for y in compcardlist:
  comptot+=y

print(f"Your cards are : {usercardlist}, curr score : {usertot}")
print(f"Computer's First hand : {compcardlist[0]}")

while comptot < 17:
  y = drawcard()
  compcardlist.append(y)
  comptot+=y

while True:
  draw = input("Do you want to draw again? 'y' or 'n'  ")
  if draw == 'y':
    x = drawcard()
    usercardlist.append(x)
    usertot+=x
    print(f"Your cards are : {usercardlist}, curr score : {usertot}")
  else:
    break;

if usertot < 22 and comptot < 22:
  if usertot > comptot:
    print("The user wins")
  else:
    print("The Dealer wins")
elif usertot > 21:
  print("Dealer wins")
elif comptot > 21:
  print("User Wins")


print(usercardlist, usertot)
print(compcardlist, comptot)


  
  
  
