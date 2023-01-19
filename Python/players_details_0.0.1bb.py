#//******************************************************************\\
# Filename  : players_details_0.0.1a.py
# Version   : 0.0.1bb Big Bertha test
# Date      : Jan. 19th 2023
#
# Retrieves the attirbutes of the player.
#
#********************************************************************
# Version 0.0.1b
# --------------
# Date      : Jan. 19th 2023
#
# Retrieves : Serial, Damage Inc., Defense Chance Inc., Dex. Bonus
#             Faster cast Recov. Faster Casting, Hit Chance Inc.
#             HP Inc., HP Regen., Int. Bonus, LMC, LRC, Luck, Mana
#             Regen. Selft Repair, Reflect Phys. Damage, Stam.
#             Regen., Str. Bonus, Cold Resist, Energy Resists,
#             Fire Resist, Physical Resists, Poison Resist, Strength
#             Desterity, Intelligence
#
# Displays  : Over head         : LMC & LRC and Resists
#             System messages   : all
#
# Restrict. : Can only be used on player.
#\\******************************************************************//

# Possible values : True (will display) or False (will not display)
show_local  = True # Details as system messages
show_magery = True # LMC & LRC publicly
show_resist = True # Resists details publicly
show_stats  = True # Stats details publicly

#\\******************************************************************//
#\\******************************************************************//
#\\******************************************************************//
#\\******************************************************************//
#\\******************************************************************//
#\\******************************************************************//

p       = Player
reg     = 55
reg2    = 44
reg3    = 66
#// *** overHead(col, msg) ***\\
# Post an in game message over player's head
# receives: int, str: color, message
def overHead(msg, color):
        Player.HeadMessage(color, msg)
        Misc.Pause(500)

def sysMsg(msg, color):
        Misc.SendMessage(msg, color)
        Misc.Pause(100)
        
cResist     = p.SumAttribute("Cold Resist")
damIncrease = p.SumAttribute("Damage Increase")
dcIncrease  = p.SumAttribute("Defense Chance Increase")
dexBonus    = p.SumAttribute("Dexterity bonus")
ePotion     = p.SumAttribute("Enhance Potions")
eResist     = p.SumAttribute("Energy Resist")
fResist     = p.SumAttribute("Fire Resist")
fcRecovery  = p.SumAttribute("Faster Cast Recovery")
fCasting    = p.SumAttribute("Faster Casting")
phResist    = p.SumAttribute("Physical Resist")
hcIncrease  = p.SumAttribute("Hit Chance Increase")
hpIncrease  = p.SumAttribute("Hit Point Increase")
hpRegen     = p.SumAttribute("Hit Point Regeneration")
intBonus    = p.SumAttribute("Intelligence bonus")
lmc         = p.SumAttribute("Lower Mana Cost")
lrc         = p.SumAttribute("Lower Reagent Cost")
luck        = p.SumAttribute("Luck")
manaRegen   = p.SumAttribute("Mana Regeneration")
pResist     = p.SumAttribute("Poison Resist")

reflectDam  = p.SumAttribute("Reflect Physical Damage")
sRepair     = p.SumAttribute("Self Repair")
stamRegen   = p.SumAttribute("Stamina Regeneration")
strBonus    = p.SumAttribute("Strength bonus")

if show_magery:
    overHead("LMC/LRC : {:n} / {:n}".format(lmc, lrc), reg)

if show_stats:
    overHead("Stats: {:n} / {:n} / {:n}".format(p.Str, p.Dex, p.Int), reg2)
    
if show_resist:
    overHead("Resist: {:n} / {:n} / {:n} / {:n} / {:n}".format(phResist, fResist, cResist, pResist, eResist), reg3)
    
if show_local:
    sysMsg("Your Serial: {:X}".format(p.Serial), reg)
    sysMsg("Stats: {:n} / {:n} / {:n}".format(p.Str, p.Dex, p.Int), reg)
    sysMsg("Strength bonus: {}".format(strBonus), reg)
    sysMsg("Dexterity bonus: {}".format(dexBonus), reg)
    sysMsg("Intelligence bonus: {}".format(intBonus), reg)

    sysMsg("Lower Mana Cost: {}".format(lmc), reg)
    sysMsg("Lower Reagent Cost: {}".format(lrc), reg)

    sysMsg("HP Regeneration: {}".format(hpRegen), reg)
    sysMsg("Mana Regeneration: {}".format(manaRegen), reg)
    sysMsg("Stamina Regeneration: {}".format(stamRegen), reg)

    sysMsg("Defense Chance Increase: {}".format(dcIncrease), reg)
    sysMsg("Damage Increase: {}".format(damIncrease), reg)
    sysMsg("HP Increase: {}".format(hpIncrease), reg)
    sysMsg("Hit Chance Increase: {}".format(hcIncrease), reg)
    sysMsg("Reflect Damage: {}".format(reflectDam), reg)
    sysMsg("Self Repair: {}".format(sRepair), reg)

    sysMsg("Faster Casting: {}".format(fCasting), reg)
    sysMsg("Faster Cast Recovery: {}".format(fcRecovery), reg)

    sysMsg("Physical Resist: {}".format(phResist), reg)
    sysMsg("Fire Resist: {}".format(fResist), reg)
    sysMsg("Cold Resist: {}".format(cResist), reg)
    sysMsg("Poison Resist: {}".format(pResist), reg)
    sysMsg("Energy Resist: {}".format(eResist), reg)

    sysMsg("Luck: {}".format(luck), reg)
    sysMsg("Enhance Potions:".format(ePotion), reg)
