#//*******************************************************
# filename  : grow_resisting_spells_0.0.2.py
# version   : 0.0.2b full testing 1-2
# Date      : 
# Author    : Malkari
# 
# Cast a target continuously with weaken and clumsy
# spells. Can also be used to grow your own Resisting
# Spells skill to it cap.
#
# How does it work?
# -----------------
# Run the macro and choose the target. By targeting
# yourself the training mode is activated and the script
# will cast you until your skill Resisting Spells reaches
# its cap. Otherwise, the script casts the target until
# you stop it manually or the target disappears.
#
# if you cast a pet, a lore gump will pop every 30
# seconds.
# 
# Then what?
# ----------
# That is it! Just enjoy and report bugs if you have
# any!
#
# Fail Safe
# ---------
# Some fail safes are activated on this script:
#   - Pause for world saving
#   - Stop when target cannot be found
#
# Version   : 0.0.2b - Jan. 10th 2023
#   - Added fail safes
#   - Added stop command from clumsied
#
# version   : 0.0.1b - Jan. 7th 2023
#
#//*******************************************************

castDelay = 3000 # Tested up to 500ms FC:2 FCR: 4

#***************************************************
#***************************************************
#***************************************************
#***************************************************
#***************************************************

clumsied = None
skillname = "Resist Spells"
training = False


Err = 33
Reg = 55
Warn = 44


#// *** castSpell(who) *** \\
# Casts Weaken and Clumsy spells on target.
# Receives: Mobile object.
def castSpells(who):
    Spells.CastMagery("weaken")
    Target.WaitForTarget(3000, False)
    Target.TargetExecute(who)
    pause(castDelay)
    Spells.CastMagery("clumsy")
    Target.WaitForTarget(3000, False)
    Target.TargetExecute(who)
    Target.ClearLastandQueue()
    pause(castDelay)

#// *** crash() *** \\
# Ends the script  
def crash():
    sys.exit()

#// *** failSafe() *** \\
# Temporary pause the script for 15 seconds when the world
# is about to save.
def failSafe():
    if Journal.SearchByType("will save in 10", 'System'):
        Journal.Clear()
        Player.HeadMessage(Warn, "MACRO: The world will save in 10 seconds..")
        pause(500)
        Player.HeadMessage(Reg, "Pausing script for 15 seconds..")
        pause(15000)
    
    
#// *** getTarget() *** \\    
# Prompt the user for target.
# Returns: Mobile object
def getTarget():
    Okay = False
    targ = None
    
    while not Okay:
        Player.HeadMessage(Reg, "MACRO: select target..")
        targ = Target.PromptTarget("MACRO: select target, <ESC> to cancel", Reg)

        if targ == -1:
            Misc.SendMessage("MACRO: Player cancelled.", 33)
            crash()
        elif targ == None:
            Misc.SendMessage("MACRO: ERROR NULL.. contact scripter.")
            crash()
        else:
            targ = Mobiles.FindBySerial(targ)
            Player.HeadMessage(Warn, "MACRO: Target acquired")

            if targ.Serial == Player.Serial:
                training = True
                Player.HeadMessage(Reg, "MACRO: TRAINING MODE ACTIVATED")
                
            Okay = True
    
    return targ #Something was selected..
    
#// *** lorePet(who) *** \\
# Use animal lore on non human
# Receives: Mobile object as parameter
def lorePet(who):
    if not Timer.Check('timerLore') and not Timer.Check('timerRegenMana'):
        if not who.IsHuman:
            Timer.Create('timerLore', 30000, "Loring..")
            Player.UseSkill('animal lore')
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(who)

#// *** pause(tTime) *** \\
# Pause the script using the Misc library.
# Receives: integer 
def pause(tTime):
        Misc.Pause(tTime)
        
#// *** regenMana() *** \\
# Regenerate the mana when dropping under 20
def regenMana():
    if Player.Mana < 7:
        while Player.Mana < Player.ManaMax:
            if not Timer.Check('timerRegenMana'):
                Player.HeadMessage(Warn, "MACRO: mana regen...")
                Player.UseSkill('meditation')
                Timer.Create('timerRegenMana', 11000)

#// *** main() *** \\
# Starts the script in training mode or not. Starts by
# promting for a target.
#
# In training: casts the spells and check mana
# Oterwise: casts spells, lore if it's a pet and check on mana
#
# Macro will stop if the target is lost.


Journal.Clear() # Avoiding all confusions from line 1[40]

clumsied = getTarget()

if training:
    while Player.GetRealSkillValue(skillname) < Player.GetSkillCap(skillname):
        failSafe()
        castSpells(Player.Serial)
        regenMana()
        
    Player.HeadMessage(Reg, "MACRO: Skill cap reached")
    
else:
    while True:
        if Mobiles.FindBySerial(clumsied.Serial):
            failSafe()
            castSpells(clumsied)
            
            if not clumsied.IsHuman:
                lorePet(clumsied)
                
            regenMana()
        else:
            Player.HeadMessage(Err, "MACRO: TARGET LOST")
            crash()
