

###For Moving!!##
def move():
    ##Determining hero.Quadrant
    QuadA = False
    if hx >=  42 and hy > 95:
        QuadA = True
        
    QuadB = False
    if hx <  42 and hy >=  40:
        QuadB = True
    
    QuadC = False
    if hx <= 110 and hy <  40:
        QuadC = True
        
    QuadD = False
    if hx > 110 and hy <= 95:
        QuadD = True
        
    #A quadrant:#
    if QuadA:
        if closestLDist <= 7:
            if closestL.pos.y < hero.pos.y:
                ymove =  7
                xmove = -3
            if closestL.pos.y > hero.pos.y:
                ymove = -7
                xmove = -3
            hero.move({"x": hero.pos.x + xmove, "y": hero.pos.y + ymove})
        else:
            hero.move({"x":  40, "y": 115})
        
    #B quadrant:#
    if QuadB:
        if closestLDist <= 7:
            if closestL.pos.x < hero.pos.x:
                xmove =  7
                ymove = -3
            if closestL.pos.x > hero.pos.x:
                xmove = -7
                ymove = -3
            hero.move({"x": hero.pos.x + xmove, "y": hero.pos.y + ymove})
        else:
            hero.move({"x":  20, "y":  38})
        
    #C quadrant:#
    if QuadC:
        if closestLDist <= 7:
            if closestL.pos.y < hero.pos.y:
                ymove =  7
                xmove =  3
            if closestL.pos.y > hero.pos.y:
                ymove = -7
                xmove =  3
            hero.move({"x": hero.pos.x + xmove, "y": hero.pos.y + ymove})
        else:
            hero.move({"x": 112, "y":  25})
        
    #D quadrant:#
    if QuadD:
        if closestLDist <= 7:
            if closestL.pos.x < hero.pos.x:
                xmove =  7
                ymove =  3
            if closestL.pos.x > hero.pos.x:
                xmove = -7
                ymove =  3
            hero.move({"x": hero.pos.x + xmove, "y": hero.pos.y + ymove})
        else:
            hero.move({"x": 130, "y": 97})

