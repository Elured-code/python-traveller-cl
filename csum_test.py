import pytest
from TR_CSUM_Sector import stellarHex

@pytest.fixture
def occupied_hex():
    ''' Returns a stellarHex object with System Presence set to True'''
    return stellarHex(True)

def test_checkObjectPresent(occupied_hex):
     assert occupied_hex.objectPresent == True

def test_determineObjectType(occupied_hex):
    occupied_hex.determineObjectType()

    expected = ["Star", "Brown Dwarf", "Rogue Planet", "Rogue Gas Giant", "Neutron Star", "Nebula", "Black Hole"]

    assert occupied_hex.objectType[0] in expected