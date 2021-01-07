import random
import time


#Opening Intro and Info Scenes#

def title():
    print ('''                       .__ .__   .__                           .__           _______________   ________  ____ 
______   __ __   ____  |__||  |  |__|  ______  _____     ______|__|  _____   \_____  \\   _  \  \_____  \/_   |
\____ \ |  |  \ / ___\ |  ||  |  |  | /  ___/ /     \   /  ___/|  | /     \   /  ____// /_\  \  /  ____/ |   |
|  |_> >|  |  // /_/  >|  ||  |__|  | \___ \ |  Y Y  \  \___ \ |  ||  Y Y  \ /       \\  \_/   \/       \ |   |
|   __/ |____/ \___  / |__||____/|__|/____  >|__|_|  / /____  >|__||__|_|  / \_______ \\_____  /\_______ \|___|
|__|          /_____/                     \/       \/       \/           \/          \/      \/         \/     ''')

def greetingScreen():
    print ('Welcome to Pugilism Simulator 2021! Are you ready?')
    response = input ()
    if response == ('y') or ('yes') or ('Y') or ('Yeah') or ('yeah'):
        time.sleep(1)
        print ('''Hurray, let's go!''')
        time.sleep(1)
    else:
        print ()
        print ('''Who cares what you want!? Let's go!''')


    
def instructionOption():
    print ()
    print ('''Before we begin, Would you like some help?''')
    response = input()
    if response == ('y' or 'yes' or 'Y' or 'Yeah' or 'yeah'):
        time.sleep(1)
        print ('''The aim of the game is to knock your opponent out without being knocked out yourself.
If a player's health hits 0 they are KO'd. Stamina is spent everytime you attack and
gained every time you defend. The lower your stamina gets the more damage your opponent does
and if a player's stamina gets too low their own punching power is drastically reduced.''')
        print()
        time.sleep(1)
        

        print ('''Keep your stamina high to replenish your health quickly, and if your health is high you will
automatically recover a little trickle of stamina every turn.''')
        print()
        time.sleep(1)

        print ('''Lights Jabs are weak punches that have a high chance of landing.
Heavy Swings do lots of damage but are stamina intensive and prone to missing.
Blocking helps you soak up damage while you spend a turn recovering stamina but can be overcome with heavy swings.
Dodging gives you a chance to completely avoid an opponents blows while recovering stamina.

Use dodge and block to recover stamina, light jabs to do damage and heavy swings to smash opponents with big hits!''')
        time.sleep (2)
        print ('''The time for talk is over... press any key to get it started!''')
        input()
    else:
        print ()
        time.sleep (1)
        print ('''Ok, let's get started!''')

def describeScene():
    print ()
    time.sleep(1)
    print ('You step into the ring. You and your opponent touch gloves. The bell rings...')



def makeChoice():
    time.sleep(1)
    print ()
    print('Make your move!')
    print('{1] Light Jab')
    print('[2] Heavy Swing')
    print('[3] Block')
    print('[4] Dodge')
    response = input ()
    print()
    return response


# AI Code Goes Here.

def oppChoice():

# All things going well the AI will attack.
    if oppHealth > 8 and oppStamina >= 8:
        basicAI = random.randint (1, 2)

#If tired but relatively unharmed, the AI will alternate between blocks and jabs to maintain its stamina.
    elif oppHealth > 7 and oppStamina > 4 and oppStamina <8:
        pick = random.randint (1, 2)
        if pick == 1:
            basicAI = 1
        if pick == 2:
            basicAI = 3

#If seriously hurt and tired, AI will play defensively.
    elif oppHealth <= 4 and oppHealth > 2 and oppStamina < 5:
        basicAI = random.randint (3, 4)

    elif oppHealth < 3 and oppStamina < 5:
        basicAI = 4

#If hurt but not tired, AI will go for a desperate heavy swing, or dodge to recover health
    elif oppHealth <= 5 and oppHealth > 2 and oppStamina > 6:
        pick = random.randint (1, 5)
        if pick >= 3:
            basicAI = 2
        if pick < 3:
            basicAI = 4
        

#AI will select a move at random if uncertain.
    else:
        basicAI = random.randint (1, 4)

        
    return basicAI

#Opponent Moves, calculates damage done to player while they were attacking with Jab or Heavy Swing

def oppJabDamage(oppStamina):
    global playerHealth, playerStamina
    hitSuccess = random.randint (0, 9)
    damageCalc = random.randint (2, 3)
    if hitSuccess >= 3 and oppStamina > 2:
        playerHealth -= staminaDamageModifier (playerStamina, damageCalc)
        print ('Your opponent hits you with a jab')
    elif hitSuccess >= 3 and oppStamina < 3:
        playerHealth -= (staminaDamageModifier (playerStamina, damageCalc))/2
        print ('Your opponent is tired and hits you with a weak jab.')
        
    if hitSuccess < 3:
        print ('Your opponent tries to jab, but they miss')
        