while True:
    hx =            hero.pos.x
    hy =            hero.pos.y
    xmove =         0
    ymove =         0
    
    ##Closest attackable enemy (i.e. NOT Brawler, NOT yak)##
    closestEDist =  99
    closestE =      None
    enemyIndex =    0
    
    ##Stupid Brawlers shit##
    closestBDist =  99
    closestB =      None
    brawlerIndex =  0
    
    ##Yak shit##
    closestYDist =  99
    closestY =      None
    yakIndex =      0
    
    ##Yak and B together##
    closestLDist =  99
    closestL =  None
    largeIndex =      0
    
    ##All units discovery##
    yaks =          hero.findByType("sand-yak")
    brawlers =      hero.findByType("brawler")
    #               range is  5
    throwers =      hero.findByType("thrower")
    ##              range is 25
    fangriders =    hero.findByType("fangrider")
    ##              range is 20
    shamans =       hero.findByType("shaman")
    ##              range is 30
    ogres =         hero.findByType("ogre")
    ##              range is  3
    scouts =        hero.findByType("scout")
    ##              range is  3
    longdist =      throwers + fangriders + shamans
    melee =         ogres + scouts
    nonBrawlers =   throwers + fangriders + shamans + ogres + scouts
    scary =         brawlers
    large =         brawlers + yaks
    bashready = hero.isReady("bash")
    
    #General enemy counting and nearest#
    while enemyIndex < len(nonBrawlers):
        enemy = nonBrawlers[enemyIndex]
        de = hero.distanceTo(enemy)
        if de < closestEDist:
            closestEDist = de
            closestE = enemy
        enemyIndex += 1

    #Brawler counting and nearest#
    while brawlerIndex < len(scary):
        enemy = scary[brawlerIndex]
        de = hero.distanceTo(enemy)
        if de < closestBDist:
            closestBDist = de
            closestB = enemy
        brawlerIndex += 1

    #Yaks counting and nearest#
    while yakIndex < len(yaks):
        enemy = yaks[yakIndex]
        de = hero.distanceTo(enemy)
        if de < closestYDist:
            closestYDist = de
            closestY = enemy
        yakIndex += 1
        
    #Yaks and Brawlers counting and nearest#
    while largeIndex < len(large):
        enemy = large[largeIndex]
        de = hero.distanceTo(enemy)
        if de < closestLDist:
            closestLDist = de
            closestL = enemy
        largeIndex += 1
        
    ##If the closest enemy is close enough, kill it##
    if closestEDist < 31:
        if closestBDist >= closestEDist + 15:
            hero.attack(closestE)
        if closestBDist < closestEDist + 15:
            move()
    elif closestBDist < 31:
        move()
        
        
        '''        
        if sayIndex == 1:
            hero.say(closestEDist)
            sayIndex += 1
        '''
        
        
        #else:
        #    move()
    ##Commenting this out for a test:##
    #else:
    #    move()
    '''
    ##If a Brawler is within 30, just keep moving##
    if closestB:
        while closestBDist < 30:
            move()
    '''
        
    
    
    ## Putting the brawlers run stuff away for now##
    '''
    melee = ogres + scouts + brawlers
    longdist = throwers + fangriders + shamans
    '''


    '''
    def run(e):
        # hero.say("I'm running!")
        #de = hero.distanceTo(e)
        #if de < 15:
        hero.move({"x": hx + (hx - e.pos.x), "y": hy + (hy - e.pos.y)})
        
    if e.pos.x <=40 and e.pos.y <= 120:
        hero.move({"x": 120, "y": 25})
    if e.pos.x >=113 and e.pos.y <= 120:
        hero.move({"x": 25, "y": 105})
    if 113 > e.pos.x > 40 and e.pos.y > 100:
        hero.move({"x": 25, "y": 25})
    if 113 > e.pos.x > 40 and e.pos.y < 45:
        hero.move({"x": 120, "y": 105})
    '''
    
    # First check for those big brawlers:
    '''
    if brawlers[0]:    
        for x in brawlers:
            db = hero.distanceTo(x)
            while db < 17:
                run(x)
                continue
        # Then check for long distance fighters:

    for x in longdist:
#        if db < 17:
#           run(brawlers[0])
        dt = hero.distanceTo(x)
        if dt <= 27:
            hero.attack(x)
    # Finally check for melee fighters:
    for x in melee:
#        if db < 17:
#           run(brawlers[0])
        dm = hero.distanceTo(x)
        if dm < 10:
            if x.health > 0:
                hero.attack(x)

    if db and 6 < db < 17:
        # hero.say("Help!")
        run(brawlers[0])
    if db and db <= 6:
        hero.move({"x":  115, "y": 69})
    if db and db > 17:
        mov()
'''
    
    
    '''
    closestAnyDist =99
    closestAny =    None
    if closestBDist < closestEDist:
        closestAnyDist = closestBDist 
        closestAny = closestB
    if closestEDist <= closestBDist:
        closestAnyDist = closestEDist
        closestAny = closestE
    '''
        
'''
        if hero.isPathClear({"x": closestY.pos.x, "y": closestY.pos.y - 5}, hero.pos):
            hero.moveXY(closestY.pos.x, closestY.pos.y - 5)
        else:
            hero.moveXY(closestY.pos.x, closestY.pos.y + 5)
        if hero.isPathClear({"x": closestY.pos.x - 5, "y": closestY.pos.y}, hero.pos):
            hero.moveXY(closestY.pos.x - 5, closestY.pos.y)
        else:
            hero.moveXY(closestY.pos.x + 5, closestY.pos.y)


    ##Then move around##
    #A quadrant:#
    if hx >=  42 and hy > 95:
        hero.move({"x":  40, "y": 115})
    #B quadrant:#
    if hx <  42 and hy >=  40:
        hero.move({"x":  20, "y":  38})
    #C quadrant:#
    if hx <= 110 and hy <  40:
        hero.move({"x": 112, "y":  25})
    #D quadrant:#
    if hx > 110 and hy <= 95:
        hero.move({"x": 130, "y": 97})
'''

    
