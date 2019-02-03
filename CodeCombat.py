hero.buildXY("bear-trap", 22, 17)




# This function checks if the enemy is in your attack range.
def inAttackRange(enemy):
    distance = hero.distanceTo(enemy)
    # Almost all swords have attack range of 3.
    if distance <= 3:
        return True
    else:
        return False

# Attack ogres only when they're within reach.
while True:
    # Find the nearest enemy and store it in a variable.
    enemy = hero.findNearestEnemy()
    canAttack = inAttackRange(enemy)
    # Call inAttackRange(enemy), with the enemy as the argument
    # and save the result in the variable canAttack.
    
    # If the result stored in canAttack is True, then attack!
    if canAttack == True:
        if hero.isReady("cleave") == True:
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    pass


    item = hero.findNearestItem()
# Silver coins have a value of 2
if item.type == "coin" and item.value == 2:
    hero.moveXY(item.pos.x, item.pos.y)






while True:
    item = hero.findNearestItem()
    # A silver coin has a value of 2.
    # Collect if item.type is equal to "coin"
    # AND item.value is equal to 2.
    if item.type == "coin" and item.value == 2:
        hero.moveXY(item.pos.x, item.pos.y)
    # A blue gem has a value of 10.
    # Collect if item.type is equal to "gem"
    # AND item.value is equal to 10.
    





while True:
    enemy = hero.findNearestEnemy()
    # With AND, the type is only checked if enemy exists.
    if enemy and enemy.type == "munchkin":
        hero.attack(enemy)
    # Find the nearest item.
    
    # Collect item if it exists and its type is "coin".
    


# Don't insult this tribe of peaceful ogres.

while True:
    item = hero.findNearestItem()
    if item:
        # If item.type IS NOT EQUAL TO "gem"
        if item.type != "gem":
            # Then follow your pet wolf.
            hero.moveXY(pet.pos.x, pet.pos.y)
        # Else:
        
            # Move to the gem's position.
            



# Get two secret true/false values from the wizard.
# Check the guide for notes on how to write logical expressions.
hero.moveXY(14, 24)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()

# If BOTH secretA and secretB are true, take the high path; otherwise, take the low path.
secretC = secretA and secretB
if secretC:
    hero.moveXY(20, 33)
else:
    hero.moveXY(20, 15)
hero.moveXY(26, 24)

# If EITHER secretA or secretB is true, take the high path.

hero.moveXY(38, 24)
# If secretB is NOT true, take the high path.

hero.moveXY(50, 24)




# The function maybeBuildTrap defines TWO parameters!
def maybeBuildTrap(x, y):
    # Use x and y as the coordinates to move to.
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        pass
        # Use buildXY to build a "fire-trap" at the given x and y.
        
while True:
    # This calls maybeBuildTrap, with the coordinates of the top entrance.
    maybeBuildTrap(43, 50)
    
    # Now use maybeBuildTrap at the left entrance!
    
    # Now use maybeBuildTrap at the bottom entrance!
    
    

    # Collect all the coins in each meadow.
# Use flags to move between meadows.
# Press Submit when you are ready to place flags.

while True:
    flag = hero.findFlag()
    if flag:
        pass  # `pass` is a placeholder, it has no effect.
        # Pick up the flag.
        
    else:
        # Automatically move to the nearest item you see.
        item = hero.findNearestItem()
        if item:
            position = item.pos
            x = position.x
            y = position.y
            hero.moveXY(x, y)


# Put flags where you want to build traps.
# When you're not building traps, pick up coins!

while True:
    flag = hero.findFlag()
    if flag:
        # How do we get flagX and flagY from the flag's pos?
        # (Look below at how to get x and y from items.)
        
        
        hero.buildXY("fire-trap", flagX, flagY)
        hero.pickUpFlag(flag)
    else:
        item = hero.findNearestItem()
        if item:
            itemPos = item.pos
            itemX = itemPos.x
            itemY = itemPos.y
            hero.moveXY(itemX, itemY)


# If you try to attack a distant enemy, your hero will charge toward it, ignoring all flags.
# You'll need to make sure you only attack enemies who are close to you!

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    
    if flag:
        # Pick up the flag.
        
        hero.say("I should pick up the flag.")
    elif enemy:
        # Only attack if the enemy distance is < 10 meters
        
        hero.attack(enemy)


# You can use flags to choose different tactics.
# In this level, the green flag will mean you want to move to the flag.
# The black flag means you want to cleave at the flag.
# The doctor will heal you at the Red X

