#//******************************************************************\\
# Filename  : train_spirit_speak_0.0.1.py
# Version   : 0.0.1b
# Date      : Jan. 22nd 2023
#
# Will rise the skill Spirit Speak to its cap!
#
# This skill does not damage your gears. Use everything boosting int
# and mana.
#
# DISCLAIMER: You are responsible for whatever is happening whhen
# using this script.
#
# Keep in mind this script is beta, so in testing phase. It can bug.
# Just report bugs, if you don't mind! 
#
# https://github.com/MalkScripts/RazorEnhanced
#
#********************************************************************
# Version 0.0.1b
# --------------
# Date      : Jan. 22nd 2023
#
# Simply uses the skill every 8 seconds. Regenerate the mana when 
# it is lower than 12.
#
#\\******************************************************************//

#********************************************************************
#********************************************************************
#********************************************************************
#********************************************************************
#********************************************************************

loopDelay   = 8000
minMana     = 80
skillname = "spirit speak"

reg     = 77
warn    = 44
    
def pause(thetime):
    Misc.Pause(thetime)
    
Player.HeadMessage(reg, "Beginning training..")

while Player.GetRealSkillValue(skillname) < Player.GetSkillCap(skillname):
    if Player.Mana < minMana:
        Player.UseSkill("meditation")
        while Player.Mana < Player.ManaMax:
            if not Timer.Check('timerManaRegen'):
                Player.HeadMessage(warn, "Regenerating mana..")
                Timer.Create('timerManaRegen', 5000)
            pause(1000)
            
    Player.UseSkill("Spirit Speak")
    pause(loopDelay)

Player.HeadMessage(reg, "Training over")
pause(500)
Player.HeadMessage(reg, "Script stopped.")
