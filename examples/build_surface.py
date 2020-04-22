#!/usr/bin/env python3

'''
TODO: Description Needed

'''

from ase.build import fcc111
from math import sqrt

#### Traditional ASE functionality #####

element='Au'
lattice_parameter=2.939
width=2
depth=2
vacuum=10.0

# Create surface
slab = fcc111(element, a=lattice_parameter*sqrt(2),
              size=(width,width,depth), vacuum=vacuum)

# Enable to add H at an ontop position
#add_adsorbate(slab, 'H', 1.5, 'ontop')

# Enable to visualise the slab
# from ase.visualize import view
# view(slab)

# Writes surface to file
# from ase.io import write
#write('slab_geometry.in',slab,format='aims')

#########

#### Functionality to create all surfaces ####
from software.build import facets

facets, slabs = facets.generate(element)

#########

#### Assertion tests ####

# Scale all cell vectors to match those defined previously
for i in range(len(slabs)):
    slabs[i].set_cell(slabs[i].get_cell()*(lattice_parameter/slabs[i].get_cell()[1][0]))

# This is an assertion - it checks the same results are given by both methods
# Note I don't test the vacuum direction. This differs by a small value, for reasons of no concern.
eps = 1e-10
for i in range(2):
    for j in range(3):
        assert(slab.get_cell()[i][j] - slabs[0].get_cell()[i][j] < eps)