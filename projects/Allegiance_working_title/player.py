
from GoldOwnerClass import GoldOwnerClass

from BaseRoutines import *

from BaseClasses import *

from WeaponClasses import *

import pickle
        


class SkillClass:
    pass

class FractionClass:
    pass

class PersonalFractionClass(FractionClass):
    pass

class BattleEvent:
    def __init__(attackerid, defenderid):
        self.AttackOwner=attackerid
        self.Defending=defenderid
        self.AttackMembers=[attackerid]
        self.DefenceMembers=[defendeidr]

    def DecideResult():
        attack_AttStat=0
        attack_DefStat=0
        for memberid in self.AttackMembers:
            member=PlayerClass.GetFromID(memberid)
            attack_AttStat+=member.GetAttack()
            attack_DefStat+=member.GetDefence()

        defence_AttStat=0
        defence_DefStat=0
        for memberid in self.DefenceMembers:
            member=PlayerClass.GetFromID(memberid)
            defence_AttStat+=member.GetAttack()
            defence_DefStat+=member.GetDefence()

        if attack_AttStat>defence_DefStat:
            #The Attack wins. Proceed to punish the loser and reward the winner
            #Weapon usage
            #Food usage
            #Gold transfer
            pass
        elif defence_AttStat>attack_DefStat:
            #Attack failed totally! Punish the attacker and reward the defence
            pass
        else:
            #stalemate. Everyone goes home
            pass

        #Loser uses more weapons, 
        
        
    

class PlayerClass(GoldOwnerClass):
    def __init__(self):
        self.Weapon=0
        self.Armor=0
        self.AttackStat=0
        self.DefendStat=0
        self.attack_points=0
        self.defence_points=0
        
        
        

    def GetFromID(playerid):
        #Load player from DB
        pass

    def Load(self,userid):
        #Find player with userid in DB and load all values
        pass

    def Create(self,userid):
        self.InitializeDefaults()
        self.SetUserID(userid)
        self.Fraction
        self.WriteToDB()

    def InitializeDefaults(self):
        self.SetName(default)
        self.SetGold(default)
       
    def SetUserID(self,userid):
        #Include code to test validity of userid here
        self.userid=userid
    
    def WriteToDB(self):
        pass

    def SetName(self,name):
        self.name=name

    def JoinFraction(fractionid):
        pass

    def EquipWeapon(self,weapon):
        self.Weapon=weapon

    def EquipArmor(self,armor):
        self.Armor=armor

    def GetAttackValue(self):
        value=self.attack_points
        if hasattr(self.Weapon,"GetAttackValue"):
            value+=self.Weapon.GetAttackValue()
        return value

    def GetAttackValue(self):
        value=self.defence_points
        if hasattr(self.Armor,"GetDefenceValue"):
            value+=self.Armor.GetDefenceValue()
        return value

          
