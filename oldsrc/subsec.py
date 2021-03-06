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

# 
# Run subsec.py -h for usage
#

#
# Things to do:
#
# - Add capability to define 'core', 'settled', 'frontier' and 'wild' worlds with definitions 


import argparse
import random
import TR_CE_EXT_MTB
import TR_CE_SRD_World
import TR_Subsector
import sys

# Define common functions

# Dice rollers

def D100Roll():
    random.seed()
    return random.randint(1, 6) + random.randint(1, 101)

DENSITY_LOOKUP = {1: 4, 2: 18, 3: 33, 4: 50, 5: 66}

# Construct and parse command line arguments

parser = argparse.ArgumentParser(description='Generate a CE subsector', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('name', help = 'Enter the name of the subsector to be generated')
parser.add_argument('-d', '--density', type=int, choices=[1, 2, 3, 4, 5], default=3, help='density value (1 = rift, 2 = sparse, 3 = scattered, 4 = standard, 5 = dense).', metavar='DENSITY')
parser.add_argument('-e', '--engine', choices=['CE', 'CEEX', 'CT'], default='CE', help='Generation engine (CE = Cepheus Engine SRS no mods, CEEX Cepheus Engine with Extensions, CT Classic Traveller)', metavar='TYPE')
parser.add_argument('-p', '--parent', default = '', help = 'The name of the parent sector (omit for no parent)')
parser.add_argument('-l', '--letter', default = '', help = 'The subsector position letter (omit for no position')
parser.add_argument('-s', '--settled', type=int, default = 3, choices=[0, 1, 2, 3, 4, 5], help='settlement value (0 = unsettled, 1 = wilds, 2 = frontier, 3 = standard, 4 = high, 5 = very high')

args = parser.parse_args()

print()
print(args)
print()

# Instantiate the subsector and generate

s = TR_Subsector.Subsector(args.engine, args.name, args.parent, args.letter, args.density, args.settled)

# Break out if unimplemented types are requested

if args.engine in ['CT']:
    print("Type not yet implemented - coming soon")
    sys.exit()

# Generate the subsector

s.genSubSec()

# Print the subsector

s.printSubSec()
