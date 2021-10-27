from os import popen
from _pytest.python_api import ApproxMapping

import pytest
from itertools import product, permutations
from src.utils.TR_Constants import HYDTLMOD, STARPORTS
from src.TR_CE_MainWorld import World
from src.utils.TR_Support import D6Rollx2


SIZ_LIST = list(range(0, 11))
ATM_LIST = list(range(0, 16))
HYD_LIST = list(range(0, 11))
POP_LIST = list(range(0, 13))
GOV_LIST = list(range(0, 16))
LAW_LIST = list(range(0, 16))
TLV_LIST = list(range(0, 24))

D6ROLLS = [1, 2, 3, 4, 5, 6]
D6X2ROLLS = list(range(2, 13))
TWOD6X2ROLLS = product(list(range(2, 13)), list(range(2, 13)))
EXOTIC_ATM = list(range(10, 16))
BASES = [' ', 'A', 'N', 'G', 'P', 'S']


@pytest.fixture
def new_World():
    ''' Returns a newly initialised World object '''
    return World('Test')

''' Test atmosphere for siz = 0 '''
@pytest.mark.parametrize("roll1", D6X2ROLLS)
def test_gen_atm_siz0(new_World, roll1):
    new_World.siz = 0
    new_World.gen_atm(roll1)
    assert new_World.atm == 0

''' Test hydro for siz = 0 '''
@pytest.mark.parametrize("roll1", D6X2ROLLS)
@pytest.mark.parametrize("roll2", D6X2ROLLS)
def test_gen_hyd_siz0(new_World, roll1, roll2):
    new_World.siz = 0
    new_World.gen_atm(roll1)
    new_World.gen_hyd(roll2)
    assert new_World.hyd == 0

''' Test atmosphere for siz = A '''
@pytest.mark.parametrize("roll1", D6X2ROLLS)
def test_gen_atm_sizA(new_World, roll1):
    expect = ATM_LIST
    new_World.siz = 10
    new_World.gen_atm(roll1)
    assert new_World.atm in ATM_LIST

''' Test hydro for siz = A '''
@pytest.mark.parametrize("roll1", D6X2ROLLS)
@pytest.mark.parametrize("roll2", D6X2ROLLS)
def test_gen_hyd_sizA(new_World, roll1, roll2):
    expect = HYD_LIST
    new_World.siz = 10
    new_World.gen_atm(roll1)
    new_World.gen_hyd(roll2)
    assert new_World.hyd in expect

''' Test hydro for exotic atmospheres and size A '''
@pytest.mark.parametrize("atm", EXOTIC_ATM)
@pytest.mark.parametrize("roll1", D6X2ROLLS)
def test_gen_hyd_exoticatm_sizA(new_World, atm, roll1):
    expect = HYD_LIST
    new_World.siz = 10
    new_World.atm = atm
    new_World.gen_hyd(roll1)
    assert new_World.hyd in expect

''' Test pop for acceptable values '''
''' At this point unit testing for all possible combinations isn't feasible, so '''
''' I've used some sample values '''

@pytest.mark.parametrize("siz", [0, 10])
@pytest.mark.parametrize("atm", [0, 15])
@pytest.mark.parametrize("hyd", [0, 10])
@pytest.mark.parametrize("roll1", [2, 12])
def test_gen_pop(new_World, siz, atm, hyd, roll1):
    expect = POP_LIST
    new_World.siz = siz
    new_World.atm = atm
    new_World.hyd = hyd
    new_World.gen_pop(roll1)
    assert new_World.pop in POP_LIST

''' Test pMod for acceptable values'''
@pytest.mark.parametrize("roll", D6X2ROLLS)
@pytest.mark.parametrize("pop", list(range(1, 13)))
def test_gen_pMod(new_World, roll, pop):
    expect = list(range(1, 10))
    new_World.pop = pop
    new_World.gen_pMod(roll)
    assert new_World.pMod in expect

@pytest.mark.parametrize("roll", D6X2ROLLS)
def test_gen_pMod_pop0(new_World, roll):
    new_World.pop = 0
    new_World.gen_pMod(roll)
    assert new_World.pMod == 0


''' Test gov for acceptable values '''
@pytest.mark.parametrize("pop", POP_LIST)
@pytest.mark.parametrize("roll1", D6X2ROLLS)
def test_gen_gov(new_World, pop, roll1):
    expect = GOV_LIST
    new_World.pop = pop
    new_World.gen_gov(roll1)
    assert new_World.gov in expect

''' Test gov for pop = 0 '''
@pytest.mark.parametrize("roll1", D6X2ROLLS)
def test_gen_gov_pop0(new_World, roll1):
    new_World.pop = 0
    new_World.gen_gov(roll1)
    assert new_World.gov == 0

''' Test law for acceptable values'''
@pytest.mark.parametrize("gov", GOV_LIST)
@pytest.mark.parametrize("roll1", D6X2ROLLS)
def test_gen_law(new_World, gov, roll1):
    expect = LAW_LIST
    new_World.gov = gov
    new_World.gen_law(roll1)
    assert new_World.law in expect

''' Test law for gov = 0 '''
@pytest.mark.parametrize("roll1", D6X2ROLLS)
def test_gen_law_gov0(new_World, roll1):
    new_World.gov = 0
    new_World.gen_law(roll1)
    assert new_World.law == 0

''' Test starports for acceptable values '''
@pytest.mark.parametrize("pop", POP_LIST)
@pytest.mark.parametrize("roll1", D6X2ROLLS)
def test_gen_starPort(new_World, pop, roll1):
    new_World.pop = pop
    new_World.gen_starPort(roll1)
    assert new_World.starPort in STARPORTS

''' Test TL for acceptable values '''
@pytest.mark.parametrize("starPort", STARPORTS)
@pytest.mark.parametrize("siz", [0, 10])
@pytest.mark.parametrize("atm", [0, 15])
@pytest.mark.parametrize("pop", [0, 10, 11, 12])
@pytest.mark.parametrize("gov", [0, 7, 15])
@pytest.mark.parametrize("roll1", D6ROLLS)
def test_gen_TL(new_World, starPort, siz, atm, pop, gov, roll1):
    expect = TLV_LIST
    new_World.siz = siz
    new_World.atm = atm
    new_World.pop = pop
    new_World.giv = gov
    new_World.starPort = starPort
    new_World.gen_tlv(roll1)
    assert new_World.tlv in expect

''' Test bases for acceptable values '''
@pytest.mark.parametrize("starport", STARPORTS)
@pytest.mark.parametrize("roll1", [2, 12])
@pytest.mark.parametrize("roll2", [2, 12])
@pytest.mark.parametrize("roll3", [2, 12])
def test_bases(new_World, starport, roll1, roll2, roll3):
    expect = BASES
    new_World.gen_bases(roll1, roll2, roll3)
    assert new_World.bases in expect

''' Test belt generation for acceptable values '''
@pytest.mark.parametrize("roll1", D6X2ROLLS)
@pytest.mark.parametrize("roll2", D6ROLLS)
def test_belts(new_World, roll1, roll2):
    expect = range(0, 4)
    new_World.gen_nbelts(roll1, roll2)
    assert new_World.nbelts in expect

''' Test gas giant generation for acceptable values '''
@pytest.mark.parametrize("roll1", D6X2ROLLS)
@pytest.mark.parametrize("roll2", D6ROLLS)
def test_giants(new_World, roll1, roll2):
    expect = range(0, 5)
    new_World.gen_ngiants(roll1, roll2)
    assert new_World.ngiants in expect