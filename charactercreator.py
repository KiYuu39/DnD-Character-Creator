import random
from project import *

def rollStats(): #roll 6 main stats using 4d6 method: roll 4d6, drop the lowest of the four
    rolls = []
    stats = [0,0,0,0,0,0]
    for i in range(6):
        for d6 in range(4):
            x = random.randint(1,6)
            rolls.append(x)
        
        del rolls[rolls.index(min(rolls))]
        rollSum = sum(rolls)
        stats[i] = rollSum
        rolls=[]
    return stats

def titlePrint():
    print("\t\t\t\t\t\t________     __      ________   ")
    print("\t\t\t\t\t\t`MMMMMMMb.  6MMb     `MMMMMMMb. ")
    print("\t\t\t\t\t\t MM    `Mb 6M' `b     MM    `Mb ")
    print("\t\t\t\t\t\t MM     MM 8M  ,9     MM     MM ")
    print("\t\t\t\t\t\t MM     MM YM.,9  ___ MM     MM ")
    print("\t\t\t\t\t\t MM     MM  `Mb   `M' MM     MM ")
    print("\t\t\t\t\t\t MM     MM ,M'MM   P  MM     MM ")
    print("\t\t\t\t\t\t MM     MM MM  YM. 7  MM     MM ")
    print("\t\t\t\t\t\t MM     MM MM   `Mb   MM     MM ")
    print("\t\t\t\t\t\t MM    .M9 YM.   7MM  MM    .M9 ")
    print("\t\t\t\t\t\t_MMMMMMM9'  YMMM9  YM_MMMMMMM9' ")
                                
    print("   ____   ___                                                                         ____                                                    ")
    print("  6MMMMb/ `MM                                                                        6MMMMb/                                                  ")
    print(" 8P    YM  MM                                           /                           8P    YM                            /                     ")
    print("6M      Y  MM  __      ___   ___  __    ___     ____   /M      ____  ___  __       6M      Y ___  __   ____      ___   /M      _____  ___  __ ")
    print("MM         MM 6MMb   6MMMMb  `MM 6MM  6MMMMb   6MMMMb./MMMMM  6MMMMb `MM 6MM       MM        `MM 6MM  6MMMMb   6MMMMb /MMMMM  6MMMMMb `MM 6MM ")
    print("MM         MMM9 `Mb 8M'  `Mb  MM69 \" 8M'  `Mb 6M'   Mb MM    6M'  `Mb MM69 \"       MM         MM69 \" 6M'  `Mb 8M'  `Mb MM    6M'   `Mb MM69 \" ")
    print("MM         MM'   MM     ,oMM  MM'        ,oMM MM    `' MM    MM    MM MM'          MM         MM'    MM    MM     ,oMM MM    MM     MM MM'    ")
    print("MM         MM    MM ,6MM9'MM  MM     ,6MM9'MM MM       MM    MMMMMMMM MM           MM         MM     MMMMMMMM ,6MM9'MM MM    MM     MM MM   ")  
    print("YM      6  MM    MM MM'   MM  MM     MM'   MM MM       MM    MM       MM           YM      6  MM     MM       MM'   MM MM    MM     MM MM     ")
    print(" 8b    d9  MM    MM MM.  ,MM  MM     MM.  ,MM YM.   d9 YM.  ,YM    d9 MM            8b    d9  MM     YM    d9 MM.  ,MM YM.  ,YM.   ,M9 MM     ")
    print("  YMMMM9  _MM_  _MM_`YMMM9'Yb_MM_    `YMMM9'Yb.YMMMM9   YMMM9 YMMMM9 _MM_            YMMMM9  _MM_     YMMMM9  `YMMM9'Yb.YMMM9 YMMMMM9 _MM_    \n\n\n")

