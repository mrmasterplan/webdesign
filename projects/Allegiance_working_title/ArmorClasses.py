
from BaseRoutines import *

from BaseClasses import *

class ArmorClass(ItemClass,RepairClass):
    def GetDefenceValue(self):
        #add code to account of deteriorating performance
        if self.RepairOk():
            ret_val=self.defence_points
        else:
            ret_val=0
        return ret_val

    def Defend(self):
        ret_val=self.GetDefenceValue()
        self.Use()
        return ret_val

class ArmorRagsClass(ArmorClass):
    def __init__(self,ownerid):
        ItemClass.__init__(self,ownerid)
        self.defence_points=1
        self.total_repair=5
        self.name = "rags"
