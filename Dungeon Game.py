
import random

print("\"Welcome to the Dungeon\"\n Try to Survive")
playOn = True
zombieHealth = 20
playerHealth = 20
playerHealth2 = 20
print("Suddenly a zombie shambles from the corner")
roomsConquered = 0
zombie = True
player = True
fight = True
while fight and zombie and player:
    fight = input("Do you pull out your sword and shield or your bow and arrow?").upper
    if fight == "SWORD" or "SWORD AND SHIELD" or "SWORD SHIELD":
        fight = True
        swordDamage = random.randint(1,10) + 1
        swordHit = random.randint(1,20) + 3
        zombieHit = random.randint(1,20) + 1
        zombieDamage = random.randint(3,8) - 2

        if swordHit == 23:
            print("You cut the Zombie's arm off!!")
            zombieHealth2 = zombieHealth - (swordDamage * 2)
            if zombieHealth2 >= 0:
                zombieHealth = zombieHealth2
                print("The zombie has", zombieHealth2, "health remaining")
            elif zombieHealth2 <= 0:
                print("The zombie died!")
                zombie = False
                break
            fight = input("Do you want to use your sword or your bow?")

        elif swordHit > 8 < 23:
            print("you hit the zombie")
            zombieHealth2 = zombieHealth - (swordDamage)
            print("The zombie has " + str(zombieHealth2) + " health left")
            fight = input("Do you want to use your sword or your bow?")


            if zombieHealth2 > 0:
                zombieHealth = zombieHealth2
                print("The zombie has", zombieHealth2, "health remaining")
            elif zombieHealth2 <= 0:
                print("The zombie died!")
                zombie = False
                break

        elif zombieHit > 12 and zombieHealth > 0:
            playerHealth2 = playerHealth - zombieDamage
            playerHealth = playerHealth2
        else:
            zombie = False
            break
        if zombieDamage > 0:
            print("the zombie hit you")
            playerHealth2 = playerHealth - zombieDamage
            print("You have", playerHealth2, "health left")

        elif swordHit < 8:
            print("you missed...")
            playerHealth2 = playerHealth - zombieDamage
            print("the zombie hit you")
            print("You have", playerHealth2, "health left")
            fight = input("Do you want to use your sword or your bow?1")

            if playerHealth2 >= 0:
                playerHealth2 = playerHealth

            elif playerHealth2 <= 0:
                print("you died...")
                player = False
                break
    elif fight == "BOW" or "BOW AND ARROW" or "BOW ARROW" or "ARROW":
        bowDamage = random.randint(1,7) + 2
        bowHit = random.randint(1,20) + 4
        zombieHit = random.randint(1,20) + 1
        zombieDamage = random.randint(3,8) - 3

        if bowHit >= 21:
            print("You cut the Zombie's arm off!!")
            zombieHealth2 = zombieHealth - (swordDamage * 2)
            if zombieHealth2 > 0:
                zombieHealth = zombieHealth2
                print("The zombie has", zombieHealth2, "health remaining")

            elif zombieHealth2 < 1:
                print("The zombie died!")
                zombie = False
                break


        elif bowHit > 8 < 21:
            print("you hit the zombie")
            zombieHealth2 = zombieHealth - (bowDamage)
            fight = input("Do you want to use your bow or sword?")

            if zombieHealth2 > 0:
                zombieHealth = zombieHealth2
                print("The zombie has", zombieHealth2, "health remaining")
            elif zombieHealth2 <= 0:
                print("The zombie died!")
                zombie = False
                break

        if zombieHit > 12:
          playerHealth2 = playerHealth - zombieDamage
        if zombieHealth2 <= 0:
            zombieDamage = 0
        if zombieHealth2 > 0:
            print("the zombie missed")
            print("You have", playerHealth2, "health left")
        else:
            print("The zombie missed...")

        if bowHit < 8:
            print("you missed...")
            playerHealth2 = playerHealth - zombieDamage
            print("the zombie hit you")
            print("You have", playerHealth2, "health left")

            if playerHealth2 > 0:
                playerHealth2 = playerHealth
            elif playerHealth2 <= 0:
                print("you died...")
                player = False
                break