def main():
    #=====6 main stats======================================================================================================================
    stats = [0,0,0,0,0,0]
    stats = rollStats()

    level = 0

    #=====default proficiency values======================================================================================================================
    savethrows = [False,False,False,False,False,False]
    proflist = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    #=====print title======================================================================================================================
    titlePrint()

    #=====get name======================================================================================================================
    print("Please note: if provided a numbered list, please enter corresponding number.\n")
    name = input("Enter character name: ")
    
    #=====get background======================================================================================================================
    print("\nBackgrounds: ")
    print("\t1. Acolyte\n\t2. Charlatan\n\t3. Criminal\n\t4. Spy\n\t5. Entertainer\n\t6. Folk hero\n\t7. Gladiator\n\t8. Guild artisan\n\t9. Guild merchant\n\t10. Hermit\n\t11. Knight\n\t12. Noble\n\t13. Outlander\n\t14. Pirate\n\t15. Sage\n\t16. Sailor\n\t17. Soldier\n\t18.Urchin")
    bkg = 0                 #numerical marker for background
    backgroundString = ""   #string form of background for output file
    while bkg<1 or bkg>18:
        bkg = int(input("Enter background: "))
        if bkg<1 or bkg>18:
            print("Please enter valid number.\n")
        match bkg:
            case 1:
                backgroundString = "Acolyte"
            case 2:
                backgroundString = "Charlatan"
            case 3:
                backgroundString = "Criminal"
            case 4:
                backgroundString = "Spy"
            case 5:
                backgroundString = "Entertainer"
            case 6:
                backgroundString = "Folk Hero"
            case 7:
                backgroundString = "Gladiator"
            case 8:
                backgroundString = "Guild Artisan"
            case 9:
                backgroundString = "Guild Merchant"
            case 10:
                backgroundString = "Hermit"
            case 11:
                backgroundString = "Knight"
            case 12:
                backgroundString = "Noble"
            case 13:
                backgroundString = "Outlander"
            case 14:
                backgroundString = "Pirate"
            case 15:
                backgroundString = "Sage"
            case 16:
                backgroundString = "Sailor"
            case 17:
                backgroundString = "Soldier"
            case 18:
                backgroundString = "Urchin"
    
    #=====get class, subclass, class features======================================================================================================================
    valid = False
    nameblock = ""          #basic info block that goes with character name
    featuresblock = ""      #block of class-related features (added to end of character sheet with other features)
    num = 0                 #temporary class type holder
    ch_class = 0            #class type value
    arcaneTrickster = False #value needed later if player chooses arcane trickster subclass
    
    while not valid: #will loop until valid number is entered (1-12)
        print("\nClasses: ")
        print("\t1. Barbarian\n\t2. Bard\n\t3. Cleric\n\t4. Druid\n\t5. Fighter\n\t6. Monk\n\t7. Paladin\n\t8. Ranger\n\t9. Rogue\n\t10. Sorcerer\n\t11. Warlock\n\t12. Wizard")
        num = int(input("Enter class: "))

        match num:
            case 1:
                valid = True
                ch = Barbarian()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 1
                level = ch.getLevel()
            case 2:
                valid = True
                ch = Bard()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 2
                level = ch.getLevel()
            case 3:
                valid = True
                ch = Cleric()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 3
                level = ch.getLevel()
            case 4:
                valid = True
                ch = Druid()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 4
                level = ch.getLevel()
            case 5:
                valid = True
                ch = Fighter()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 5
                level = ch.getLevel()
            case 6:
                valid = True
                ch = Monk()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 6
                level = ch.getLevel()
            case 7:
                valid = True
                ch = Paladin()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 7
                level = ch.getLevel()
            case 8:
                valid = True
                ch = Ranger()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 8
                level = ch.getLevel()
            case 9:
                valid = True
                ch = Rogue()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 9
                level = ch.getLevel()
                arcaneTrickster = ch.getArcaneTrickster
            case 10:
                valid = True
                ch = Sorcerer()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 10
                level = ch.getLevel()
            case 11:
                valid = True
                ch = Warlock()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 11
                level = ch.getLevel()
            case 12:
                valid = True
                ch = Wizard()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 12
                level = ch.getLevel()
            case _:
                print("Please enter a valid number.\n")

    #=====get race, race features======================================================================================================================
    racefile = open("race.txt","a")
    racefile.truncate(0)
    raceString=""           #string form of race for output file
    raceblock=""            #block of text for race-related features to be added at end of output file

    tag = ""                #used for specific races
    race = 0                #race type value
    size = "none"
    speed = 0

    print("\nRaces: ")
    print("\t1. Dragonborn\n\t2. Dwarf\n\t3. Elf\n\t4. Gnome\n\t5. Half Elf\n\t6. Halfling\n\t7. Half Orc\n\t8. Human\n\t9. Tiefling")
    while race>9 or race<1: #loops until valid number is entered (1-9)
        race = int(input("Enter race: "))
        if race>9 or race<1:
            print("Please enter valid number.\n")
    
    match race: #get/calculate all race-related stats & proficiencies
        case 1: #dragonborn
            ancestry = 0
            stats[0]+=2
            stats[5]+=1
            size = "medium"
            speed = 30
            raceString="Dragonborn"

            print("Draconic ancestry colors:")
            print("\t1. Black\n\t2. Copper\n\t3. Blue\n\t4. Bronze\n\t5. Brass\n\t6. Gold\n\t7. Red\n\t8. Green\n\t9. Silver\n\t10. White")
            while ancestry<1 or ancestry>10:
                ancestry = int(input("Enter draconic ancestry: "))
                if ancestry<1 or ancestry>10:
                    print("Please enter valid number.\n")
                elif ancestry==1 or ancestry==2:
                    element = "acid\tBreath weapon: 5x30ft line, DEX save\nResistance to acid\n"
                elif ancestry==3 or ancestry==4:
                    element = "lightning\tBreath weapon: 5x30ft line, DEX save\nResistance to lightning"
                elif ancestry==5:
                    element = "fire\tBreath weapon: 5x30ft line, DEX save\nResistance to fire\n"
                elif ancestry==6 or ancestry==7:
                    element = "fire\tBreath weapon: 15ft cone, DEX save\nResistance to fire\n"
                elif ancestry==8:
                    element = "poison\tBreath weapon: 15ft cone, DEX save\nResistance to poison"
                elif ancestry==9 or ancestry==10:
                    element = "cold\tBreath weapon: 15ft cone, CON save\nResistance to cold\n"

            racefile.write(element)
            racefile.write("\nLanguages: Common, draconic\n")

        case 2: #dwarf
            stats[2]+=2
            size = "medium"
            racefile.write("Speed not reduced by heavy armor\n")
            racefile.write("Darkvision 60ft\n")
            racefile.write("Dwarven resilience\nDwarven combat training\nStonecunning\nTool proficiency: Mason's tools\n")
            racefile.write("Languages: Common, dwarvish\n")

            dtype = 0
            print("Dwarf types:\n\t1. Hill dwarf\n\t2. Mountain dwarf")
            while dtype<1 or dtype>2:
                dtype = int(input("Enter dwarf type: "))
                if dtype<1 or dtype>2:
                    print("Please enter valid number.\n")
                elif dtype==1:
                    stats[4]+=1
                    tag = "hill"
                    raceString="Hill Dwarf"
                elif dtype==2:
                    stats[0]+=2
                    racefile.write("Proficiency in light & medium armor\n")
                    raceString="Mountain Dwarf"

        case 3: #elf
            stats[1]+=2
            size = "medium"
            speed = 30
            racefile.write("Fey ancestry\nTrance\n")
            #darkvision, language

            etype = 0
            print("Elf types:\n\t1. Dark elf\n\t2. High elf\n\t3. Wood elf")
            while etype<1 or etype>3:
                etype = int(input("Enter elf type: "))
                if etype<1 or etype>3:
                    print("Please enter valid number.\n")
                elif etype==1:
                    stats[5]+=1
                    racefile.write("Superior darkvision 120ft\n")
                    racefile.write("Drow magic (dancing lights)\n")
                    racefile.write("Drow weapon training\n")
                    racefile.write("Languages: common, elven")
                    raceString="Dark Elf"
                elif etype==2:
                    stats[3]+=1
                    racefile.write("1 wizard cantrip (INT spellcast ability)\n")
                    racefile.write("Elf weapon training\n")
                    racefile.write("Languages: common, elven, additional language of choice\n")
                    raceString="High Elf"
                elif etype==3:
                    stats[4]+=1
                    racefile.write("Elf weapon training\nMask of the wild\n")
                    speed = 35
                    raceString="Wood Elf"
        
        case 4: #gnome
            stats[3]+=2
            size = "small"
            speed = 25
            racefile.write("Darkvision 60ft\nGnome cunning\n")
            racefile.write("Languages: Common, gnomish\n")

            gtype = 0
            print("Gnome types:\n\t1. Forest gnome\n\t2. Rock gnome")
            while gtype<1 or gtype>2:
                gtype = int(input("Enter gnome type: "))
                if gtype<1 or gtype>2:
                    print("Please enter valid number.\n")
                elif gtype==1:
                    stats[1]+=1
                    racefile.write("Natural illusionist (INT)\nSpeak with small beasts\n")
                    raceString="Forest Gnome"
                elif gtype==2:
                    stats[2]+=1
                    racefile.write("Artificer's lore\nTinker (clockwork toy, fire starter, music box)\n")
                    raceString="Rock Gnome"

        case 5: #half elf
            stats[5]+=2
            stats[1]+=1
            stats[3]+=1
            size = "medium"
            speed = 30
            racefile.write("Darkvision 60ft\nFey ancestry\nLanguages: Common, elven, additional language of choice\n")
            racefile.write("Half-elf versatility\n")

        case 6: #halfling
            stats[1]+=2
            size = "small"
            speed = 25
            racefile.write("Lucky\nBrave\nNimble\nLanguages: Common, halfling\n")

            htype = 0
            print("Halfling types:\n\t1. Lightfoot halfling\n\t2. Stout halfling")
            while htype<1 or htype>2:
                htype = int(input("Enter halfling type: "))
                if htype<1 or htype>2:
                    print("Please enter valid number.\n")
                elif htype==1:
                    stats[5]+=1
                    racefile.write("Naturally stealthy\n")
                    raceString="Lightfoot Halfling"
                elif htype==2:
                    stats[2]+=1
                    racefile.write("Stout resilience\n")
                    raceString="Stout Halfling"

        case 7: #half orc
            stats[0]+=2
            stats[2]+=1
            size = "medium"
            speed = 30
            racefile.write("Darkvision 60ft\nRestless endurance\nSavage attacks\nLanguages: Common, orc\n")
            tag = "orc"
            raceString="Half Orc"
        
        case 8: #human
            for i in range(6):
                stats[i]+=1
            size = "medium"
            speed = 30
            racefile.write("Languages: Common, additional language of choice")
            raceString="Human"

        case 9: #tiefling
            stats[5]+=2
            size = "medium"
            speed = 30
            racefile.write("Darkvision 60ft\nHellish resistance\nLanguages: Common, infernal\n")
            raceString="Tiefling"

    racefile.close()
    with open("race.txt","r") as x:
        raceblock = x.read().rstrip()
    
    #=====proficiencies======================================================================================================================
    proffile = open("additional_proficiencies.txt","a")
    proffile.truncate(0)

    match ch_class: #saving throw/skill proficiencies per race
        case 1: #barbarian
            savethrows[0]=True
            savethrows[2]=True
            proffile.write("Armor proficiencies: light armor, medium armor, shields\nWeapon proficiencies: simple weapons, martial weapons\n")
            proflist[7]=True
            proflist[17]=True
        case 2: #bard
            savethrows[1]=True
            savethrows[2]=True
            proffile.write("Armor proficiencies: light armor\nWeapon proficiencies: simple weapons, hand crossbows, longswords, rapiers, shortswords\nTools: three musical instruments of choice\n")
            proflist[12]==True
            proflist[13]==True
            proflist[0]==True
        case 3: #cleric
            savethrows[4]=True
            savethrows[5]=True
            proffile.write("Armor proficiencies: light armor, medium armor, shields\nWeapon proficiencies: all simple weapons\n")
            proflist[9]=True
            proflist[14]=True
        case 4: #druid
            savethrows[3]=True
            savethrows[4]=True
            proffile.write("Armor proficiencies: light armor, medium armor, shields (nothing made of metal for armor and shields)\nWeapon proficiencies: clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears\nTools: herbalism kit\n")
            proflist[1]=True
            proflist[10]=True
        case 5: #fighter
            savethrows[0]=True
            savethrows[2]=True
            proffile.write("Armor proficiencies: all armor, shields\nWeapon proficiencies: simple weapons, martial weapons\n")
            proflist[3]=True
            proflist[17]=True
        case 6: #monk
            savethrows[0]=True
            savethrows[1]=True
            proffile.write("Weapon proficiencies: simple weapons, shortswords\nTool proficiencies: A musical instrument\n")
            proflist[0]=True
            proflist[7]=True
        case 7: #paladin
            savethrows[4]=True
            savethrows[5]=True
            proffile.write("Armor proficiencies: all armor, shields\nWeapon proficiencies: simple weapons, martial weapons\n")
            proflist[6]=True
            proflist[14]=True
        case 8: #ranger
            savethrows[0]=True
            savethrows[1]=True
            proffile.write("Armor proficiencies: light armor, medium armor, shields\nWeapon proficiencies: simple weapons, martial weapons\n")
            proflist[1]=True
            proflist[8]=True
            proflist[10]=True
        case 9: #rogue
            savethrows[1]=True
            savethrows[3]=True
            proffile.write("Armor proficiencies: light armor\nWeapon proficiencies: simple weapons, hand crossbows, longswords, rapiers, shortswords\nTools: thieves' tools")
            proflist[4]=True
            proflist[6]=True
            proflist[15]=True
            proflist[16]=True
        case 10: #sorcerer
            savethrows[2]=True
            savethrows[5]=True
            proffile.write("Weapon proficiencies: daggers, darts, slings, quarterstaffs, light crossbows\n")
            proflist[2]=True
            proflist[14]=True
        case 11: #warlock
            savethrows[4]=True
            savethrows[5]=True
            proffile.write("Armor proficiencies: light armor\nWeapon proficiencies: simple weapons\n")
            proflist[5]=True
            proflist[14]=True
        case 12: #wizard
            savethrows[3]=True
            savethrows[4]=True
            proffile.write("Weapon proficiencies: daggers, darts, slings, quarterstaffs, light crossbows\n")
            proflist[2]=True
            proflist[5]=True

    if tag=="orc": #from half-orc race
        proflist[7]==True

    #=====background-related skill proficiencies & features======================================================================================================================
    match bkg:
        case 1:
            proflist[6]=True
            proflist[14]=True
            proffile.write("Two additional languages known\nShelter of the Faithful\n")
        case 2:
            proflist[4]=True
            proflist[15]=True
            proffile.write("Additional tool proficiencies: disguise kit, forgery kit\n")
        case 3 | 4:
            proflist[4]=True
            proflist[16]=True
            proffile.write("Additional tool proficiencies: gaming set, thieves' tools\n")
        case 5:
            proflist[0]=True
            proflist[12]=True
            proffile.write("Additional tool proficiencies: disguise kit, one additional musical instrument\n")
        case 6|7:
            proflist[1]=True
            proflist[17]=True
            proffile.write("Additional tool proficiencies: artisan's tools, land vehicles\n")
        case 8|9:
            proflist[6]=True
            proflist[13]=True
            proffile.write("Additional tool proficiencies: artisan's tools\nAdditional languages: 1\n")
        case 10:
            proflist[9]=True
            proflist[14]=True
            proffile.write("Additional tool proficiencies: herbalism kit\nAdditional languages: 1\n")
        case 11|12:
            proflist[13]=True
            proflist[5]=True
            proffile.write("Additional tool proficiencies: gaming set\nAdditional languages: 1\n")
        case 13:
            proflist[3]=True
            proflist[17]=True
            proffile.write("Additional tool proficiencies: one additional musical instrument of choice\nAdditional languages: 1\n")
        case 14|16:
            #athletics, perception
            #navigators tools, water vehicles
            proflist[4]=True
            proflist[11]=True
            proffile.write("Additional tool proficiencies: navigator's tools, water vehicles\n")
        case 15:
            #arcana, history
            #2 languages
            proflist[2]=True
            proflist[5]=True
            proffile.write("Additional languages: 2\n")
        case 17:
            proflist[3]=True
            proflist[7]=True
            proffile.write("Additional tool proficiencies: gaming set, land vehicles\n")
        case 18:
            #sleight of hand, stealth
            #disguise kit, thieves' tools
            proflist[15]=True
            proflist[16]=True
            proffile.write("Additional tool proficiencies: thieves' tools\n")

    proffile.close()
    addfeatsblock=""
    with open("additional_proficiencies.txt","r") as x:
        addfeatsblock = x.read().rstrip()

    #=====spellcasting======================================================================================================================
    spellfile = open("spellslots.txt","a")
    spellfile.truncate(0)

    match ch_class:
        #2,3,4,7,8,9(arcane trickster),10,11,12
        case 2: #bard
            if level==1:
                spellfile.write("Known cantrips: 2\nKnown spells: 4\n\n1st: 2")
            elif level==2:
                spellfile.write("Known cantrips: 2\nKnown spells: 5\n\n1st: 3")
            elif level==3:
                spellfile.write("Known cantrips: 2\nKnown spells: 6\n\n1st: 4\n2nd: 2")
        case 3: #cleric
            if level==1:
                spellfile.write("Known cantrips: 3\n\n1st: 2")
            elif level==2:
                spellfile.write("Known cantrips: 3\n\n1st: 3")
            elif level==3:
                spellfile.write("Known cantrips: 3\n\n1st: 4\n2nd: 2")
        case 4: #druid
            if level==1:
                spellfile.write("Known cantrips: 2\n\n1st: 2")
            elif level==2:
                spellfile.write("Known cantrips: 2\n\n1st: 3")
            elif level==3:
                spellfile.write("Known cantrips: 2\n\n1st: 4\n2nd:2")
        case 7: #paladin
            if level==1:
                spellfile.write("Known cantrips: 0")
            elif level==2:
                spellfile.write("Known cantrips: 2")
            elif level==3:
                spellfile.write("Known cantrips: 3")
        case 8: #ranger
            if level==1:
                spellfile.write("Known spells: 0\n")
            elif level==2:
                spellfile.write("Known spells: 2\n\n1st: 2\n")
            elif level==3:
                spellfile.write("Known spells: 3\n\n1st: 3\n")
        case 9: #rogue (arcane trickster only)
            if arcaneTrickster:
                spellfile.write("Known cantrips: Mage Hand +2\nKnown spells: 3\n\n1st: 2")
        case 10: #sorcerer
            if level==1:
                spellfile.write("Known cantrips: 4\nKnown spells: 2\n\n1st: 2")
            elif level==2:
                spellfile.write("Known cantrips: 4\nKnown spells: 3\n\n1st: 3")
            elif level==3:
                spellfile.write("Known cantrips: 4\nKnown spells: 4\n\n1st: 4\n2nd: 2\n")
        case 11: #warlock
            if level==1:
                spellfile.write("Known cantrips: 2\nKnown spells: 2\n\nSpell slots: 1\nSlot level: 1st\nInvocations known: 0\n")
            elif level==2:
                spellfile.write("Known cantrips: 2\nKnown spells: 3\n\nSpell slots: 2\nSlot level: 1st\nInvocations known: 2\n")
            elif level==3:
                spellfile.write("Known cantrips: 2\nKnown spells: 4\n\nSpell slots: 2\nSlot level: 2nd\nInvocations known: 2\n")
        case 12: #wizard
            if level==1:
                spellfile.write("Known cantrips: 3\n\n1st: 2\n")
            elif level==2:
                spellfile.write("Known cantrips: 3\n\n1st: 3\n")
            elif level==3:
                spellfile.write("Known cantrips: 3\n\n1st: 4\n2nd: 2\n")
        case _:
            spellfile.write("This class does not spellcast.\n\n")
        
    spellfile.close()
    spellsblock=""  #block of text for spell-related information
    with open("spellslots.txt","r") as x:
        spellsblock = x.read().rstrip()

    #=====convert main 6 stats via stat table method======================================================================================================================
    convertedstats = [0,0,0,0,0,0]  #6 main stats will be converted into bonuses (+/-)
    for i in range(6):
        if stats[i]==3:
            convertedstats[i] = -4
        elif stats[i]==4 or stats[i]==5:
            convertedstats[i] = -3
        elif stats[i]==7 or stats[i]==7:
            convertedstats[i] = -2
        elif stats[i]==8 or stats[i]==9:
            convertedstats[i] = -1
        elif stats[i]==13 or stats[i]==14:
            convertedstats[i] = 1
        elif stats[i]==15 or stats[i]==16:
            convertedstats[i] = 2
        elif stats[i]==17 or stats[i]==18:
            convertedstats[i] = 3
        elif stats[i]==19:
            convertedstats[i] = 4
        elif stats[i]==20:
            convertedstats[i] = 5
        else:
            convertedstats[i] = 0
            
    #=====HP calculation======================================================================================================================
    hp=0
    match ch_class:
        case 1:
            if level==1:
                hp=12+convertedstats[2]
            elif level==2:
                hp=19+(2*convertedstats[2])
            elif level==3:
                hp=26+(3*convertedstats[2])
        case 2:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 3:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 4:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 5:
            if level==1:
                hp=10+convertedstats[2]
            elif level==2:
                hp=16+(2*convertedstats[2])
            elif level==3:
                hp=22+(3*convertedstats[2])
        case 6:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 7:
            if level==1:
                hp=10+convertedstats[2]
            elif level==2:
                hp=16+(2*convertedstats[2])
            elif level==3:
                hp=22+(3*convertedstats[2])
        case 8:
            if level==1:
                hp=10+convertedstats[2]
            elif level==2:
                hp=16+(2*convertedstats[2])
            elif level==3:
                hp=22+(3*convertedstats[2])
        case 9:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 10:
            if level==1:
                hp=6+convertedstats[2]
            elif level==2:
                hp=10+(2*convertedstats[2])
            elif level==3:
                hp=14+(3*convertedstats[2])
        case 11:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 12:
            if level==1:
                hp=6+convertedstats[2]
            elif level==2:
                hp=10+(2*convertedstats[2])
            elif level==3:
                hp=14+(3*convertedstats[2])

    if tag=="hill": #tag for hill dwarf
        hp+=level

    #=====additional skills======================================================================================================================
    bkgfile = open("other_skills.txt","a")
    bkgfile.truncate(0)

    num = 0         #temporary number to hold skill bonus
    box = ""        #proficient/non proficient checkbox string
    for i in range(18):
        num=0
        if proflist[i]==True:
            box="[x]"
            num+=2
        else:
            box="[ ]"

        #STR
        if i==3:
            num+=convertedstats[0]
            bkgfile.write(f"{box} Athletics: ")
            if num<0:
                bkgfile.write("{0:-}".format(num))
            else:
                bkgfile.write("{0:+}".format(num))
            bkgfile.write("\n")
        #DEX
        if i==0 or i==15 or i==16:
            num+=convertedstats[1]
            if i==0:
                bkgfile.write(f"{box} Acrobatics: ")
            elif i==15:
                bkgfile.write(f"{box} Sleight of Hand: ")
            elif i==16:
                bkgfile.write(f"{box} Stealth: ")
            if num<0:
                bkgfile.write("{0:-}".format(num))
            else:
                bkgfile.write("{0:+}".format(num))
            bkgfile.write("\n")
        #no CON based substats
        #INT
        if i==2 or i==5 or i==8 or i==10 or i==14:
            num+=convertedstats[3]
            if i==2:
                bkgfile.write(f"{box} Arcana: ")
            elif i==5:
                bkgfile.write(f"{box} History: ")
            elif i==8:
                bkgfile.write(f"{box} Investigation: ")
            elif i==10:
                bkgfile.write(f"{box} Nature: ")
            elif i==14:
                bkgfile.write(f"{box} Religion: ")
            if num<0:
                bkgfile.write("{0:-}".format(num))
            else:
                bkgfile.write("{0:+}".format(num))
            bkgfile.write("\n")
        #WIS
        if i==1 or i==6 or i==9 or i==11 or i==17:
            num+=convertedstats[4]
            if i==1:
                bkgfile.write(f"{box} Animal Handling: ")
            elif i==6:
                bkgfile.write(f"{box} Insight: ")
            elif i==9:
                bkgfile.write(f"{box} Medicine: ")
            elif i==11:
                bkgfile.write(f"{box} Perception: ")
            elif i==17:
                bkgfile.write(f"{box} Survival: ")
            if num<0:
                bkgfile.write("{0:-}".format(num))
            else:
                bkgfile.write("{0:+}".format(num))
            bkgfile.write("\n")
        #CHA
        if i==4 or i==7 or i==12 or i==13:
            num+=convertedstats[5]
            if i==4:
                bkgfile.write(f"{box} Deception: ")
            elif i==7:
                bkgfile.write(f"{box} Intimidation: ")
            elif i==12:
                bkgfile.write(f"{box} Performance: ")
            elif i==13:
                bkgfile.write(f"{box} Persuasion: ")
            if num<0:
                bkgfile.write("{0:-}".format(num))
            else:
                bkgfile.write("{0:+}".format(num))
            bkgfile.write("\n")

    bkgfile.close()
    bkgblock=""
    with open("other_skills.txt","r") as x:
        bkgblock = x.read().rstrip()

    #=====put everything in a file======================================================================================================================
    bigbar = "-----------------------------------------------------------------------------------------------------\n"
    sheet = open("final_character_sheet.txt","a")
    sheet.truncate(0)

    sheet.write("Character name: ")
    sheet.write(f"{name}\n{nameblock}\nRace: {raceString}\nBackground: {backgroundString}\n")
    sheet.write(bigbar)

    #proficiency bonus
    sheet.write("Proficiency bonus: +2\n")

    #maxHP
    sheet.write(f"HP: {hp}\n")
    #AC
    if ch_class==6: #monks have different AC calculation, assuming unarmored
        ac=10+convertedstats[1]+convertedstats[4]
        sheet.write("Unarmored ")
    else:
        ac = 10+convertedstats[1]
    sheet.write(f"Base AC: {ac}\n")

    #initiative
    sheet.write(f"Speed: {speed} ft\n")
    sheet.write(f"Size: {size}\n")
    sheet.write("Initiative: ")
    sheet.write("{0:+}".format(convertedstats[1]))
    sheet.write("\n")
    
    sheet.write(bigbar)

    #6 main stats
    sheet.write(f"STR: {stats[0]}\t|DEX: {stats[1]}\t|CON: {stats[2]}\t|INT: {stats[3]}\t|WIS: {stats[4]}\t|CHA: {stats[5]}\n")
    sheet.write(bigbar)

    #saving throws
    temp = ""       #temporary bonus number holder
    savestring=""   #string to be written into file
    for i in range(6):
        if savethrows[i]==True:
            box="[x]"
            temp = 2+convertedstats[i]
        else:
            box="[ ]"
            temp = convertedstats[i]
        
        match i:
            case 0:
                savestring=box+" Strength: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)
            case 1:
                savestring=box+" Dexterity: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)
            case 2:
                savestring=box+" Constitution: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)
            case 3:
                savestring=box+" Intelligence: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)
            case 4:
                savestring=box+" Wisdom: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)
            case 5:
                savestring=box+" Charisma: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)

    #additional proficiencies
    sheet.write("\n")
    sheet.write(bkgblock)
    sheet.write("\n")
    sheet.write(bigbar)

    #spellcasting
    sheet.write(spellsblock)
    sheet.write("\n")
    sheet.write(bigbar)

    #additional features
    sheet.write(f"{featuresblock}\n\n")
    sheet.write(f"{raceblock}\n\n")
    sheet.write(f"{addfeatsblock}\n")
    

    sheet.close()
    print("\nCharacter sheet complete.\n\n\n")
    
    #display to console
    with open("final_character_sheet.txt","r") as x:
        final = x.read().strip()
    
    print(final)
    print("\n\n")



                                                                                                                                              



if __name__ == "__main__":
    main()


'''featuresfile = open("features.txt","a")
        featuresfile.write("test\ntest\ntest")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        #print(filestring)'''