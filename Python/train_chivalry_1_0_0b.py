#//******************************************************************\\
# Filename  : train_chivalry_1.0.0b.py
# Version   : 1.0.0 b
# Date      : Feb. 20rd 2023
#
# What does it do?
# ----------------
# Grows the skill Chivalry to its cap (max. 115) using:
#
#   - Consecrate Weapon [30-40]
#   - Divine Fury       [40-55]
#   - Enemy Of One      [55-69]
#   - Lich Holy Light   [69-88]
#   - Noble Sacrifice   [88-115 (or cap)]
#
# If your skill cap is lower than 115, the script will stop then!
#
# What do I need?
# ---------------
# - A Chivalry spell book with the spells casted (see above)
# - Chivalry 101 from NPC in Luna (skill min. 30.0)
# - Some Tithes(LRC 100 gear kit is recommended)
# - Something else to do!
#
# How does it work?
# -----------------
# The script will cast the spell needed to grow your skill
# depending on the level of your skill. You can stop the training
# at anytime and restart it later. It will continue where you are
# at. The script will stop when your skill cap is reached, up to
# a maximum of 115.0.
#
# Then what?
# ----------
# Put the spell book in your backpack, tithe some golds (or gear
# up with a LRC 100 armor) and launch the script.
#
# Fail Safes
# ----------
# Some fail safes are activated on this script:
#   - Pauses on world saving
#   - Stops when the book is not found
#   - Stops when the spell is not in the book
#
# WARNING : THE SCRIPT WILL NOT STOP IF YOU MISS TITHES.
# At this time, the library does not provide the information to
# prevent it.
#
# DISCLAIMER
# ----------
# You are responsible for whatever is happening when using this 
# script.
#
# Keep in mind this script is beta, so in testing phase. It can bug.
# Thank you for reporting bug, if you do not mind!
#
# https://github.com/MalkScripts/RazorEnhanced
#
#**********************************************************************
# Version 1.0.0b
# --------------
# Date      : Feb. 20th 2023
#
# Casts: Consecrate Weapon  (30-40)     Holy Light       (69-88)
#        Divine Fury        (40-55)     Noble Sacrifice  (88-115)
#        Enemy Of One       (55-69)     
#        
#
# - Regenerate mana when under the required amount
# - Casting stops at the skill cap or at 115, depending which one
#   is reached first.
#
#\\******************************************************************//


cw = OneSpell("consecrate weapon",  40,     10,     10)
df = OneSpell("divine fury",        55,     10,     10)
eo = OneSpell("enemy of one",       69,     10,     20)
hl = OneSpell("holy light",         88,     10,     20)
ns = OneSpell("noble sacrifice",    115,    30,     20)




import sys

book            = [0x2252, 0x0000] # ID, color
chivalryBook    = None
mandatoryBreak  = 150
trainingCap     = 115
skillname       = "chivalry"
tmrRegen        = "timerRegenMana"
tmrRegenPost    = "timerRegenManaPost"

# Colors
err     = 33    # Red
reg     = 77    # Dark Turquoise
warn    = [
    44,         # Orange
    55          # Yellow
]

cooldown = [
    150,    # [0] Mandatory processing
    4000,   # [1] After each cast
    750,    # [2] countdown (msg displays has 150ms delay)
    11000,  # [3] Meditation cooldown
    5000,   # [4] Mana regeneration (message posting)
]


class OneSpell:
    def __init__(self, name, level, price, mana):
        self.name   = name
        self.level  = level
        self.price  = price
        self.mana   = mana
  
        
#*******************************************************
#*** countdown() ***************************************
#*******************************************************
#
# Display countdown.
#
# Receives  : nothing
# Returns   : nothing
#*******************************************************
def countdown():
    headMsg(warn[1],"3..")
    pause(cooldown[2])
    headMsg(warn[0],"..2..")
    pause(cooldown[2])
    headMsg(err,"..1..")
    pause(cooldown[2])
    headMsg(err,"GO")
    pause(cooldown[0])

    
#*******************************************************
#*** checkForBook() ************************************
#*******************************************************
#
# Validates a Chivalry spell book is in the backpack
# of the player. The spell book has to be in the 
# backpack, not a bag or another container.
#
# Receives  : nothing
# Returns   : nothing
#*******************************************************
def checkForBook():
    # Book has to be in the backpack or in the hand
    # of the player to cast.
    chivalryBook = Items.FindAllByID(book[0], book[1], Player.Backpack.Serial, 0)
    pause(cooldown[0])
    if not chivalryBook:
        # Maybe it is already in hand..
        chivalryBook = Player.GetItemOnLayer('RightHand')
        pause(cooldown[0])
        if chivalryBook:
            # The book has to be in the hand
            if not chivalryBook.ItemID == book[0] and not chivalryBook.Hue == book[1]:
                headMsg(err, "CHIVALRY BOOK NOT FOUND!")
                crash()
        else:
            headMsg(err, "CHIVALRY BOOK NOT FOUND!")
            crash()
            
    pause(cooldown[0])