def oppHeavySwingDamage(oppStamina):
    global playerHealth
    hitSuccess = random.randint (0, 9)
    damageCalc = random.randint (4, 5)
    if hitSuccess >= 6:
        playerHealth -= staminaDamageModifier (playerStamina, damageCalc)
        print ('Your opponent clobbers you with a heavy swing')
    elif hitSuccess >= 6 and oppStamina < 3:
        playerHealth -= (staminaDamageModifier (playerStamina, damageCalc) - 2)/2
        print ('Your opponent is tired and hits you with a weakened heavy swing')
    if hitSuccess < 6:
        print ('Your opponent makes a heavy swing but they miss')


#Code for Player Actions, returns damage done to opponent
def Jab(oppChoice, playerStamina):
    global oppHealth
    hitSuccess = random.randint (0, 9)
    damageCalc = random.randint (2, 3)
    if oppChoice == 1 and hitSuccess >= 3 and playerStamina > 2:
        print ('You catch him with a jab')
        oppHealth = oppHealth - staminaDamageModifier (oppStamina, damageCalc)
    elif oppChoice == 1 and hitSuccess >= 3 and playerStamina < 3:
        print ('You catch him with an exhausted and weak jab')
        oppHealth = (oppHealth - staminaDamageModifier (oppStamina, damageCalc))/2
    
    if oppChoice == 1 and hitSuccess < 3:
        print ('Your jab goes wide')
        
        
    if oppChoice == 2 and hitSuccess < 3:
        print ('The jab misses, hard')
        
        
    if oppChoice == 2 and hitSuccess >= 3 and playerStamina > 2:
        print ('Your Jab finds a home')
        oppHealth = oppHealth - staminaDamageModifier (oppStamina, damageCalc)
    elif oppChoice == 2 and hitSuccess >= 3 and playerStamina < 3:
        print ('You catch him with an exhausted and weak jab')
        oppHealth = (oppHealth - staminaDamageModifier (oppStamina, damageCalc))/2
    
    if oppChoice == 3 and playerStamina > 2:
        print ('Your jab hits him while he covers up')
        oppHealth -= staminaDamageModifier (oppStamina, damageCalc) - 1

    elif oppChoice == 3 and playerStamina < 3:
        print ('You catch him covering up with an exhausted and weak jab')
        oppHealth = (oppHealth - staminaDamageModifier (oppStamina, damageCalc) - 1)/2

        
    if oppChoice == 4 and hitSuccess >= 7 and playerStamina > 2:
        print ('He tries to dodge, but you catch him with your jab')
        oppHealth -= staminaDamageModifier (oppStamina, damageCalc)
    elif oppChoice == 4 and hitSuccess >= 7 and playerStamina < 3:
        print ('He tries to dodge, but you catch him with an exhausted and weak jab')
        
    if oppChoice == 4 and hitSuccess < 7:
        print ('he dodges your jab')
    if oppChoice == 1:
        oppJabDamage(oppStamina)
    if oppChoice == 2:
        oppHeavySwingDamage(oppStamina)
        
            
def heavySwing(oppChoice, playerStamina):
    global oppHealth
    hitSuccess = random.randint (0, 9)
    damageCalc = random.randint (4, 5)
    if oppChoice == 1 and hitSuccess >= 5 and playerStamina > 2:
        print ('You smash your opponent with a heavy swing')
        oppHealth = oppHealth - staminaDamageModifier (oppStamina, damageCalc)
    elif oppChoice == 1 and hitSuccess >= 5 and playerStamina < 3:
        oppHealth -= (staminaDamageModifier(oppStamina, damageCalc)-2)/2
        print ('You smash your opponent with an exhuasted and weakened heavy swing')
    
    if oppChoice == 1 and hitSuccess < 5:
        print ('Your heavy swing goes wide')
        
    
    if oppChoice == 2 and hitSuccess >= 4 and playerStamina > 2:
        print ('You smash your opponent with a heavy swing')
        oppHealth -= staminaDamageModifier (oppStamina, damageCalc)
    elif oppChoice == 2 and hitSuccess >= 4 and playerStamina < 3:
        oppHealth -= (staminaDamageModifier(oppStamina, damageCalc)-2)/2
        print ('You smash your opponent with an exhuasted and weakened heavy swing')
    
    if oppChoice == 2 and hitSuccess < 4:
        print ('Your heavy swing goes wide')
        

    if oppChoice == 3 and playerStamina > 2:
        print ('You hammer your opponents block')
        oppHealth -= (staminaDamageModifier (oppStamina, damageCalc) - 1)

    elif oppChoice == 3 and playerStamina < 3:
        oppHealth -= (staminaDamageModifier(oppStamina, damageCalc) - 3)/2
        print ('You smash your opponent with an exhuasted and weakened heavy swing')

    if oppChoice == 4 and hitSuccess >= 7 and playerStamina > 2:
        print ('Your opponent tries to dodge and fails. You clobber them.')
    elif oppChoice == 4 and hitSuccess >= 7 and playerStamina < 3:
        oppHealth -= (staminaDamageModifier(oppStamina, damageCalc))/2
        print ('Your opponent tries to dodge but you catch them with an exhuasted and weakened heavy swing')
        oppHealth -= (staminaDamageModifier (oppStamina, damageCalc)- 2)/2
        
    if oppChoice == 4 and hitSuccess <7:
        print ('Your opponent easily dodges your heavy swing')
    if oppChoice == 1:
        oppJabDamage(oppStamina)
    if oppChoice == 2:
        oppHeavySwingDamage(oppStamina)
        

    