while True:
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    nearest = hero.findNearestEnemy()
    
    if green:
        hero.pickUpFlag(green)
    elif black and hero.isReady("cleave"):
        hero.pickUpFlag(black)
        # Cleave!
        
    elif nearest and hero.distanceTo(nearest) < 10:
        # Attack!
        
        pass

# You can use flags to choose different tactics.
# In this level, the green flag will mean you want to move to the flag.
# The black flag means you want to cleave at the flag.
# The doctor will heal you at the Red X

while True:
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    nearest = hero.findNearestEnemy()
    
    if green:
        hero.pickUpFlag(green)
    elif black and hero.isReady("cleave"):
        hero.pickUpFlag(black)
        # Cleave!
        
    elif nearest and hero.distanceTo(nearest) < 10:
        # Attack!
        
        pass




reen = hero.findFlag("green")
    black = hero.findFlag("black")
    violet = hero.findFlag("violet")
    enemy = hero.findNearestEnemy()
    
    if green:
        hero.pickUpFlag(green)
        enemy = hero.findNearestEnemy()
        if enemy and enemy.type == "ogre":
            if hero.isReady("cleave"):
             hero.cleave(enemy)
            hero.attack(enemy)

            else:
            hero.moveXY(18, 30)



# Use "if" and "else if" to handle any situation.
# Put it all together to defeat enemies and pick up coins!
# Make sure you bought great armor from the item shop! 400 health recommended.

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()

    if flag:
        # What happens when I find a flag?
        
    elif enemy:
        # What happens when I find an enemy?
        
    elif item:
        # What happens when I find an item?
        
        

        # Let yaks get close, then move 10m right to dodge.
# Dodge 4 yaks to complete the level.

while True:
    # Get hero's current x and y position.
    x = hero.pos.x
    y = hero.pos.y
    
    # Find the nearest yak.
    yak = hero.findNearestEnemy()
    
    # If the distanceTo the yak is less than 10:
    if hero.distanceTo(yak) < 10:
        # To move right, add 10 to hero's x position.
        
        # Use moveXY(x, y) to move!
        
        pass
    

    # Move right to reach the oasis,
# Move left to avoid nearby yaks.
while True:
    x = hero.pos.x
    y = hero.pos.y
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        # Subtract 10 from x to move left.
        
        # Use moveXY to move to the new x, y position.
        
        pass
    else:
        # Add 10 to x to move right.
        
        # Use moveXY to move to the new x, y position.
        
        pass


# Keep moving right, but adjust up and down as you go.

while True:
    enemy = hero.findNearestEnemy()
    xPos = hero.pos.x + 5
    yPos = 17
    if enemy:
        # Adjust y up or down to get away from yaks.
        if enemy.pos.y > hero.pos.y:
            # If the Yak is above you, subtract 3 from yPos.
            
            pass
        elif enemy.pos.y < hero.pos.y:
            # If the Yak is below you, add 3 to yPos.
            
            pass
    hero.moveXY(xPos, yPos)


# Get to the oasis. Watch out for new enemies: ogre scouts!
# Go up and right by adding to the current X and Y position.

while True:
    # If there's an enemy, attack.
    
    # Else, keep moving up and to the right. 
    
    pass
    


    # Use "fire-trap"s to defeat the ogres.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # If the enemy is to the left of the hero:
        if enemy.pos.x < hero.pos.x:
            # buildXY a "fire-trap" on the left X.
            
            pass
        # If the enemy is to the right of the hero:
        elif enemy.pos.x > hero.pos.x:
            # buildXY a "fire-trap" on the right X.
            
            pass
        # If the enemy is below the hero:
        elif enemy.pos.y < hero.pos.y:
            # buildXY a "fire-trap" on the bottom X.
            
            pass
        # If the enemy is above the hero:
        elif enemy.pos.y > hero.pos.y:
            # buildXY a "fire-trap" on the top X.
            
            pass
    # Move back to the center.
    hero.moveXY(40, 34)


# Move right, to the oasis.
# Build a "fence" above or below when you see a yak.

while True:
    yak = hero.findNearestEnemy()
    if yak:
        # If yak.pos.y is greater than hero.pos.y
        
            # buildXY a "fence" 10m below the yak.
            
        # else: 
        
            # buildXY a "fence" 10m above the yak.
            
        pass
    else:
        # moveXY right 10m towards the oasis.
        
        pass


# Lure the ogres into a trap. These ogres are careful.
# They will only follow if the hero is injured.

