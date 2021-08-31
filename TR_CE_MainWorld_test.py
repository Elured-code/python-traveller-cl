import pytest
from itertools import product, permutations
from TR_CE_MainWorld import World
from TR_Support import D6Rollx2

D6X2ROLLS = list(range(2, 13))
SIZ_LIST = list(range(0, 11))
ATM_LIST = list(range(0, 16))

TWOD6X2ROLLS = list(product(range(2, 13), range(2, 13)))
THREED6X2ROLLS = list(product(range(2, 13), range(2, 13), range(2, 13)))



@pytest.fixture
def new_World():
    ''' Returns a newly initialised World object '''
    return World('Test')


''' Test world generation - size for acceptable value '''
@pytest.mark.parametrize("rolls", D6X2ROLLS)
def test_gen_siz(new_World, rolls):
    expected = SIZ_LIST
    new_World.gen_siz(rolls)
    assert new_World.siz in expected

''' Test atmosphere for acceptable value for all size values'''
@pytest.mark.parametrize("roll1, roll2", TWOD6X2ROLLS)
def test_gen_atm(new_World, roll1, roll2):
    expected = ATM_LIST
    new_World.gen_siz(roll1)
    new_World.gen_atm(roll2)
    assert new_World.atm in expected

''' Test atmosphere for siz = 0 '''
@pytest.mark.parametrize("rolls", D6X2ROLLS)
def test_gen_atm_siz0(new_World, rolls):
    new_World.siz = 0
    new_World.gen_atm(rolls)
    assert new_World.atm == 0


