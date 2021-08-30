import pytest
from TR_CSUM_Sector import stellarHex

@pytest.fixture
def occupied_hex():
    ''' Returns a stellarHex object with System Presence set to True'''
    return stellarHex(True)

@pytest.fixture
def bd_primary():
    ''' Returns a stellarHex object with a brown dwarf primary'''
    hex = stellarHex(True)
    hex.objects[0]['Type'] = "Brown Dwarf"
    return hex


def test_checkObjectPresent(occupied_hex):
     assert occupied_hex.objectPresent == True

def test_determineObjectType(occupied_hex):
    occupied_hex.determineObjectType(0)

    expectedType = ["Star", "Brown Dwarf", "Rogue Planet", "Rogue Gas Giant", "Neutron Star", "Nebula", "Black Hole"]

    assert occupied_hex.objects[0]['Type'] in expectedType, "Assertion failed:  object type not expected"

def test_bdClass(bd_primary):
    bd_primary.determineStarClass(0)

    expectedClass = ["L", "T", "Y"]

    assert 'Stellar Class' in bd_primary.objects[0]
    assert bd_primary.objects[0]['Stellar Class'] in expectedClass, "Assertion failed:  class not expected"

# def test_objectClass(occupied_hex):
#     occupied_hex.determineStarClass()

#     expectedClass = ["L", "T", "Y", "M", "K", "G", "F", "A", "B", "O"]

#     if 'Class' in occupied_hex.objectType[0]: assert occupied_hex.objectType[0]['Class'] in expectedClass, "Assertion failed:  class not expected"



