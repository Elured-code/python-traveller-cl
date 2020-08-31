#
# Cepheus Engine SRD with Extensions Subsector Generation
#
# Version:  0.2
# Author:   Michael Bailey
# Date:     23 July 2020
#

#
# This code generates an 8 x 10 subsector according to:
# 1. CE SRD system generation rules; and
# 2. Stellar data generation kludged together by myself with some quickly researched type/spectra
#    distribution
#

# Constructor:  Subsector(str sName, str SecName, char subLetter, int subDensity)
#   engName:    Generation engine name - currently CE (CE SRD) or CEEX (CE Extended)
#   sName:      Subsector name
#   secName:    Host Sector name
#   subLetter:  Subsector position designator
#   subDensity: Subsector stellar density value
#
# Public methods:
# 
#   PrintSubsector:      output the subsector data to the console
#



#
# Things to do:
#
# - Add capability to define 'core', 'settled', 'frontier' and 'wild' worlds with definitions 


import random
import TR_CE_EXT_MTB
import TR_CE_SRD_World
import TR_CE_Extended
import TR_Support
import TR_Constants
import sys

# Define local constants

ENGINES = ['CT', 'CE', 'CEEX']
# DENSITY_LOOKUP = {1: 4, 2: 18, 3: 33, 4: 50, 5: 66}
SUBSECLETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
FIXEDHEADER = ''' 1-13: Name
15-18: HexNbr
20-28: UWP
   31: Bases
33-47: Codes & Comments
   49: Zone
52-54: PBG
56-57: Allegiance
59-74: Stellar Data

....+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8'''

# Define common functions



class Subsector:

    # Define properties

    @property
    def engName(self):
        return self.__engName
    
    @property
    def pType(self):
        return self.__pType
    
    @property
    def subName(self):
        return self.__subName

    @property
    def secName(self):
        return self.__secName

    @property
    def subLetter(self):
        return self.__subLetter

    @property
    def subDensity(self):
        return self.__subDensity

    @property
    def subContents(self):
        return self.__subContents

    @property
    def sumPop(self):
        return self.__sumPop

    @property
    def hiTL(self):
        return self.__hiTL

    @property
    def hiPop(self):
        return self.__hiPop

    # Define setters

    @engName.setter
    def engName(self, engName):
        if engName in ENGINES: self.__engName = engName
        else: self.engName = 'CE'

    @pType.setter
    def pType(self, pType):
        if pType in [*range(0, 6, 1)]: self.__pType = pType
        else: self.__pType = 3
    
    @subName.setter
    def subName(self, subName):
        self.__subName = subName

    @secName.setter
    def secName(self, secName):
        self.__secName = secName

    @subLetter.setter
    def subLetter(self, subLetter):
        if subLetter in SUBSECLETTERS: self.__subLetter = subLetter
        else: self.__subLetter = ' '

    @subDensity.setter
    def subDensity(self, subDensity):
        if subDensity in [1, 2, 3, 4, 5]: self.__subDensity = subDensity
        else: self.__subDensity = 3

    @subContents.setter
    def subContents(self, subContents):
        self.__subContents = subContents

    @sumPop.setter
    def sumPop(self, sumPop):
        self.__sumPop = sumPop

    @hiTL.setter
    def hiTL(self, hiTL):
        if hiTL < 0: self.__hiTL = 0
        else: self.__hiTL = hiTL

    @hiPop.setter
    def hiPop(self, hiPop):
        if hiPop < 0: self.__hiPop = 0
        else: self.__hiPop = hiPop



    # Initialise the Subsector object

    def __init__(self, engName, subName, secName, subLetter, subDensity, pType):
        self.__pType = pType
        self.engName = engName
        self.__subName = subName
        self.__secName = secName
        self.__subLetter = subLetter
        self.__subDensity = subDensity
        self.contents = []
        self.hiTL = 0
        self.sumPop = 0
        self.hiPop = 0

    # Clear the subsector object

    def clear(self):
        self.contents = []
    
    # Generate the subsector

    def genSubSec(self):

    # Set the probability of system presence in any given hex

        prob = TR_Constants.DENSITY_LOOKUP.get(self.subDensity)
        
        # Loop through the subsector hexes, checking for and if required generating mainworlds
        i = 1
        while i <= 8:
            j = 1
            while j <= 10:   
                if TR_Support.D100Roll() < prob:
                    loc = format(i, '02d') + format(j, '02d')
                    isMainWorld = True
                    
                    # Generate the world using ht eengine specified
                    
                    if self.engName == 'CEEX': w1 = TR_CE_Extended.System("Main-" + loc, isMainWorld, self.pType)
                    elif self.engName == 'CE': w1 = TR_CE_SRD_World.World("Main-" + loc)
                    w1.loc = loc
                    w1.genWorld(loc)
                    
                    # Add the world to the subsector contents

                    self.contents.append(w1)


                j += 1
            i += 1

    # Print a subsector to stdout

    def printSubSec(self):

        # Print the header text

        print(self.subName + " " + "(" + self.secName + "/" + self.subLetter + ")")
        print(FIXEDHEADER)

        for World in self.contents:
            World.formatUWPString_text_SEC()
            print(World.UWPString)

    # Write a subsector to a variable

    def writeSubSec(self):
        returnval = ''
        returnval += self.subName + " " + "(" + self.secName + "/" + self.subLetter + ")" + '\n'
        returnval += FIXEDHEADER + '\n'
    
        for World in self.contents:
            World.formatUWPString_text_SEC()
            returnval += World.UWPString
            returnval += '\n'

        return returnval


# # Testing code here

# s1 = Subsector("CE", "TestSub", "TestSec", "B", 3, 5)

# # print(s1.pType)
# s1.genSubSec()
# print("```")
# s1.printSubSec()
# print("```")