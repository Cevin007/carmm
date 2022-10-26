# General structure of the filter class - they should:
# - Iterate through a given ConfigSpace object
# - Find energies
# - Have some criteria to accept or reject a given structure
# - Return a list of energies of the accepted guesses - IN THE ORDER OF THE
# GIVEN CONFIGSPACE VECTOR.

class EMT_filter():