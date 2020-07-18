import random

from rpg.classes.Enemy import Enemy, bcolors
from rpg.classes.inventory import Item
from rpg.classes.magic import Spell

print(bcolors.FAIL + bcolors.BOLD + "JOKER vs SUPERMAN" + " Battle for Gotham" + bcolors.ENDC)

# Creating Black magic
fire = Spell("Fire", 50, 150, "black")
freeze = Spell("Freeze", 70, 200, "black")
water = Spell("Water", 100, 300, "black")
blizzard = Spell("Blizzard", 125, 3500, "black")

# Creating White magic
cure = Spell("Cure", 80, 700, "white")
medkit = Spell("Med Kit", 150, 1500, "white")

# Creating Recovery Items
potion = Item("Paracetamol", "potion", "Heals 100 HP", 100)
hipotion = Item("Lucozade", "potion", "Recovers 500 HP", 500)
superpotion = Item("Refnol", "tonic", "Recovers 100 MP", 100)
elixir = Item("Aspirin", "elixir", "Fully restores HP ", 250)
# Creating Attack items
grenade = Item("Grenade", "attack", "Deals 300 damage", 300)
knife = Item("Knife", "attack", "deals 150 damage", 150)

player_spells = [fire, freeze, water, blizzard, cure, medkit]
enemy_spells = [fire, blizzard, medkit]
player_items = [{"Item": potion, "quantity": 10}, {"Item": hipotion, "quantity": 5},
                {"Item": superpotion, "quantity": 5}, {"Item": grenade, "quantity": 5},
                {"Item": elixir, "quantity": 5}, {"Item": knife, "quantity": 5}]

# Instantiate Players
player1 = Enemy("Superman", 13050, 300, 480, 250, player_spells, player_items)
player2 = Enemy("Batman  ", 12860, 300, 330, 250, player_spells, player_items)
player3 = Enemy("Flash   ", 21000, 200, 210, 250, player_spells, player_items)

enemy1 = Enemy("Joker   ", 5800, 450, 850, 222, enemy_spells, [])
enemy2 = Enemy("Luthor  ", 4030, 400, 450, 300, enemy_spells, [])
enemy3 = Enemy("Lena    ", 4000, 400, 450, 300, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

while running:
    print("=====================")

    print(bcolors.BOLD + "NAME                   HP                                     MP      " + bcolors.ENDC)
    for player in players:
        player.get_stats()

    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(bcolors.BOLD + "NAME                   HP                                        "
                         "                    MP      " + bcolors.ENDC)
    for enemy in enemies:
        enemy.get_enemy_stats()

    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    for player in players:
        player.choose_action()
        choice = input("    Choose your action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)

            print(player.name.replace(" ", ""), "deals", dmg,
                  "points of damage to", enemies[enemy].name.replace(" ", ""), )

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " is dead.")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose type of Magic:")) - 1

            if magic_choice == -1:
                continue
            elif magic_choice >= 7:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_spell_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals " + players[player].name + str(magic_dmg) + " HP " +
                      bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg) + " points of damage to"
                      + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " is dead.")
                    del enemies[enemy]
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose Item: ")) - 1

            if item_choice == -1:
                continue
            elif item_choice >= 8:
                continue

            item = player.items[item_choice]["Item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n", "None left...", bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + item.name + " heals for", str(item.prop), "HP", bcolors.ENDC)
            elif item.type == "elixir":

                if item.name == "Aspirin":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + item.name + " fully restores HP/MP", bcolors.ENDC)
            elif item.type == "tonic":
                player.mp = player.maxmp
                print(bcolors.OKGREEN + item.name + " heals for", str(item.prop), "MP", bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name + " deals ", str(item.prop), "points of damage to",
                      enemies[enemy].name.replace(" ", ""), bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " is dead.")
                    del enemies[enemy]

    # Enemy attacks
    print("-----------------------------------------")
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            target = random.randrange(0, 3)
            enemy_dmg = enemies[0].generate_damage()
            players[target].take_damage(enemy_dmg)

            print(bcolors.FAIL, enemy.name.replace(" ", ""), " attacks", players[target].name.replace(" ", ""),
                  enemy_dmg,
                  "points of damage.", bcolors.ENDC)
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals " + enemy.name + str(magic_dmg) + " HP " +
                      bcolors.ENDC)
            elif spell.type == "black":

                target = random.randrange(0, 3)

                players[target].take_damage(magic_dmg)

                print(bcolors.OKBLUE + enemy.name.replace(" ", "") + "'s " + spell.name + " deals " + str(magic_dmg) +
                      " points of damage to " + players[target].name.replace(" ", "") + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(player.name.replace("   ", "") + " is dead.")
                    del players[target]
                    # print(enemy.name + " used", spell, ", damage costs", magic_dmg)

            current_mp = enemy.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            defeated_enemies = 0
            defeated_players = 0

            for enemy in enemies:
                if enemy.get_hp() == 0:
                    defeated_enemies += 1
            for player in players:
                if player.get_hp() == 0:
                    defeated_players += 1

            if defeated_enemies == 2:
                print(bcolors.FAIL + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)
                print(bcolors.OKGREEN + "YOU WIN" + bcolors.ENDC)
                running = False
            elif player.get_hp() == 2:
                print(bcolors.FAIL + players[player].name + bcolors.ENDC)
                print(bcolors.FAIL + " YOU LOSE " + bcolors.ENDC)
                running = False