# This function checks the hero's health 
# and returns a Boolean value.
def shouldRun():
    if hero.health < hero.maxHealth / 2:
        return True
    else:
        return False

while True:
    # Move to the X only if shouldRun() returns True
    
    hero.moveXY(75, 37)
    # Else, attack!
    

    # Ask the healer for help when you're under one-half health.

while True:
    currentHealth = hero.health
    healingThreshold = hero.maxHealth / 2
    # If your current health is less than the threshold,
    # move to the healing point and say, "heal me".
    # Otherwise, attack. You'll need to fight hard!
    
    

    # Use your new skill to choose what to do: hero.time

while True:
    # If it's the first 10 seconds, attack.
    if hero.time < 10:
        
        pass
    # Else, if it's the first 35 seconds, collect coins.
    elif hero.time < 35:
        
        pass
    # After 35 seconds, attack again!
    else:
        
        pass


# Collect 25 gold, and then tell Naria the total.
# Use break to stop collecting when totalGold >= 25.

totalGold = 0
while True:
    coin = hero.findNearestItem()
    if coin:
        # Pick up the coin.
        
        # Add the coin's value to totalGold.
        # Get its value with:  coin.value
        
        pass
    if totalGold >= 25:
        # This breaks out of the loop to run code at the bottom.
        # The loop ends, code after the loop will run.
        break

# Done collecting gold!
hero.moveXY(58, 33)
# Go to Naria and say how much gold you collected.



# We are field testing a new battle unit: the decoy.
# Build 4 decoys, then report the total to Naria.

decoysBuilt = 0
while True:
    coin = hero.findNearestItem()
    
    if coin:
        # Collect the coin!
        
        pass
    # Each decoy costs 25 gold.
    # If hero.gold is greater than or equal to 25:
    
        # buildXY a "decoy"
        
        # Add 1 to the decoysBuilt count.
        
    if decoysBuilt == 4:
        # Break out of the loop when you have built 4.
        
        pass
    
hero.say("Done building decoys!")
hero.moveXY(14, 36)
# Say how many decoys you built.



if enemy:
        if x > 80 and y > 72:
            if enemy and enemy.type == "sand-yak":
                hero.moveXY(30, 108)
            else:
                hero.attack(enemy)
        if x < 80 and y > 72:
            if enemy and enemy.type == "sand-yak":
                hero.moveXY(30, 32)
            else:
                hero.attack(enemy)
        if x > 80 and y < 72:
            if enemy and enemy.type == "sand-yak":
                hero.moveXY(130, 108)
            else:
                hero.attack(enemy)
        if x < 80 and y < 72:
            if enemy and enemy.type == "sand-yak":
                hero.moveXY(130, 32)
            else:
                hero.attack(enemy)








    if enemy and enemy.type == "sand-yak":
        if x > 80 and y > 72:
            hero.moveXY(30, 108)
        if x < 80 and y > 72:
            hero.moveXY(30, 32)
        if x > 80 and y < 72:
            hero.moveXY(130, 108)
        if x < 80 and y < 72:
            hero.moveXY(130, 32)
    elif enemy and enemy.tpye != "sand-yak":
        if d > 20:
            if x > 80 and y > 72:
                hero.moveXY(30, 108)
            if x < 80 and y > 72:
                hero.moveXY(30, 32)
            if x > 80 and y < 72:
                hero.moveXY(130, 108)
            if x < 80 and y < 72:
                hero.moveXY(130, 32)
        else:
            hero.attack(enemy)
            

        if x > 80 and y > 72:
            hero.moveXY(25, 115)
        if x < 80 and y > 72:
            hero.moveXY(30, 32)
        if x > 80 and y < 72:
            hero.moveXY(130, 108)
        if x < 80 and y < 72:
            hero.moveXY(130, 32)


            if x > 80 and y > 72:
                hero.moveXY(30, 108)
            if x < 80 and y > 72:
                hero.moveXY(30, 32)
            if x > 80 and y < 72:
                hero.moveXY(130, 108)
            if x < 80 and y < 72:
                hero.moveXY(130, 32)

# Race munchkins to the water distilled by Omarn Brewstone!
# Use the `continue` statement to avoid poison.
while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    
    # If there is no enemy, continue out of the loop.
    if not enemy:
        continue
    
    # If there is no item, ask for a potion then continue:
    if not item:
        hero.say("Give me a drink!")
        continue
    
    # If the item.type "poison", continue out of the loop.
    
    # At this point, the potion must be a bottle of water
    # so moveXY to the potion, then back to the start!





                if enemy and enemy.type == "brawler":
                break



                 and enemy.type != "brawler"





