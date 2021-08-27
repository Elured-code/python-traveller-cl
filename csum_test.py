import pytest
from TR_CSUM_Sector import stellarHex

def test_checkObjectPresent():
    hex = stellarHex()
    assert hex.objectPresent == False

def test_determineObjectType():
    hex = stellarHex()
    hex.determineObjectType()

    expected = ["Star", "Brown Dwarf", "Rogue Planet", "Rogue Gas Giant", "Neutron Star", "Nebula", "Black Hole"]

    assert hex.objectType[0] in expected