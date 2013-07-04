
from BaseRoutines import *
from BaseClasses import *

import pickle

class WeaponClass(ItemClass,RepairClass):
    def GetAttackValue(self):
        #add code to account of deteriorating performance
        if self.RepairOk():
            ret_val=self.attack_points
        else:
            ret_val=0
        return ret_val

    def Attack(self):
        ret_val=self.GetAttackValue()
        self.Use()
        return ret_val

    
class WeaponShortSwordClass(WeaponClass):
    def __init__(self,ownerid):
        ItemClass.__init__(self,ownerid)
        self.attack_points=1
        self.total_repair=5
        self.name="short sword"
        

