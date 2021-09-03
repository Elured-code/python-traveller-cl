import random

# import TR_Constants
# from TR_Support import D6Roll, D6Rollx2, D100Roll

import TR_Constants
from TR_Support import D6Roll, D6Rollx2, D100Roll, D6Rollx3



# World class - holds the world details as defined in the CE SRD
#

class World:

# Define properties

    @property
    def worldname(self):
        return self.__worldname

    @property
    def siz(self):
        return self.__siz
    @property
    def atm(self):
        return self.__atm

    @property
    def hyd(self):
        return self.__hyd

    @property
    def pop(self):
        return self.__pop

    @property
    def gov(self):
        return self.__gov

    @property
    def law(self):
        return self.__law

    @property
    def tlv(self):
        return self.__tlv

    @property
    def starPort(self):
        return self.__starPort

        
# Define setters, including checks

    @worldname.setter
    def worldname(self, worldname):
        # if len(worldname) > 13:
        #     self.__worldname = worldname[0:13]
        self.__worldname = worldname

    @siz.setter
    def siz(self, siz):
        if siz < 0: self.__siz = 0
        elif siz > 10: self.__siz = 10
        else: self.__siz = siz

    @atm.setter
    def atm(self, atm):
        if atm < 0: self.__atm = 0
        elif atm > 15: self.__atm = 15
        else: self.__atm = atm

    @hyd.setter
    def hyd(self, hyd):
        if hyd < 0: self.__hyd = 0
        elif hyd > 10: self.__hyd = 10
        else: self.__hyd = hyd

    @pop.setter
    def pop(self, pop):
        if pop < 0: self.__pop = 0
        elif pop > 10: self.__pop = 10
        else: self.__pop = pop

    @gov.setter
    def gov(self, gov):
        if gov < 0: self.__gov = 0
        elif gov > 15: self.__gov = 15
        else: self.__gov = gov

    @law.setter
    def law(self, law):
        if law < 0: self.__law = 0
        elif law > 15: self.__law = 15
        else: self.__law = law

    @tlv.setter
    def tlv(self, tlv):
        if tlv < 0: self.__tlv = 0
        else: self.__tlv = tlv
    
    @starPort.setter
    def starPort(self, starPort):
        if starPort in TR_Constants.STARPORTS:
            self.__starPort = starPort
        else: self.__starPort = "-"

# Initialise the world class        

    def __init__(self, wName):
        
        # Initialise variables

        self.worldname = wName
        self.siz = 0
        self.atm = 0
        self.hyd = 0
        self.pop = 0
        self.gov = 0
        self.law = 0
        self.starPort = 'X'
        self.tlv = 0
    
# Methods to randmomly generate mainworld properties

    def gen_siz(self, roll):
        x = roll - 2
        self.siz = x

    def gen_atm(self, roll):
        x = roll + self.siz - 7
        if x < 0: x = 0
        elif x > 15: x = 15
        if self.siz == 0: x = 0
        self.atm = x
    
    def gen_hyd(self, roll):
        x = roll + self.siz - 7

        if self.siz == 0: x = 0
        else:
            if self.atm in [0, 1, 10, 11, 12]: x -= 4
            if self.atm == 14: x -= 2
        if x < 0: x = 0
        self.hyd = x

    def gen_pop(self, roll):
        x = roll - 2
        if self.siz <= 2: x -= 1
        if self.atm in [0, 1, 10, 11, 12]: x -= 2
        if self.atm == 6: x  += 3
        if self.atm in [5, 8]: x += 1
        if self.hyd == 0 and self.atm < 3: x -= 2
        if self.pop < 0: x = 0
        if self.pop > 12: x = 12
        self.pop = x

    def gen_gov(self, roll):
        x = roll - 7 + self.pop
        if self.pop == 0: x = 0
        self.gov = x

    def gen_law(self, roll):
        x = roll - 7 + self.gov
        if self.pop == 0: x = 0
        self.law = x

    def gen_starPort(self, roll):
        spRoll = roll - 7 + self.pop
        self.starPort = TR_Constants.STARPORTSTABLE.get(spRoll)

    def gen_tlv(self, roll):
        if self.starPort in TR_Constants.STARPORTTLMOD: roll += TR_Constants.STARPORTTLMOD.get(self.starPort)
        if self.siz in TR_Constants.SIZETLMOD: roll += TR_Constants.SIZETLMOD.get(self.siz)
        if self.hyd in TR_Constants.HYDTLMOD: roll += TR_Constants.HYDTLMOD.get(self.hyd)
        if self.atm in TR_Constants.ATMTLMOD: roll += TR_Constants.ATMTLMOD.get(self.atm)
        if self.pop in TR_Constants.POPTLMOD: roll += TR_Constants.POPTLMOD.get(self.pop)
        if self.gov in TR_Constants.GOVTLMOD: roll += TR_Constants.GOVTLMOD.get(self.gov)

        # Add CE world condition requirements

        if self.hyd in [0, 10] and self.pop > 6 and roll < 4: roll = 4
        if self.atm in [4, 7, 9] and roll < 5: roll = 5
        if self.atm in [0, 1, 2, 3, 10, 11, 12] and roll < 7: roll = 7
        if self.atm in [13, 14] and self.hyd == 10 and roll < 7: roll = 7

        # Finally, if population is zero, no TL

        if self.pop == 0: roll = 0

        self.tlv = roll       


# Randomly generate a mainworld object

    def genWorld(self):

        # Generate world data

    
        # Generate physical stats

        self.gen_siz(D6Rollx2())
        self.gen_atm(D6Rollx2())
        self.gen_hyd(D6Rollx2())
        self.gen_pop(D6Rollx2())
        self.gen_gov(D6Rollx2())
        self.gen_law(D6Rollx2())
        self.gen_starPort(D6Rollx2())
        self.gen_tlv(D6Roll())
        

w = World('A')
w.genWorld()

print(w.starPort)
print(w.siz)
print(w.atm)
print(w.hyd)
print(w.pop)
print(w.gov)
print(w.law)
print(w.tlv)