# Stay alive for two minutes.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

while True:
    # if hero.health < 200:
    x = hero.pos.x
    y = hero.pos.y
    enemy = hero.findNearestEnemy()
    if enemy:
        d = hero.distanceTo(enemy)
        while True:
            if enemy and enemy.type != "sand-yak" and enemy.type != "brawler":
                if d > 40:
                    break
                if enemy.health > 1 and d < 30:
                    hero.attack(enemy)
                    enemy = hero.findNearestEnemy()
            if enemy and enemy.health < 1 and d < 30:
                break
            if enemy and enemy.type == "sand-yak":
                break
            if enemy and enemy.type == "brawler":
                if d < 10:
                    move()
                else:
                    break
            if not enemy:
                break
def move():
    if x > 29 and y > 104:
        hero.moveXY(x - 2.5, y + .25)
    if x < 114 and y < 38:
        hero.moveXY(x + 2.5, y - .25)
    if x > 114 and y < 104:
        hero.moveXY(x + .25, y + 2.5)
    if x < 29 and y > 38 :
        hero.moveXY(x - .25, y - 2.5)
move()       
            

          
          hero.moveXY(x - 10, y + 1)



# Stay alive for two minutes.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

while True:
    # if hero.health < 200:
    x = hero.pos.x
    y = hero.pos.y
    enemy = hero.findNearestEnemy()
    def mov():
        if x >= 29 and y > 104:
            hero.move({"x": 29, "y": 115})
        if x < 114 and y < 38:
            hero.move({"x": 115, "y": 35})
        if x > 114 and y < 104:
            hero.moveXY(x + 1, y + 10)
        if x <= 29 and y > 38 :
            hero.move({"x": 23, "y": 28})
    while True:
        if enemy:
            d = hero.distanceTo(enemy)
        if enemy and enemy.type != "sand-yak" and enemy.type != "brawler":
            if d > 40:
                break
            if enemy.health > 1 and d < 40:
                hero.attack(enemy)
                enemy = hero.findNearestEnemy()
            if enemy and enemy.health < 1 and d < 30:
                break
        if enemy and enemy.type == "sand-yak":
            break
        if enemy and enemy.type == "brawler":
            if d < 10:
                mov()
            else:
                break
        if not enemy:
            break
    mov()
    




# Stay alive for two minutes.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

while True:
    # if hero.health < 200:
    x = hero.pos.x
    y = hero.pos.y
    enemy = hero.findNearestEnemy()
    enemies = hero.findEnemies()
    if enemies:
        d = hero.distanceTo(enemies)
    def mov():
        if x >= 29 and y > 104:
            hero.move({"x": 29, "y": 115})
        if x < 114 and y < 38:
            hero.move({"x": 115, "y": 35})
        if x > 114 and y < 104:
            hero.moveXY(x + 1, y + 10)
        if x <= 29 and y > 38 :
            hero.move({"x": 23, "y": 28})
    while True:
        if enem:
            d = hero.distanceTo(enemy)
        if enemy and enemy.type != "sand-yak" and enemy.type != "brawler":
            if d > 40:
                break
            if enemy.health > 1 and d < 40:
                hero.attack(enemy)
                enemy = hero.findNearestEnemy()
            if enemy and enemy.health < 1 and d < 30:
                break
        if enemy and enemy.type == "sand-yak":
            break
        if enemy and enemy.type == "brawler":
            if d < 10:
                mov()
            else:
                break
        if not enemy:
            break
    mov()
    

    

throwers = hero.findByType("thrower")
    if throwers[0]:
        dt = hero.distanceTo(throwers[0])
        if dt < 40:
            hero.attack(throwers[0])
    shamans = hero.findByType("shaman")
    if shamans[0]:
        ds = hero.distanceTo(shamans[0])
        if ds < 40:
            hero.attack(shamans[0])


# Stay alive for two minutes.
# If you win, it gets harder (and more rewarding).
# If you lose, you must wait a day before you can resubmit.
# Remember, each submission gets a new random seed.

