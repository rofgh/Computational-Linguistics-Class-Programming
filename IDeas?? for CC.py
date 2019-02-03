    IDeas??


# Attack the enemy that's farthest away first.

while True:
    farthest = None
    maxDistance = 0
    enemyIndex = 0
    enemies = hero.findEnemies()

    # Look at all the enemies to figure out which one is farthest away.
    while enemyIndex < len(enemies):
        target = enemies[enemyIndex]
        enemyIndex += 1

        # Is this enemy farther than the farthest we've seen so far?
        distance = hero.distanceTo(target)
        if distance > maxDistance:
            maxDistance = distance
            farthest = target

    if farthest:
        # Take out the farthest enemy!
        # Keep attacking the enemy while its health is greater than 0.
        while farthest.health > 0:
            hero.attack(farthest)
        pass




# This field is covered in firetraps.  Thankfully we've sent a scout ahead to find a path.  He left coins along the path so that if we always stick to the nearest coin, we'll avoid the traps.

# This canyon seems to interfere with your findNearest glasses!
# You'll need to find the nearest coins on your own.

while True:
    coins = hero.findItems()
    coinIndex = 0
    nearest = None
    nearestDistance = 9999
    
    # Loop through all the coins to find the nearest one.
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        coinIndex += 1
        distance = hero.distanceTo(coin)
        # If this coin's distance is less than the nearestDistance
        
            # Set nearest to coin
            
            # Set nearestDistance to distance
            
            
    # If there's a nearest coin, move to its position. You'll need moveXY so you don't cut corners and hit a trap.



# You have one arrow. Make it count!

# This should return the enemy with the most health.
def findStrongestEnemy(enemies):
    strongest = None
    strongestHealth = 0
    enemyIndex = 0
    # While enemyIndex is less than the length of enemies:
    
        # Set an enemy variable to enemies[enemyIndex]
        
        # If enemy.health is greater than strongestHealth
        
            # Set `strongest` to enemy
            # Set strongestHealth to enemy.health
            
        # Increment enemyIndex
        

    return strongest

enemies = hero.findEnemies()
leader = findStrongestEnemy(enemies)
if leader:
    hero.say(leader)

enemyIndex = 0
enemies = hero.findEnemies()
bigH = 0

while enemyIndex < len(enemies):
    enemy = enemies[enemyIndex]
    h = enemy.health
    if h > bigH:
        bigH = h
        bigMan = enemy
    enemyIndex += 1
hero.say(bigMan)


while True:
    coinIndex = 0
    coins =  hero.findItems()

    while coinIndex < len(coins):
        coin = coins[coinIndex]
        if coin.value > 2:
            hero.moveXY(coin.pos.x, coin.pos.y)
        coinIndex += 1


        
        for x in coins:
            if x.value > 2:
                hero.moveXY(x.pos.x, x.pos.y)




VALUE OVER DISTANCE  AND LARGEST ENEMY SCRIPTS:


# Claim the coins while defeating the marauding ogres.

def findMostHealth(enemies):
    target = None
    targetHealth = 0
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        if enemy.health > targetHealth:
            target = enemy
            targetHealth = enemy.health
        enemyIndex += 1
    return target

def valueOverDistance(item):
    return item.value / hero.distanceTo(item)

# Return the item with the highest valueOverDistance(item)
def findBestItem(items):
    bestItem = None
    bestValue = 0
    itemsIndex = 0
    
    # Loop over the items array.
    # Find the item with the highest valueOverDistance()
    while itemsIndex < len(coins):
        gem = coins[itemsIndex]
        value = valueOverDistance(gem)
        if value > bestValue:
            bestValue = value
            bestItem = gem
        itemsIndex += 1
    return bestItem

while True:
    enemies = hero.findEnemies()
    enemy = findMostHealth(enemies)
    if enemy and enemy.health > 15:
        while enemy.health > 0:
            hero.attack(enemy)
    else:
        coins = hero.findItems()
        coin = None
        coin = findBestItem(coins)
        if coin:
            hero.moveXY(coin.pos.x, coin.pos.y)




enemyIndex = 0
towerHealthIndicator = 0
    
while True:
    #friends = hero.findFriends()
    tower = hero.findByType("arrow-tower")
    big = hero.findByType("ogre") + hero.findByType("fangrider")
    # big = ogre + riders
    enemy = hero.findNearestEnemy()
    if enemy:
        de = hero.distanceTo(enemy)
    enemies = hero.findEnemies()
    coin = hero.findNearestItem()
    # coins =  hero.findItems()
    towerIndex = 0
    totalTowerHealth = 0
    while towerIndex < len(tower):
        t = tower[towerIndex]
        h = t.health
        totalTowerHealth += h
        towerIndex += 1
    if totalTowerHealth < 1000 and towerHealthIndicator == 0:
        hero.say("2/3")
        towerHealthIndicator = 1
    if totalTowerHealth < 500 and towerHealthIndicator == 1:
        hero.say("1/3")
        towerHealthIndicator = 2



