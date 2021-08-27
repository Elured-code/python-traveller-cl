import pytest
from TR_CSUM_Sector import stellarHex

@pytest.fixture
def my_stellarHex():
    ''' returns a hex with no contents'''
    return stellarHex()

@pytest.mark.parametrize("systemPresence", [
    (False),
    (True),
    ])

def test_systemPresence(systemPresence):
    my_stellarHex = stellarHex(systemPresence)
    assert my_stellarHex.objectPresent == systemPresence





