import random
from src.utils import TR_Constants
from src.utils import TR_Support


# Determine the type of object present, returning a string value for the object type

def determineobjects():
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
        self.objects = []
        self.objects.append({})
        self.starRealism = TR_Constants.SC_REAL
      
# Check for object presence in the hex

    def checkObjectPresent(self, subsectorType):
        if subsectorType in TR_Constants.CSUM_DENSITY_MAP:
            x = TR_Support.D100Roll()
            y = TR_Constants.CSUM_DENSITY_MAP[subsectorType]
            
            # If there is an object present then set flag to true and initialise the objects list
            
            if x <= y: 
                self.objectPresent = True
                
            else: self.objectPresent = False
     
    
    def determineObjectType(self, objectNumber):

        # Only determine details if there is something in the hex

        if self.objectPresent:
          
            # Determine the object type

            oType = determineobjects()

            # Add the information to the objects list

            self.objects[objectNumber]['Type'] = oType
    
    def determineStarClass(self, objectNumber):

        # Only determine details if there is something in the hex

        if self.objectPresent:

            sClass = ""

            # Determine the object stellar class

            if self.objects[objectNumber]['Type'] == "Star": sClass = determineStarType(self.starRealism, TR_Support.D100Roll())
            if self.objects[objectNumber]['Type'] == "Brown Dwarf": sClass = determineBrownDwarfType(TR_Support.D100Roll())

            # Finally, add the information to the objects list

            self.objects[objectNumber]['Stellar Class'] = sClass




            
 
        

 

my_stellarHex = stellarHex(True)
my_stellarHex.checkObjectPresent("DISPERSED")
my_stellarHex.determineObjectType(0)
my_stellarHex.determineStarClass(0)

print(my_stellarHex.objects)
print("end")
# thisHex = stellarHex(False)

# print(thisHex.checkSystemPresence("SCATTERED"))