# This level is intended to be for advanced players. The solution should be pretty complex with a lot of moving parts. It might also be a bit of a gear check unless you use creative methods.
# You need to make your way to the first trial (Oasis of Marr) defeating enemies along the way. When you reach it, pick all the mushrooms to trigger the trial to begin. If you survive the onslaught, make your way to the next Oasis for the second trial, then the Temple. When all trials are complete you will have to face the final boss. Good luck!
# HINT: Glasses with a high visual range help tremendously on this level so buy the best you can get.
# HINT: the unit 'type' for the oasis guardians is 'oasis-guardian'

# # 544 (Started against 1st Guardian attack) ##

## Not really being used right now:##
totalKillIndex = 0
## Also not being used at the moment ##
allKillIndex = 0
## 1:move to 2nd oasis;2:move to 3rd oasis;3:move to center area##
guardianKillIndex = 0

while True:
    ##Find and Name Items##
    itemIndex = 0
    items = hero.findItems()
    closestItemDistance = 9999
    while itemIndex < len(items):
        item = items[itemIndex]
        di = hero.distanceTo(item)
        if di < closestItemDistance:
            closestItemDistance = di
            closestItem = item
        itemIndex += 1
    
    ##Find and Name Enemies##
    enemiesIndex = 0
    enemies = hero.findEnemies()
    enemiesDistance = 9999
    closestEnemyDistance = 9999
    nearest = None
    currentGuardian = None
    while enemiesIndex < len(enemies):
        e = enemies[enemiesIndex]
        de = hero.distanceTo(e)
        if e.type == "oasis-guardian":
            currentGuardian = e
        if de < enemiesDistance:
            enemiesDistance = de
            if de < 40:
                nearest = e
        enemiesIndex += 1
        
    ##If there is a nearest enemy, kill 'im##
    if nearest:
        closestEnemyDistance = hero.distanceTo(nearest)
        if closestEnemyDistance < closestItemDistance:
            hero.attack(nearest)
            if nearest.health < 0:
                totalKillIndex += 1
            ##Guardian monitoring##
            if currentGuardian and currentGuardian.health < 0:
                guardianKillIndex += 1
                # reset kill index
                allKillIndex = 0
                hero.say("I have killed guardian number " + guardianKillIndex + "!")
    if not nearest:
        pass
    if closestItemDistance < closestEnemyDistance:
        if nearest:
            if nearest.type == "shaman":
                hero.attack(nearest)
            if nearest.type != "shaman":
                hero.move(closestItem.pos)
        if not nearest:
            hero.move(closestItem.pos)

    ##Move after killing a guardian##
    if guardianKillIndex == 1 and hero.pos.y < 90:
        hero.move({"x": 11, "y": 96})
    if guardianKillIndex == 2 and hero.pos.x < 100:
        hero.move({"x": 112, "y": 122})
    while guardianKillIndex == 3:
        hero.move({"x": 117, "y": 80})
        final = hero.findNearestEnemy()
        while final and hero.pos.x > 115:
            hero.attack(final)
        
        
    '''
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        if enemy.health < 0:
            enemyIndex += 1
            # hero.say(enemyIndex)
    '''
    '''
    items = hero.findItems()
    while itemIndex < len(items):
        item = items[itemIndex]
        if item.type == "coin":
            hero.moveXY(item.pos.x, item.pos.y)
        itemIndex += 1
    '''

    '''
    if itemIndex == len(items):
        hero.move({"x": 11, "y": 96})
    '''
    '''
    if totalKillIndex == 15:
        hero.move({"x": 104, "y": 126})
    if totalKillIndex == 17:
        hero.move({"x": 91, "y": 94})
        '''
    
        
        
WOULD THIS HELP FOR THE TREASURE LEVEL??

def collectUntil(enoughGold):
    # While hero.gold is less than enoughGold:
    while hero.gold < enoughGold:
        # Find a coin and take it: 
        coin = hero.findNearestItem()
        hero.move(coin.pos)
    pass



# Calculate the secret number and get into the Treasury.
# Those two guys know keys for the password.
friends = hero.findFriends()
number1 = friends[0].secretNumber
number2 = friends[1].secretNumber
# Just to be sure that the first number is greater.
if number2 > number1:
    swap = number1
    number1 = number2
    number2 = swap

# It's simple but slow function to find gcd.
def bruteforceGCD (a, b):
    hero.say("The naive algorithm.")
    cycles = 0
    # We enumerate all possible divisors.
    counter = b
    while True:
        cycles += 1
        if cycles > 100:
            hero.say("Calculating is hard. I'm tired.")
            break
        # If both number have "counter" divisor.
        if a % counter == 0 and b % counter == 0:
            break
        counter -= 1
    hero.say("I used " + cycles + " cycles")
    return counter

# It's smart way to find gcd.
def euclidianGCD (a, b):
    cycles = 0
    while b:
        cycles += 1
        swap = b
        b = a % b
        a = swap
    hero.say("I used " + cycles + " cycles")
    return a

# Maybe you need to use another function?
secretNumber = bruteforceGCD(number1, number2) # ∆
hero.moveXY(48, 34)
hero.say(secretNumber)
# The treasury is open (I hope so)! Go there!
hero.moveXY(68, 34)





            hero.move({"x": hero.pos.x + 1, "y": hero.pos.y})

            hero.move({"x": hero.pos.x - 1, "y": hero.pos.y})

            hero.move({"x": hero.pos.x, "y": hero.pos.y + 1})
            
            hero.move({"x": hero.pos.x, "y": hero.pos.y - 1})