while True:
    # if hero.health < 200:
    x = hero.pos.x
    y = hero.pos.y
    enemy = hero.findNearestEnemy()
    enemies = hero.findEnemies()
    throwers = hero.findByType("thrower")
    shamans = hero.findByType("shaman")
    fangs = hero.findByType("fangrider")
    if enemy:
        d = hero.distanceTo(enemy)
    throwers = hero.findByType("thrower")
    if throwers[0]:
        dt = hero.distanceTo(throwers[0])
        if dt < 40:
            hero.attack(throwers[0])
            throwers = hero.findByType("thrower")
            shamans = hero.findByType("shaman")
            fangs = hero.findByType("fangrider")
    shamans = hero.findByType("shaman")
    if shamans[0]:
        ds = hero.distanceTo(shamans[0])
        if ds < 40:
            hero.attack(shamans[0])
            throwers = hero.findByType("thrower")
            shamans = hero.findByType("shaman")
            fangs = hero.findByType("fangrider")
    fangs = hero.findByType("fangrider")
    if fangs[0]:
        ds = hero.distanceTo(fangs[0])
        if ds < 40:
            hero.attack(fangs[0])
            throwers = hero.findByType("thrower")
            shamans = hero.findByType("shaman")
            fangs = hero.findByType("fangrider")
    def mov():
        if x >= 29 and y > 100:
            hero.move({"x": 29, "y": 115})
        if x < 114 and y < 38:
            hero.move({"x": 115, "y": 35})
        if x > 114 and y < 104:
            hero.moveXY(x + 1, y + 10)
        if x <= 29 and y > 38 :
            hero.move({"x": 23, "y": 28})
    while True:
        if enemy:
            d = hero.distanceTo(enemy)
        if enemy and enemy.type != "sand-yak" and enemy.type != "brawler":
            if d > 20:
                break
            if enemy.health > 1 and d < 20:
                hero.attack(enemy)
                enemy = hero.findNearestEnemy()
            if enemy and enemy.health < 1 and d < 20:
                break
        if enemy and enemy.type == "sand-yak":
            break
        if enemy and enemy.type == "brawler":
                break
        if not enemy:
            break
    mov()



shamans = hero.findByType("shaman")
        fangs = hero.findByType("fangrider")
        if throwers[0]:
            dt = hero.distanceTo(throwers[0])
            if dt < 40:
                hero.attack(throwers[0])
                throwers = hero.findByType("thrower")
                shamans = hero.findByType("shaman")
                fangs = hero.findByType("fangrider")
        if not throwers[0]:
            break
        if shamans[0]:
            ds = hero.distanceTo(shamans[0])
            if ds < 40:
                hero.attack(shamans[0])
                throwers = hero.findByType("thrower")
                shamans = hero.findByType("shaman")
                fangs = hero.findByType("fangrider")
        if not shamans[0]:
            break
        if fangs[0]:
            df = hero.distanceTo(fangs[0])
            if df < 40:
                hero.attack(fangs[0])
                throwers = hero.findByType("thrower")
                shamans = hero.findByType("shaman")
                fangs = hero.findByType("fangrider")
        if not fangs[0]:
            break



if melee[0].type != "sand-yak" and melee[0].type != "brawler":
                if d >= 10:
                    break
                if near.health > 1 and d < 27:
                    hero.attack(near)
                    near = hero.findNearestEnemy()
                if near and near.health < 1 and d < 27:
                    break
            if near and near.type == "sand-yak":
                break
    
    
    
    
    
    
    
    
    
    
    def nearenemy():
        if near:
            d = hero.distanceTo(near)
            if near.type != "sand-yak" and near.type != "brawler":
                if d >= 28:
                    break
                if near.health > 1 and d < 27:
                    hero.attack(near)
                    near = hero.findNearestEnemy()
                if near and near.health < 1 and d < 27:
                    break
            if near and near.type == "sand-yak":
                break
            if near and near.type == "brawler":
                antibrawl()
            if d >= 28:
                break
        if not near:
            pass


