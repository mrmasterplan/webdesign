
from BaseRoutines import *


class GoldOwnerClass:
    
    def SetGold(self,n_gold):
        self.mygoldvalue=n_gold

    def GetGold(self):
        try:
            currgold = self.mygoldvalue
        except AttributeError:
            self.mygoldvalue=0
            currgold=0
        return int(round(currgold,0))

    def TakeGold(self,n_gold):
        try:
            currgold=self.mygoldvalue
            if currgold<n_gold:
                return 0
            self.mygoldvalue-=n_gold
            return 1
        except AttributeError:
            return 0

    def AddGold(self,n_gold):
        try:
            self.mygoldvalue+=n_gold
        except AttributeError:
            self.mygoldvalue=n_gold
                
    def HasGold(self,n_gold):
        try:
            if self.mygoldvalue>=n_gold:
                return 1
        except AttributeError:
            pass
        return 0
            


class ItemClass:
    def __init__(self,ownerid):
        self.ownerid=ownerid
        self.id=GenerateUniqueID()
        return self.id

    def SetOwner(self,owner=0):
        self.owner=owner

    def DropOwner(self):
        self.SetOwner(0)
    
    def __del__(self):
        if self.owner:
            SystemWarning("Item dropped by "+self.owner)
    
class RepairClass:
    #When using this class remember to set total_repair
    #Things that require repair should check RepairOk()==1
    
    def __init__(self):
        #assumed not be used normally
        self.total_repair=0
        self.current_repair=0

    
    def GetRepair(self):
        #returns in integer %
        if not hasattr(self,"current_repair"):
            self.current_repair=self.total_repair
        out_of=100
        ret_val=float(self.current_repair*out_of)/self.total_repair
        ret_val=int(round(ret_val,0))
        return ret_val

    def Use(self,times=1):
        if not hasattr(self,"current_repair"):
            self.current_repair=self.total_repair
        self.current_repair-=times
        if self.current_repair<0:
            self.current_repair=0

    def RepairOk(self):
        if not hasattr(self,"current_repair"):
            self.current_repair=self.total_repair
        return self.current_repair>0

    def Mend(self, amount=1):
        if not hasattr(self,"current_repair"):
            self.current_repair=self.total_repair
        
        if self.current_repair<self.total_repair:
            self.current_repair+=amount
            return 1
        return 0

    def FullRepair(self):
        if not hasattr(self,"current_repair"):
            self.current_repair=self.total_repair

        return self.current_repair==self.total_repair

    def RepairAll(self):
        self.current_repair=self.total_repair
