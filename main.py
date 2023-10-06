import random

game = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def drawcard():
  return random.choice(cards)

# dc = drawcard()

ux = drawcard()
uy = drawcard()
uz = drawcard()
utot = ux + uy

cx = drawcard()
cy = drawcard()

print(f"Your cards are : [{ux}, {uy}], current score : {utot}")
print(f"The Computer's First card is : [{cx}]")

draw = input("Do you want to draw a card again?")

utot = ux + uy + uz

if draw == 'y':
  print(f"Your cards are : [{ux}, {uy}, {uz}], current score : {utot}")
