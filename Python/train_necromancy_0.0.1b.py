#//******************************************************************\\
# Filename  : train_necromancy_0.0.1b.py
# Version   : 0.0.1 b
# Date      : Jan. 23rd 2023
#
# What does it do?
# ----------------
# Grows Necromancy to its cap using:
#
#   - Curse Weapon (20-30)
#   - Wraith Form (30-55)
#   - Horrific Beast (55-81)
#   - Lich Form (81-99.9)
#   - Vampiric Embrace (99.9-120)
#
# If your skill cap is lower than 120, the script will stop then!
#
# What do I need?
# ---------------
# - A Necromancy spell book with the spells casted (see above)
# - Necromancy 101 from NPC (skill min. 20.0)
# - A big bunch of reagents (LRC 100 gear kit is recommended)
# - Bandages (lich form drops your HP a bit)
# - The will to grow back up your karma
#
# How does it work?
# -----------------
# Gear up and run the script! DO NOT FORGET TO UNLOCK YOUR KARMA.
#
# Then what?
# ----------
# Get busy, wait until it is done then UNLOCK YOUR KARMA.
#
# Fail Safes
# ----------
# Some fail safes are activated on this script:
#   - Pause of 15 seconds for world saving
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
# Version 0.0.1b
# --------------
# Date      : Jan. 23rd 2023
#
# Casts: Curse Weapon   (20-30)     Lich Form        (81-99.9)
#        Wraith Form    (30-55)     Vampiric Embrace (99.9-120)
#        Horrific Beast (55-81)     
#        
#
# - Regenerate mana when under the required amount
# - Casting stops at the skill cap.
#
#\\******************************************************************//

#**********************************************************************
#**********************************************************************
#**********************************************************************
#**********************************************************************
#**********************************************************************
#**********************************************************************
#**********************************************************************
#**********************************************************************
import sys

Break           = 500
delayCasts      = 4500
delayManaRegen  = 5000
delayFailSafe   = 15000
skillLvl        = Player.GetRealSkillValue('necromancy')
timerManaRegen  = "tManaRegen"

# Colors
err     = 33
reg     = 77
warn    = 44

#// *** crash() *** \\
# Ends the script  
#
# Receives  : nothing
# Returns   : nothing
def crash():
    sys.exit()

#// *** failSafe() *** \\
# Temporary pause the script for 15 seconds when the world
# is about to save.
#
# Receives  : nothing
# Returns   : nothing
def failSafe():
    Journal.Clear()
    headMsg(warn, "The world will save in 10 seconds..")
    pause(Break)
    headMsg(reg, "Pausing script for 15 seconds..")
    pause(delayFailSafe)
    
#// *** headMsg(color, msg) *** \\
# Posts a message over the head of the player.
#
# Receives  : int, str: color, message to post.
# Returns   : nothing
def headMsg(color, msg):
    Player.HeadMessage(color, msg)
    pause(Break)

#// *** pause(tTime) *** \\
# Pauses the script for the amount of time received. Written
# to shorten the code.
#
# Receives  : int: amount of time for the pause (in ms)
# Returns   : nothing
def pause(tTime):
        Misc.Pause(tTime)

#// *** regenMana() *** \\
# Regenerate mana to maximum.
#
# Receives  : nothing
# Returns   : nothing
def regenMana():
    Player.UseSkill('meditation')
    while Player.Mana < Player.ManaMax:
        if not Timer.Check(timerManaRegen):
            headMsg(warn, "mana regeneration..")
            Timer.Create(timerManaRegen, delayManaRegen)
        pause(Break)

#// *** main() *** \\

#Avoiding all possible confusions
Journal.Clear()

#Validating if the player has a LRC 100 gear set
#(will only warn the user)
if Player.SumAttribute("Lower Reagent Cost") < 100:
    headMsg(warn, "YOU DO NOT HAVE A LRC 100 SET.")
    headMsg(reg, "You can ran out of reagents before the end of the training.")

#Script will not start if skill is lower than 20.0 points.
if skillLvl < 20:
    headMsg(err, "Skill is too low! Visit NPC in Umbra for starter.")
    crash()


#//*************************************************** \\
#  *** Once there, player has everything required *** 
#\\*************************************************** //

#Regenerating mana before beginning
if Player.Mana < Player.ManaMax:
    headMsg(warn, "Full mana before beginning")
    regenMana()

    
headMsg(reg, "Training begins..")
    
while skillLvl < Player.GetSkillCap('necromancy'):

    if Journal.SearchByType("will save in 10", 'System'):
        #Pausing script when world saving is announced
        failSafe()
        
    skillLvl    = Player.GetRealSkillValue('necromancy')
    manaLvl     = Player.Mana
    if skillLvl < 30:
        if manaLvl < 11:
            regenMana()
        else:
            Spells.CastNecro('curse weapon')
    elif skillLvl < 55:
        if manaLvl < 17:
            regenMana()
        else:
            Spells.CastNecro('wraith form')
    elif skillLvl < 81:
        if manaLvl < 11:
            regenMana()
        else:
            Spells.CastNecro('horrific beast')
    elif skillLvl < 99.9:
        if manaLvl < 25:
            regenMana()
        else:
            Spells.CastNecro('lich form')
    elif skillLvl < 120:
        if manaLvl < 25:
            regenMana()
        else:
            Spells.CastNecro('vampiric embrace')

    pause(Break)
    
    if Journal.SearchByType("more reagents are needed",'System'):
        headMsg(err, "MORE REAGENTS NEEDED!!")
        crash()
        
    pause(delayCasts)
        
headMsg(reg, "Training is over!")
sys.exit()
    