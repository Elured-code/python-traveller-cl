import random
import TR_Constants
import TR_Support


# Determine the type of object present, returning a string value for the object type

def determineObjectType():
    x = TR_Support.D100Roll()
    if x <= 80: thisType = "Star"
    elif x <= 88: thisType =  "Brown Dwarf"
    elif x <= 94: thisType = "Rogue Planet"
    elif x <= 97: thisType = "Rogue Gas Giant"
    elif x <= 98: thisType = "Neutron Star"
    elif x <= 99: thisType = "Nebula"
    else: thisType = "Black Hole" 
    return thisType  


def determineBrownDwarfType(roll: int):
    if roll <= 50: returnVal = "L"
    elif roll <= 75: returnVal = "T"
    else: returnVal = "Y"

    return returnVal

def determineStarType(realismType: int, roll: int):
    if realismType == TR_Constants.SC_REAL:
        if roll <= 80: thisClass = "M"
        elif roll <= 88: thisClass = "K"
        elif roll <= 94: thisClass = "G"
        elif roll <= 97: thisClass = "F"
        elif roll <= 98: thisClass = "A"
        elif roll <= 99: thisClass = "B"
        else: thisClass = "O"      

    if realismType == TR_Constants.SC_SEMIREAL:
        if roll <= 50: thisClass = "M"
        elif roll <= 77: thisClass = "K"
        elif roll <= 90: thisClass = "G"
        elif roll <= 97: thisClass = "F"
        elif roll <= 98: thisClass = "A"
        elif roll <= 99: thisClass = "B"
        else: thisClass = "O" 

    if realismType == TR_Constants.SC_FANTASTIC:
        if roll <= 25: thisClass = "M"
        elif roll <= 50: thisClass = "K"
        elif roll <= 75: thisClass = "G"
        elif roll <= 97: thisClass = "F"
        elif roll <= 98: thisClass = "A"
        elif roll <= 99: thisClass = "B"
        else: thisClass = "O"

    return thisClass

### stellarHex class - properties and methods for a hexes contents, including stars and worlds
#
#

class stellarHex:

# Getters

    @property
    def starRealism(self):
        return self.__starRealism

# Setters

    @starRealism.setter
    def starRealism(self, starRealism):

        # Reset non supported values to 1

        if starRealism not in [1, 2, 3]: starRealism = 1
        self.__starRealism = starRealism

        

    def __init__(self, *args):
        if not args: self.objectPresent = False
        else: self.objectPresent = args[0]
        self.objectType = []
        self.starRealism = TR_Constants.SC_REAL
      
# Check for object presence in the hex

    def checkObjectPresent(self, subsectorType):
        if subsectorType in TR_Constants.CSUM_DENSITY_MAP:
            x = TR_Support.D100Roll()
            y = TR_Constants.CSUM_DENSITY_MAP[subsectorType]
            if x <= y: self.objectPresent = True
            else: self.objectPresent = False
     
    def determineObjectDetails(self):

        # Only determine details if there is something in the hex

        if self.objectPresent:

            objDetails = {}

            # Determine the object type

            objDetails['Type'] = determineObjectType()

            # Determine the object stellar class

            if objDetails['Type'] == "Star": objDetails['Stellar Class'] = determineStarType(self.starRealism, TR_Support.D100Roll())
            if objDetails['Type'] == "Brown Dwarf": objDetails['Stellar Class'] = determineBrownDwarfType(TR_Support.D100Roll())

            # Finally, add the information to the objectType list

            self.objectType.append(objDetails)


            
 
        

 

my_stellarHex = stellarHex(True)
my_stellarHex.determineObjectDetails()

print(my_stellarHex.objectType)
print("end")
# thisHex = stellarHex(False)

# print(thisHex.checkSystemPresence("SCATTERED"))


