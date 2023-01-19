#//***********************************************************
#// file name : train_remove_trap_0.0.1b.py
#// version   : 0.0.1 full bereta test
#// Date      : 2023-01-02
#// By        : Malkari
#//
#// This script will grow the skill Remove Trap up to 80.0
#// using:
#//
#//     - a chest
#//     - magery
#//     - chivalry
#//     - A lot of your time.. A LOT!
#//
#// Suggested setup
#// ---------------
#//  - A chest (lock it down in the place)
#//  - LRC 100 gears
#//  - Magery & Chivalry spell books
#//  - The ability to cast the spells Agility & Divine 
#//    Fury.
#//
#// Then what?
#// ----------
#// Start the script, select the chest to train on and..
#// ..that is it!
#//
#// What is it doing?
#// -----------------
#// The script will cast the Magic Trap spell on the
#// chest and then will try to remove the trap. Every
#// 130 seconds, the Agility and Divine Fury spells will be
#// casted to boost the dexterity.
#//
#// Skill Ball safe
#// ---------------
#// This script comes with a Skill Ball safe, which means that
#// when active, the script wills top at 60.0. See instructions
#// below to activate.
#//
#// World Saving Fail Safe
#// ----------------------
#// This script has a fail safe feature and should stop for
#// for 15 seconds when the 10 seconds left before saving the
#// world announcement is done (keyword: should).
#//
#// A note from the scripter..
#// --------------------------
#// BY DEFAULT THE SCRIPT DOES NOT TRY UNTIL TRAP IS REMOVED
#// It only try once and trap the chest again. At the time
#// of writing these lines, both way were growing the skill.
#// See below for how to change the method to remove the
#// trap completely before continuing.
#//
#// You are the only one responsible for whatever can happen
#// when using this script; I am not in any way.
#//***********************************************************

clean = False #Change this value for True if you want the trap
              #completely removed before continuing.

useSkillBall = False #Change this value for True if you
                     #intend to use your skill ball.

#//*********************************************************
#//*********************************************************
#//*********************************************************
#//****** GO BELOW ONLY IF YOU KNOW WHAT YOU'RE DOING ******
#//*********************************************************
#//*********************************************************
#//*********************************************************
import sys

cap = 80
delayTimerAgility = 130000

chest = None
pauseAgility = 2000
skillname = "remove trap"

Err = 33
Reg = 55
Warn = 44

#// *** crash() *** \\
#// Terminates the script. Created to lighten the code.
#//  - Returns: nothing
def crash():
    sys.exit()
    
#// *** pause() *** \\
#// Simple pause using the Misc library. Created to lighten the code.
#//  - Returns: nothing
def pause(tTime):
    Misc.Pause(tTime)

#// *** failSafe() *** \\
#// Temporary pause the script for 15 seconds when the world saving is announced.
#//  - Returns: nothing
def failSafe():
    if Journal.SearchByType("will save in 10", 'System'):
        Journal.Clear()
        Player.HeadMessage(Warn, "MACRO: The world will save in 10 seconds..")
        pause(500)
        Player.HeadMessage(Reg, "Pausing script for 15 seconds..")
        pause(15000)
    else:
        pause(250)
    
#// *** castAgility() *** \\
#//  - Returns: nothing
def castAgility():
    Spells.CastMagery('agility')
    Target.WaitForTarget(10000)
    Target.Self()
    Timer.Create('timerAgility', delayTimerAgility)
    pause(pauseAgility)
    if Player.Stam < Player.StamMax:
        Spells.CastChivalry('divine fury')
        pause(pauseAgility)
    

#// *** trapChest(tChest) *** \\
#//  - Returns: nothing
def trapChest(tChest):
    Spells.CastMagery("Magic Trap")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(tChest)
    pause(5000)

#// *** removeTrap(tChest) *** \\
#//  - Returns: nothing
def removeTrap(tChest):
    if clean:
        failSafe()
    if not Timer.Check('timerAgility'):
        castAgility()
        pause(2000)

    Player.UseSkill(skillname)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(tChest)
    

#// *** cleanTrap(tChest) *** \\
#//  - Returns: nothing
def cleanTrap(tChest):
    Okay = False

    while not Okay:
        Journal.Clear()
        removeTrap(tChest)
        pause(1000)
        if not Journal.SearchByType('You fail', 'System'):
            Okay = True
        else:
            pause(10000)

#// *** promptChest() *** \\
#// Prompts for the chest to trap/untrap and validates something
#// has been selected. Otherwise, it terminates the script.
#//  - Returns: Item integer (serial)    
def promptChest():
    tChest = None
    Okay = False

    while not Okay:
        Player.HeadMessage(Reg, "MACRO: Select your training chest")
        tChest = Target.PromptTarget("MACRO: Select the chest to train on; ESC to cancel..", Reg)
        if tChest == -1:
            Player.HeadMessage(Err, "MACRO: Player cancelled.")
            crash()
        elif tChest == None:
            Player.HeadMessage(Err, "MACRO: ERROR NULL.. contact scripter")
            crash()
        else:
            Okay = True
            
    return tChest

    
#// *** main() *** \\
#// Validates the skill cap to reach, prompts for the chest
#// to use, traps the chest and removes the trap depending
#// the method chosen. The script stops when the skill 
#// reaches the cap wanted (max 80.0 points).

#Resetting the cap if higher then 80
if useSkillBall:
    cap = 60
elif cap > 80:
    cap = 80
    Player.HeadMessage(Warn, "MACRO: The skill cap you have set is higher than 80.")
    Player.HeadMessage(Reg, "Skill cap to reach reset to 80")
  
chest = promptChest()
Player.HeadMessage(Reg,"Remove Trap training started")
Journal.Clear()
while Player.GetRealSkillValue(skillname) < cap:
    failSafe()
    trapChest(chest)

    if clean:
        cleanTrap(chest)
    else:
        removeTrap(chest)
    
    pause(10000)

Player.HeadMessage(Reg, "MACRO: training is over!")