def antibrawl():
        if brawlers[0]:
            db = hero.distanceTo(brawlers[0])
            if db <= 15:
                if brawlers[0].pos.x > 42 and brawlers[0].pos.y < 42:
                    hero.move({"x": 25, "y": 25})
                if brawlers[0].pos.x < 42  and brawlers[0].pos.y < 100:
                    hero.move({"x": 25, "y": 116})
                if brawlers[0].pos.x < 115 and brawlers[0].pos.y > 100:
                    hero.move({"x": 135, "y": 116})
                if brawlers[0].pos.x > 114 and brawlers[0].pos.y > 42:
                    hero.move({"x": 135, "y": 25})
            if db > 15:
                break
            else:
                break
        if not brawlers[0]:
            break
    while True:
        nearenemy()
        





    hero.say(melee[0])
    def run(e):
        melee = hero.findByType("scout" or "ogre")
        throwers = hero.findByType("thrower" or "shaman" or "fangrider")
        brawlers = hero.findByType("brawler")
        if e.pos.x <=40 and e.pos.y <= 120:
            hero.move({"x": 120, "y": 25})
        if e.pos.x >=113 and e.pos.y <= 120:
            hero.move({"x": 25, "y": 105})
        if 113 > e.pos.x > 40 and e.pos.y > 100:
            hero.move({"x": 25, "y": 25})
        if 113 > e.pos.x > 40 and e.pos.y < 45:
            hero.move({"x": 120, "y": 105})
        melee = hero.findByType("scout" or "ogre")
        throwers = hero.findByType("thrower" or "shaman" or "fangrider")
        brawlers = hero.findByType("brawler")
    while True:
        melee = hero.findByType("scout" or "ogre")
        throwers = hero.findByType("thrower" or "shaman" or "fangrider")
        brawlers = hero.findByType("brawler")
        # First check for those big brawlers:
        if brawlers[0]:
            db = hero.distanceTo(brawlers[0])
            if db < 15:
                pass
            if db >= 15:
                return
        # Then check for long distance fighters:
        if throwers[0]:
            dt = hero.distanceTo(throwers[0])
            if dt <= 27:
                hero.attack(throwers[0])
            if dt > 27:
                return
        # Finally check for melee fighters:
        if melee[0]:
            dm = hero.distanceTo(melee[0])
            if dm < 10:
                if melee[0].health > 0:
                    hero.attack(melee[0])
        if not melee[0] or throwers[0]:
            return
    def mov():
        melee = hero.findByType("scout" or "ogre")
        throwers = hero.findByType("thrower" or "shaman" or "fangrider")
        brawlers = hero.findByType("brawler")
        if hx >= 40 and hy >= 100:
            hero.move({"x": 25, "y": 100})
            return
        if hx <= 115 and hy <= 40:
            hero.move({"x": 120, "y": 25})
            return
        if hx >= 115 and hy <= 105:
            hero.move({"x": 120, "y": 110})
            return
        if hx <= 40 and hy >= 40 :
            hero.move({"x": 25, "y": 25})
            return   
    lookout()




# First, defeat 6 ogres.
# Then collect coins until you have 30 gold.

# This variable is used for counting ogres.
defeatedOgres = 0

# This loop is executed while defeatedOgres is less than 6.
while defeatedOgres < 6:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        defeatedOgres += 1
    else:
        hero.say("Ogres!")

# Move to the right side of the map.
hero.moveXY(49, 36)

# This loop is executed while you have less than 30 gold.
while hero.gold < 30:
    # Find and collect coins.
    
    # Remove this say() message.
    hero.say("I should gather coins!")

# Move to the exit.
hero.moveXY(76, 32)




# while-loops repeat until the condition is false.

ordersGiven = 0
while ordersGiven < 5:
    # Move down 10 meters.
    
    # Order your ally to "Attack!" with hero.say
    # They can only hear you if you are on the X.
    hero.say("Attack!")

    # Be sure to increment ordersGiven!
    

while True:
    enemy = hero.findNearestEnemy()
    # When you're done giving orders, join the attack.
    




hero.moveXY(10, 50)
x = hero.pos.x
y = hero.pos.y
hero.say("Attack!")
orders = 1
while orders < 5:
    x = hero.pos.x
    y = hero.pos.y
    hero.moveXY(x+0, y-10)
    hero.say("Attack!")
    orders += 1
hero.moveXY(51, 32)
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    



# Use a while to loop until you have counted 10 attacks.

attacks = 0
while attacks < 10:
    # Attack the nearest enemy!
    
    # Incrementing means to increase by 1.
    # Increment the `attacks` variable.
    attacks += 1

# When you're done, retreat to the ambush point.
hero.say("I should retreat!") #∆ Don't just stand there blabbering!





# Use while loops to pick out the ogre

while True:
    enemies = hero.findEnemies()
    enemyIndex = 0

    # Wrap this logic in a while loop to attack all enemies.
    # Find the array's length with:  len(enemies)

    enemy = enemies[enemyIndex]
    # "!=" means "not equal to."
    if enemy.type != "sand-yak":
        # While the enemy's health is greater than 0, attack it!
        
        pass

    # Between waves, move back to the center.
    
    
