import random
import TR_Constants
import TR_Support


class stellarHex:

    def __init__(self, *args):
        if not args: self.objectPresent = False
        else: self.objectPresent = args[0]
        self.objectType = []
      
    
    def checkObjectPresent(self, subsectorType):
        if subsectorType in TR_Constants.CSUM_DENSITY_MAP:
            x = TR_Support.D100Roll()
            y = TR_Constants.CSUM_DENSITY_MAP[subsectorType]
            if x <= y: self.objectPresent = True
            else: self.objectPresent = False

    def determineObjectType(self):
        x = TR_Support.D100Roll()
        if x <= 80: self.objectType.append("Star")
        elif x <= 88: self.objectType.append("Brown Dwarf")
        elif x <= 94: self.objectType.append("Rogue Planet")
        elif x <= 97: self.objectType.append("Rogue Gas Giant")
        elif x <= 98: self.objectType.append("Neutron Star")
        elif x <= 99: self.objectType.append("Nebula")
        else: self.objectType.append("Black Hole")

            

my_stellarHex = stellarHex(True)
my_stellarHex.determineObjectType()

print("end")
# thisHex = stellarHex(False)

# print(thisHex.checkSystemPresence("SCATTERED"))


