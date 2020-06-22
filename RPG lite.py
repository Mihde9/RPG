import random
import re


supermanhp = 500
jokerattl = 20
jokerattm = 70
jokeratth = 120

while supermanhp > 10:
  damage = random.randrange(jokerattl, jokeratth)
  supermanhp = supermanhp - damage
  
  if supermanhp <= 10:
    supermanhp = 10

  print("Joker hits", damage, "of damage to Superman. Superman's HP is", supermanhp)

  if supermanhp == 10:
    print("Superman is dead, and Loise Lane cannot save him")