#Code for defensive player actions. Returns damage done to player this turn

def block(oppChoice, oppStamina):
    global playerHealth
    
    if oppChoice == 1 and oppStamina > 2:
        damageCalc = random.randint (2, 3)
        print ('You block and limit the damage of your opponents jab')
        playerHealth -= staminaDamageModifier (playerStamina, damageCalc) - 1
    elif oppChoice == 1 and oppStamina < 3:
        damageCalc = random.randint (1, 2)
        playerHealth -= (staminaDamageModifier (playerStamina, damageCalc) - 1)/2
        print ('You block and your opponent hits you with a weakened jab')

    if oppChoice == 2 and oppStamina > 2:
        damageCalc = random.randint (4, 5)
        print ('You block and he smashes you with a heavy swing')
        playerHealth -= staminaDamageModifier (playerStamina, damageCalc) - 2
    elif oppChoice == 2 and oppStamina < 3:
        damageCalc = random.randint (3, 4)
        playerHealth -= (staminaDamageModifier (playerStamina, damageCalc) - 2)/2
        print ('You block and your opponent hits you with a weakened heavy swing')

    if oppChoice == 3:
        print ('You both block this turn and neither of you attack')
        
        
    if oppChoice == 4:
        print ('You block and he dodges, neither of you attack')
        
    

def dodge(oppChoice, oppStamina):
    hitSuccess = random.randint (0, 9)
    global playerHealth
    if oppChoice == 1 and hitSuccess >= 4:
        damageCalc = random.randint (1, 2)
        print ('You dodge your opponents incoming jab')
        
        
    if oppChoice == 1 and hitSuccess < 4 and oppStamina > 2:
        damageCalc = random.randint (2, 3)
        print ('You try to dodge but your opponent catches you with a jab')
        playerHealth -= staminaDamageModifier (playerStamina, damageCalc)
    elif oppChoice == 1 and hitSuccess < 4 and oppStamina < 3:
        damageCalc = random.randint (2, 3)
        playerHealth -= (staminaDamageModifier (playerStamina, damageCalc))/2
        print ('You try to dodge but your opponent catches you with a tired jab.')
        
    if oppChoice == 2 and hitSuccess < 2 and oppStamina > 2:
        damageCalc = random.randint (4, 5)
        print ('You try to dodge but they smash you with a heavy swing')
        playerHealth -= staminaDamageModifier (playerStamina, damageCalc)

    elif oppChoice == 2 and hitSuccess < 2 and oppStamina < 3:
        damageCalc = random.randint (4, 5)
        print ('You try to dodge but they smash you with a weakened heavy swing')
        playerHealth -= (staminaDamageModifier (playerStamina, damageCalc) - 2)
        
    if oppChoice == 2 and hitSuccess >= 2:
        damageCalc = random.randint (3, 4)
        print ('You dodge their heavy swing')
        
        
    if oppChoice == 3:
        print ('Your opponent blocks while you dodge, no one attacks')
        

    if oppChoice == 4:
        print ('You both try to dodge, no one attacks')
        



#Code for Checking and Altering Health and Stamina

def staminaFloor():
    global oppStamina, playerStamina
    if oppStamina < 0:
        oppStamina = 0
    if playerStamina <0:
        playerStamina = 0

def oppStaminaLoss(oppAction):
    global oppStamina
    if oppAction == 1:
        oppStamina -= 3
    if oppAction == 2:
        oppStamina -= random.randint(3,4)
    if oppAction == 3:
        oppStamina += random.randint (2, 3)
    if oppAction == 4:
        oppStamina += 2
    if oppStamina < 0:
        oppStamina = 0
    
        

def displayStatus(playerHealth, playerStamina):
    ()
    print ('''Stamina: ''' + str(playerStamina))
    print ('''Health: ''' + str(playerHealth))