sword = False
bow = False
helmet = False
weapon = False
if not player:
    print("\"you anger the Old Gods with your incompetence!!!\"")
    playOn = False
if not zombie:
    print("You killed the zombie!!")
    print("\"You please the Old Gods\"")
    reward = input("\"Would you like a weapon or an article of armor?\"").upper()
    if reward == "ARMOR":
        print("you got a mystical helmet, hardened by centuries of combat.")
        weapon = False
        helmet = True
    elif reward == "WEAPON" or "SWORD" or "BOW":
        weapon = input("\"Would you like a bow or a sword?\"").upper()
        if weapon == "BOW":
            print("you got a black bow, emenating a mysterious power.")
            bow = True
            weapon = True
        if weapon == "SWORD":
            print("you got a purple sword, pulsing with energy.")
            sword = True
            weapon = True
        helmet = False
    else:
        print("\"You're dumb.\"")
print("\"The first room of the dungeon has been conquered. "
          "You have started a journey you can not go back on.\"")
print("To your left is a wooden door, oozing with slime. "
          "To your right is an open door, with mysterious noises coming out of it")
door = input("Which way do you choose?").upper()
playerHealth = playerHealth2
dog = False
player = True
slimeHealth = 15
slime = True
if playOn:
    if door == "LEFT":
        print("""You push open the door, slime sticking onto your hand as you take it off.
As you search the room you spot a small gelatinous beast. Be prepared for a fight.""")
        fight = True
        while fight and slime == 1 and player == 1:
            fight = input("Do you pull out your sword and shield or your bow and arrow?").upper
            if fight == "SWORD" or "SWORD AND SHIELD" or "SWORD SHIELD":
                if sword and not helmet:
                    swordDamage = random.randint(1, 10) + 3
                    swordHit = random.randint(1, 20) + 1
                    slimeHit = random.randint(1, 20) + 3
                    slimeDamage = random.randint(1, 5) + 2

                    if swordHit > 10 < 22:
                        print("you hit the slime")
                        slimeHealth2 = slimeHealth - (swordDamage)
                        if slimeHealth2 >= 0:
                            slimeHealth = slimeHealth2
                            print("The slime has", slimeHealth2, "health remaining")

                        elif slimeHealth2 <= 0:
                            print("The slime died!")
                            slime = False

                    if slimeHit > 12:
                        playerHealth2 = playerHealth - zombieDamage
                        playerHealth = playerHealth2
                        if slimeHealth < 1:
                            slimeDamage = 0
                        if slimeHealth > 0:
                            print("the slime hit you")
                            print("You have", playerHealth2, "health left")
                    elif slimeHit <= 12:
                        print("the slime missed")
                        print("You have", playerHealth, "health left")

                    elif swordHit < 10:
                        print("you missed...")
                        playerHealth2 = playerHealth - zombieDamage
                        print("You have", playerHealth2, "health left")

                        if playerHealth2 >= 0:
                            playerHealth2 = playerHealth

                    elif playerHealth2 <= 0:
                        print("you died...")
                        player = False
                elif bow and not helmet:
                    swordDamage = random.randint(1, 10) + 1
                    swordHit = random.randint(1, 20) + 3
                    slimeHit = random.randint(1, 20) + 3
                    slimeDamage = random.randint(1, 5) + 2

                    if swordHit > 8 < 22:
                        print("you hit the slime")
                        slimeHealth2 = slimeHealth - (swordDamage)

                        if slimeHealth2 >= 0:
                            slimeHealth = slimeHealth2
                            print("The slime has", slimeHealth2, "health remaining")
                        elif slimeHealth2 <= 0:
                            print("The slime died!")
                            slime = False

                    if slimeHit > 12:
                        playerHealth2 = playerHealth - zombieDamage
                        playerHealth = playerHealth2
                        if slimeHealth < 1:
                            slime = False
                        if slimeHealth > 0:
                            print("the slime hit you")
                            print("You have", playerHealth2, "health left")

                    elif slimeHit <= 12:
                        print("the slime missed")
                        print("You have", playerHealth, "health left")

                    elif swordHit < 8:
                        print("you missed...")

                    if playerHealth2 >= 0:
                        playerHealth2 = playerHealth

                    elif playerHealth2 <= 0:
                        print("you died...")
                        player = False
                elif not weapon and helmet:
                    swordDamage = random.randint(1, 10) + 3
                    swordHit = random.randint(1, 20) + 1
                    slimeHit = random.randint(1, 20) + 3
                    slimeDamage = random.randint(1, 5) + 2

                    if swordHit > 10 < 22:
                        print("you hit the slime")
                        slimeHealth2 = slimeHealth - swordDamage

                        if slimeHealth2 >= 0:
                            slimeHealth = slimeHealth2
                            print("The slime has", slimeHealth2, "health remaining")
                        elif slimeHealth2 <= 0:
                            print("The slime died!")
                            slime = False

                    if slimeHit > 12:
                        slimeDamage -= 4
                        playerHealth2 = playerHealth - slimeDamage
                        playerHealth = playerHealth2
                        if slimeHealth2 <= 0:
                            slimeDamage = 0
                        if slimeHealth > 0:
                            print("the slime hit you")
                            print("You have", playerHealth2, "health left")
                    else:
                        print("the slime missed")
                        print("You have", playerHealth, "health left")

                    if swordHit < 10:
                        print("you missed...")
                        playerHealth2 = playerHealth - slimeDamage
                        print("You have", playerHealth2, "health left")

                    if playerHealth2 >= 0:
                        playerHealth2 = playerHealth

                    elif playerHealth2 <= 0:
                        print("you died...")
                        player = False
            if fight == "BOW" or "BOW AND ARROW" or "BOW ARROW" or "ARROW":
                if sword and not helmet:
                    swordDamage = random.randint(1, 10) + 3
                    swordHit = random.randint(1, 20) + 1
                    slimeHit = random.randint(1, 20) + 3
                    slimeDamage = random.randint(1, 5) + 2

                    if swordHit > 10 < 22:
                        print("you hit the slime")
                        slimeHealth2 = slimeHealth - (swordDamage)
                        if slimeHealth2 >= 0:
                            slimeHealth = slimeHealth2
                            print("The slime has", slimeHealth2, "health remaining")

                        elif slimeHealth2 <= 0:
                            print("The slime died!")
                            slime = False

                    if slimeHit > 12:
                        playerHealth2 = playerHealth - zombieDamage
                        playerHealth = playerHealth2
                        if slimeHealth < 1:
                            slimeDamage = 0
                        if slimeHealth > 0:
                            print("the slime hit you")
                            print("You have", playerHealth2, "health left")
                    elif slimeHit <= 12:
                        print("the slime missed")
                        print("You have", playerHealth, "health left")

                    elif swordHit < 10:
                        print("you missed...")
                        playerHealth2 = playerHealth - zombieDamage
                        print("You have", playerHealth2, "health left")

                        if playerHealth2 >= 0:
                            playerHealth2 = playerHealth

                    elif playerHealth2 <= 0:
                        print("you died...")
                        player = False
                elif bow and not helmet:
                    swordDamage = random.randint(1, 10) + 1
                    swordHit = random.randint(1, 20) + 3
                    slimeHit = random.randint(1, 20) + 3
                    slimeDamage = random.randint(1, 5) + 2

                    if swordHit > 8 < 22:
                        print("you hit the slime")
                        slimeHealth2 = slimeHealth - (swordDamage)

                        if slimeHealth2 >= 0:
                            slimeHealth = slimeHealth2
                            print("The slime has", slimeHealth2, "health remaining")
                        elif slimeHealth2 <= 0:
                            print("The slime died!")
                            slime = False

                    if slimeHit > 12:
                        playerHealth2 = playerHealth - zombieDamage
                        playerHealth = playerHealth2
                        if slimeHealth < 1:
                            slime = False
                        if slimeHealth > 0:
                            print("the slime hit you")
                            print("You have", playerHealth2, "health left")

                    elif slimeHit <= 12:
                        print("the slime missed")
                        print("You have", playerHealth, "health left")

                    elif swordHit < 8:
                        print("you missed...")

                    if playerHealth2 >= 0:
                        playerHealth2 = playerHealth

                    elif playerHealth2 <= 0:
                        print("you died...")
                        player = False
                elif not weapon and helmet:
                    swordDamage = random.randint(1, 10) + 3
                    swordHit = random.randint(1, 20) + 1
                    slimeHit = random.randint(1, 20) + 3
                    slimeDamage = random.randint(1, 5) + 2

                    if swordHit > 10 < 22:
                        print("you hit the slime")
                        slimeHealth2 = slimeHealth - (swordDamage)

                        if slimeHealth2 >= 0:
                            slimeHealth = slimeHealth2
                            print("The slime has", slimeHealth2, "health remaining")
                        elif slimeHealth2 <= 0:
                            print("The slime died!")
                            slime = False

                    if slimeHit > 12:
                        slimeDamage -= 4
                        playerHealth2 = playerHealth - slimeDamage
                        playerHealth = playerHealth2
                        if slimeHealth2 <= 0:
                            slimeDamage = 0
                        if slimeHealth > 0:
                            print("the slime hit you")
                            print("You have", playerHealth2, "health left")
                    else:
                        print("the slime missed")
                        print("You have", playerHealth, "health left")

                    if swordHit < 10:
                        print("you missed...")
                        playerHealth2 = playerHealth - slimeDamage
                        print("You have", playerHealth2, "health left")

                    if playerHealth2 >= 0:
                        playerHealth2 = playerHealth

                    elif playerHealth2 <= 0:
                        print("you died...")
                        player = False
    if door == "RIGHT":
        print("You walk through the doorway when suddenly you've been pounced upon")
        print("*Woof Woof*")
        print("It's a fluffy dog!")
        # print("") this is where dog ASCII goes
        dogChoice = input("Do you want the dog?").upper()
        if dogChoice == "YES":
            dog = True
            print("The fluffy dog is content.")
        else:
            print("The disappointed dog walks away, never to be seen again.")
        door1 = input("Do you want to go back to the left door?").lower()
        if door1 == "yes":
            door = "LEFT"
            print("""You push open the door, slime sticking onto your hand as you take it off.
            As you search the room you spot a small gelatinous beast. Be prepared for a fight.""")
            fight = True
            while fight and slime == 1 and player == 1:
                fight = input("Do you pull out your sword and shield or your bow and arrow?").upper
                if fight == "SWORD" or "SWORD AND SHIELD" or "SWORD SHIELD":
                    if sword and not helmet:
                        swordDamage = random.randint(1, 10) + 3
                        swordHit = random.randint(1, 20) + 1
                        slimeHit = random.randint(1, 20) + 3
                        slimeDamage = random.randint(1, 5) + 2

                        if swordHit > 10 < 22:
                            print("you hit the slime")
                            slimeHealth2 = slimeHealth - (swordDamage)
                            if slimeHealth2 >= 0:
                                slimeHealth = slimeHealth2
                                print("The slime has", slimeHealth2, "health remaining")

                            elif slimeHealth2 <= 0:
                                print("The slime died!")
                                slime = False

                        if slimeHit > 12:
                            playerHealth2 = playerHealth - zombieDamage
                            playerHealth = playerHealth2
                            if slimeHealth < 1:
                                slimeDamage = 0
                            if slimeHealth > 0:
                                print("the slime hit you")
                                print("You have", playerHealth2, "health left")
                        elif slimeHit <= 12:
                            print("the slime missed")
                            print("You have", playerHealth, "health left")

                        elif swordHit < 10:
                            print("you missed...")
                            playerHealth2 = playerHealth - zombieDamage
                            print("You have", playerHealth2, "health left")

                            if playerHealth2 >= 0:
                                playerHealth2 = playerHealth

                        elif playerHealth2 <= 0:
                            print("you died...")
                            player = False
                    elif bow and not helmet:
                        swordDamage = random.randint(1, 10) + 1
                        swordHit = random.randint(1, 20) + 3
                        slimeHit = random.randint(1, 20) + 3
                        slimeDamage = random.randint(1, 5) + 2

                        if swordHit > 8 < 22:
                            print("you hit the slime")
                            slimeHealth2 = slimeHealth - (swordDamage)

                            if slimeHealth2 >= 0:
                                slimeHealth = slimeHealth2
                                print("The slime has", slimeHealth2, "health remaining")
                            elif slimeHealth2 <= 0:
                                print("The slime died!")
                                slime = False

                        if slimeHit > 12:
                            playerHealth2 = playerHealth - zombieDamage
                            playerHealth = playerHealth2
                            if slimeHealth < 1:
                                slime = False
                            if slimeHealth > 0:
                                print("the slime hit you")
                                print("You have", playerHealth2, "health left")

                        elif slimeHit <= 12:
                            print("the slime missed")
                            print("You have", playerHealth, "health left")

                        elif swordHit < 8:
                            print("you missed...")

                        if playerHealth2 >= 0:
                            playerHealth2 = playerHealth

                        elif playerHealth2 <= 0:
                            print("you died...")
                            player = False
                    elif not weapon and helmet:
                        swordDamage = random.randint(1, 10) + 3
                        swordHit = random.randint(1, 20) + 1
                        slimeHit = random.randint(1, 20) + 3
                        slimeDamage = random.randint(1, 5) + 2

                        if swordHit > 10 < 22:
                            print("you hit the slime")
                            slimeHealth2 = slimeHealth - swordDamage

                            if slimeHealth2 >= 0:
                                slimeHealth = slimeHealth2
                                print("The slime has", slimeHealth2, "health remaining")
                            elif slimeHealth2 <= 0:
                                print("The slime died!")
                                slime = False

                        if slimeHit > 12:
                            slimeDamage -= 4
                            playerHealth2 = playerHealth - slimeDamage
                            playerHealth = playerHealth2
                            if slimeHealth2 <= 0:
                                slimeDamage = 0
                            if slimeHealth > 0:
                                print("the slime hit you")
                                print("You have", playerHealth2, "health left")
                        else:
                            print("the slime missed")
                            print("You have", playerHealth, "health left")

                        if swordHit < 10:
                            print("you missed...")
                            playerHealth2 = playerHealth - slimeDamage
                            print("You have", playerHealth2, "health left")

                        if playerHealth2 >= 0:
                            playerHealth2 = playerHealth

                        elif playerHealth2 <= 0:
                            print("you died...")
                            player = False
                if fight == "BOW" or "BOW AND ARROW" or "BOW ARROW" or "ARROW":
                    if sword and not helmet:
                        swordDamage = random.randint(1, 10) + 3
                        swordHit = random.randint(1, 20) + 1
                        slimeHit = random.randint(1, 20) + 3
                        slimeDamage = random.randint(1, 5) + 2

                        if swordHit > 10 < 22:
                            print("you hit the slime")
                            slimeHealth2 = slimeHealth - (swordDamage)
                            if slimeHealth2 >= 0:
                                slimeHealth = slimeHealth2
                                print("The slime has", slimeHealth2, "health remaining")

                            elif slimeHealth2 <= 0:
                                print("The slime died!")
                                slime = False

                        if slimeHit > 12:
                            playerHealth2 = playerHealth - zombieDamage
                            playerHealth = playerHealth2
                            if slimeHealth < 1:
                                slimeDamage = 0
                            if slimeHealth > 0:
                                print("the slime hit you")
                                print("You have", playerHealth2, "health left")
                        elif slimeHit <= 12:
                            print("the slime missed")
                            print("You have", playerHealth, "health left")

                        elif swordHit < 10:
                            print("you missed...")
                            playerHealth2 = playerHealth - zombieDamage
                            print("You have", playerHealth2, "health left")

                            if playerHealth2 >= 0:
                                playerHealth2 = playerHealth

                        elif playerHealth2 <= 0:
                            print("you died...")
                            player = False
                    elif bow and not helmet:
                        swordDamage = random.randint(1, 10) + 1
                        swordHit = random.randint(1, 20) + 3
                        slimeHit = random.randint(1, 20) + 3
                        slimeDamage = random.randint(1, 5) + 2

                        if swordHit > 8 < 22:
                            print("you hit the slime")
                            slimeHealth2 = slimeHealth - (swordDamage)

                            if slimeHealth2 >= 0:
                                slimeHealth = slimeHealth2
                                print("The slime has", slimeHealth2, "health remaining")
                            elif slimeHealth2 <= 0:
                                print("The slime died!")
                                slime = False

                        if slimeHit > 12:
                            playerHealth2 = playerHealth - zombieDamage
                            playerHealth = playerHealth2
                            if slimeHealth < 1:
                                slime = False
                            if slimeHealth > 0:
                                print("the slime hit you")
                                print("You have", playerHealth2, "health left")

                        elif slimeHit <= 12:
                            print("the slime missed")
                            print("You have", playerHealth, "health left")

                        elif swordHit < 8:
                            print("you missed...")

                        if playerHealth2 >= 0:
                            playerHealth2 = playerHealth

                        elif playerHealth2 <= 0:
                            print("you died...")
                            player = False
                    elif not weapon and helmet:
                        swordDamage = random.randint(1, 10) + 3
                        swordHit = random.randint(1, 20) + 1
                        slimeHit = random.randint(1, 20) + 3
                        slimeDamage = random.randint(1, 5) + 2

                        if swordHit > 10 < 22:
                            print("you hit the slime")
                            slimeHealth2 = slimeHealth - (swordDamage)

                            if slimeHealth2 >= 0:
                                slimeHealth = slimeHealth2
                                print("The slime has", slimeHealth2, "health remaining")
                            elif slimeHealth2 <= 0:
                                print("The slime died!")
                                slime = False

                        if slimeHit > 12:
                            slimeDamage -= 4
                            playerHealth2 = playerHealth - slimeDamage
                            playerHealth = playerHealth2
                            if slimeHealth2 <= 0:
                                slimeDamage = 0
                            if slimeHealth > 0:
                                print("the slime hit you")
                                print("You have", playerHealth2, "health left")
                        else:
                            print("the slime missed")
                            print("You have", playerHealth, "health left")

                        if swordHit < 10:
                            print("you missed...")
                            playerHealth2 = playerHealth - slimeDamage
                            print("You have", playerHealth2, "health left")

                        if playerHealth2 >= 0:
                            playerHealth2 = playerHealth

                        elif playerHealth2 <= 0:
                            print("you died...")
                            player = False
        else:
            print("You continue through the dungeon, never looking back.")
            playOn = False
    if not player:
        print("\"You are a failure to your family and deserve nothing!\"")
    if not slime:
        print("\"You have conquered yet another room in this dungeon\"")
        print("You hear a \'clink\' in the corner of the room. You see its a bag of coins...")
