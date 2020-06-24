from rpg.classes.Enemy import Enemy, bcolors
import re

magic = [{"name": "Fire", "cost": 15, "dmg": 60},
         {"name": "Freeze", "cost": 20, "dmg": 80},
         {"name": "Water", "cost": 30, "dmg": 100}]

player = Enemy (800, 400, 180, 250, magic)
enemy = Enemy (800, 340, 150, 222, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "JOKER vs SUPERMAN" + " Battle for Gotham" + bcolors.ENDC)

while running:
   print("=====================")
   player.choose_action()
   choice = input("Choose your action:")
   index = int(choice) - 1

   if index == 0:
       dmg = player.generate_damage()
       enemy.take_damage(dmg)
       print("Superman attacked for", dmg, "points of damage.")
   elif index == 1:
       player.choose_magic()
       magic_choice = int(input("Choose type of Magic:")) - 1
       magic_dmg = player.generate_spell_damage(magic_choice)
       spell = player.get_spell_name(magic_choice)
       cost = player.get_spell_mp_cost(magic_choice)

       current_mp = player.get_mp()

       if cost > current_mp:
           print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC )
           continue

       player.reduce_mp(cost)
       enemy.take_damage(magic_dmg)
       print(bcolors.OKBLUE + "\n" + spell + " deals " + str(magic_dmg) + " points of damage" + bcolors.ENDC)

   enemy_choice = 1
   enemy_dmg = enemy.generate_damage()
   player.take_damage(enemy_dmg)
   print("Joker attacked for", enemy_dmg, "points of damage.")

   print("-------------------------")
   print("Joker's HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
   print("Joker's MP:", bcolors.FAIL + str(enemy.get_mp()) + "/" + str(enemy.get_max_mp()) + bcolors.ENDC)

   print("Superman's HP", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
   print("Superman's MP:", bcolors.OKGREEN + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

   if player.hp < 100:
    print(bcolors.WARNING + "You are running low on health" + bcolors.ENDC)

   if player.hp == 0:
    print(bcolors.FAIL + "You are dead! You will respawn to the nearest hospital" + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "YOU WIN" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL +" YOU LOSE " + bcolors.ENDC)
        running = False