def oppStatus (oppStamina, oppHealth):
    if oppStamina > 5 and oppStamina <= 7:
        print ('Your opponent looks slightly tired')
    if oppStamina <=5 and oppHealth > 5:
        print ('Your opponent looks very tired')
    if oppStamina > 5 and oppHealth >= 5 and oppHealth < 8:
        print ('Your opponent has a small cut')
    if oppStamina > 5 and oppHealth < 5:
        print ('Your opponent looks beaten up')
    if oppStamina <= 5 and oppHealth <= 5:
        print ('Your opponent looks very tired and beaten up')
    if oppStamina > 7 and oppHealth > 7:
        print ('Your opponent looks healthy')

def staminaDamageModifier(target_stamina, damage):
    
    if target_stamina < 5:
        result = damage * 2
        
    if target_stamina > 4 and target_stamina <= 7:
        result = damage + 1
        
    if target_stamina > 7:
        result = damage
    return result
    


def healthRecovery (current_health, stamina):
    global playerHealth
        
    if current_health < 7 and current_health > 5 and stamina > 5:
        playerHealth += 1
        print ('You manage to recover some health.')

    if current_health < 7 and current_health > 5 and stamina <= 5:
        print ('You are too out of breath right now to recover any health..')
        
        
    if current_health <= 5 and current_health > 0 and stamina > 5:
        print ('The room stops spinning and you recover some health.')
        playerHealth += random.randint (2, 3)

    if current_health < 5 and current_health > 0 and stamina <= 5:
        print ('You are too exhausted to recover health right now')

def oppHealthRecovery (Health, Stamina):
    global oppHealth
    if Health < 7 and Health > 5 and Stamina > 5:
        oppHealth += 1
    if Health <= 5 and Health > 0 and Stamina > 5:
        oppHealth += random.randint (1, 2)
    
        
        

def staminaEffect (makeChoice):
    global playerStamina
    if makeChoice == '1':
        playerStamina -= 3
    if makeChoice == '2':
        playerStamina -= random.randint (3,4)
    if makeChoice == '3':
        playerStamina += random.randint (2,3)
    if makeChoice == '4':
        playerStamina += 2
    if playerStamina > 10:
        playerStamina = 10
    

def staminaRecovery (health, stamina):
    global playerHealth, playerStamina
    if health > 8 and stamina < 7:
        print ('You easily recover your breath')
        playerStamina = stamina + 2
    if health <= 8 and health > 5 and stamina < 7:
        playerStamina += 1
        print ('Gasping, you recover some stamina')
    if health <= 5:
        print ('You are too beaten up to catch your breath properly')
        
        


def victoryChecker():
    if oppHealth < 1 and playerHealth < 1:
        print ('You both knock eachother unconscious. It is a kind of victory... ...sort of.')
    elif oppHealth < 1:
        print ('Your opponent falls to the floor defeated, you raise your gloves in victory')
        V = 2
    elif playerHealth < 1:
        print ('You black out. Today was not your day.')
        V = 1
    else:
        V = 0
    return V

def oppStaminaRecover(Health, Stamina):
    global oppStamina
    if Health > 8 and Stamina < 7:
        oppStamina += 2
    if Health >= 8 and Health > 5 and Stamina < 7:
        oppStamina += 1


#Bigger Programs / Bigger Problems

def start():
    greetingScreen()
    instructionOption()
    describeScene()

def round():
    playerAction = makeChoice()
    oppAction = oppChoice()
    if playerAction == '1':
        Jab(oppAction, playerStamina)
    if playerAction == '2':
        heavySwing(oppAction, playerStamina)
    if playerAction == '3':
        block(oppAction, oppStamina)
    if playerAction == '4':
        dodge(oppAction, oppStamina)
    staminaEffect(playerAction)
    oppStaminaLoss(oppAction)
    staminaFloor()


def endRound():
    if victoryChecker() == 0:
        time.sleep(1)
        healthRecovery (playerHealth, playerStamina)
        staminaRecovery (playerHealth, playerStamina)
        displayStatus (playerHealth, playerStamina)
        oppHealthRecovery (oppHealth, oppStamina)
        oppStaminaRecover (oppHealth, oppStamina)
        oppStatus(oppStamina, oppHealth)
    else:
        print ('Game over!')
        time.sleep(1)
        print ('Would you like to play again?')
        response = input()
        if response in ['yes', 'y', 'Yes', 'Yup', 'Y', 'Yeah', 'yeah']:
            main()
         
    


playerHealth = 10
playerStamina = 10
oppHealth = 10
oppStamina = 10
game_over = 0

def fighting():
    round()
    endRound()
    if oppHealth > 0 and playerHealth > 0:
        fighting()
def main():
    greetingScreen()
    instructionOption()
    describeScene()
    fighting()
title()
time.sleep(2)
main()

    
       