#*******************************************************
#*** checkForWorldSaving() *****************************
#*******************************************************
#
# Checks for a world saving anf pausing the script
# during that time
#
# Receives  : nothing
# Returns   : nothing
#*******************************************************
def checkForWorldSaving():
    if Journal.SearchByType("will save in 10", 'System'):
        Journal.Clear()
        pause(cooldown[0])
        headMsg(warn[0], "The world will save in 10 seconds..")
        pause(cooldown[0])
        headMsg(warn[1], "Pausing script..")
        while not Journal.SearchByType("World save complete.", 'System'):
            pause(cooldown[0])

        # To be sure we got the message only once
        Journal.Clear()
        pause(cooldown[2])
        
        # Script restarts automatically after world saving.
        headMsg(warn[0], "SCRIPT RESTARTING IN")
        countdown()
        
    # Mandatory processing cooldown    
    pause(cooldown[0])

    
#*******************************************************
#*** crash() *******************************************
#*******************************************************
#
# Ends the script. Used to shorten the code. 
#
# Receives  : nothing
# Returns   : nothing
#*******************************************************
def crash():
    headMsg(reg, "Script halted by function")
    sys.exit()

    
#*******************************************************
#*** failSafe() ****************************************
#*******************************************************
#
# Check for world saving and book is still available.
#
# Receives  : nothing
# Returns   : nothing
#*******************************************************
def failSafe():
    checkForWorldSaving()
    checkForBook()
    if Player
    
#*******************************************************
#*** headMsg(color, msg) *******************************
#*******************************************************
#
# Posts a message over the head of the player.
#
# Receives  : int, str: color, message to post.
# Returns   : nothing
#*******************************************************
def headMsg(color, msg):
    Player.HeadMessage(color, msg)
    pause(cooldown[0])

    
#*******************************************************
#*** pause(tTime) **************************************
#*******************************************************
#
# Pauses the script for the amount of time received.
# Written to shorten possible modifications to the 
# code.
#
# Receives  : int, amount of time for the pause (in ms)
# Returns   : nothing
#*******************************************************
def pause(tTime):
    Misc.Pause(tTime)

    
#*******************************************************
#*** main() ********************************************
#*******************************************************

headMsg(reg, "Initializing script...")
checkForBook()
headMsg(reg, "Chivalry Spell Book Found!")
headMsg(reg, "Initializing spells..")

#*******************************************************
#*********************** SPELLS ************************
#*******************************************************
#                    name,         level   price   mana
#*******************************************************
cw = OneSpell("consecrate weapon",  40,     10,     10)
df = OneSpell("divine fury",        55,     10,     10)
eo = OneSpell("enemy of one",       69,     10,     20)
hl = OneSpell("holy light",         88,     10,     20)
ns = OneSpell("noble sacrifice",    115,    30,     20)

headMsg(reg, "..done!")
headMsg(reg, "Ready to go in")
countdown()

# will do until skill cap is reached (115 maximum)
while Player.GetRealSkillValue(skillname) < trainingCap:
    if Player.GetRealSkillValue(skillname) >= Player.GetSkillCap(skillname):
        #Skill cap of the player is lower than 115
        break
        
    Journal.Clear()
    failSafe()
    
    skillLvl = Player.GetRealSkillValue(skillname)

    if skillLvl < 30:
        headMsg(err, "Gain skill by visiting NPC in Luna")
        crash()
    elif skillLvl < cw.level:
        toCast = cw
    elif skillLvl < df.level:
        toCast = df
    elif skillLvl < eo.level:
        toCast = eo
    elif skillLvl < hl.level:
        toCast = hl
    elif skillLvl < trainingCap:
        toCast = ns
    
    Spells.CastChivalry(toCast.name)
    pause(cooldown[0])
   
    # Has the book, but the spell?
    if Journal.SearchByType("You do not have that spell", 'System'):
        Journal.Clear()
        headMsg(err, "SPELL OR BOOK MISSING!")
        crash()
        
    pause(cooldown[1])
    
    # A minimum of mana is required to cast the spell
    if Player.Mana < toCast.mana:
        if not Timer.Check(tmrRegen):
            Player.UseSkill('meditation')
            Timer.Create(tmrRegen, cooldown[3])
            
        pause(cooldown[0])
        while Player.Mana < Player.ManaMax:
            if not Timer.Check(tmrRegenPost):
                Timer.Create(tmrRegenPost, cooldown[4])
                headMsg(warn[1], "Renegerating mana..")
                
            pause(cooldown[0])

            if Journal.SearchByType("You stop meditating", 'System'):
                if not Timer.Check(tmrRegen):
                    Player.UseSkill('meditation')
                    pause(cooldown[0])
                    Timer.Create(tmrRegen, cooldown[3])
                    Journal.Clear()

            pause(cooldown[0])

    # Mandatory processing cooldown
    pause(cooldown[0])

headMsg(reg, "TRAINING IS OVER!")
