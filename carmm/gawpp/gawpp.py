# Generalised Adsorbate Workflow Project Placeholder
# The core Gawpp object accepts the initial arguments from the user.
# For now, we'll take it that the user just wants to find the best
# place to put an adsorbate in an 'optimal' position.
# Therefore, the minimal input should be: 1) The proposed platform site and
# 2) The proposed adsorbate.

# The structure of the Gawpp object should be decided early - overall
# the code is composed of the base structure, the configurational space
# and the applied filters. Should each configurational space be defined
# as its own class, which encompasses its own variable and the desired
# scope which it spans and its associated structures?

# The overall configurational space should be a separate object, or an
# object within Gawpp which is operated on by outside structures.
# These operation (wrapper) functions would then: a) introduce their own
# variables, scopes and structures to a list of possible structures
# within the configurational space, b) iterate over the existing configurational
# space, c) create some readable output to test the number of structures
# which are introduced.

# However, should this mean structures are generated on the fly?
# If a large number of structures are introduced

# The final workflow should look something like this:
#
# from def_config_space import ApplyAngleConfigSpace, ApplyPositionConfigSpace,
# from filters import HardSphereFilter
#
# surface = Atoms(somesurface)
# adsorbate = Atoms(someadsorbate)
#
# Gobj = Gawpp(somesurface, someadsorbate)
# Gobj.add_config_vector(ApplyPositionConfigSpace(Group_to_move,[possible positions])
# Gobj.add_config_vector(ApplyAngleSpace(Group_to_rotate,center_of_rotation,axis_of_rotation,)

# Gobj.apply_filter(HardSphereFilter)

# Gobj.

class Gawpp():

    # Should define:
    # - The initial structure and adsorbate
    # - Define the configuration space and scope.
    # - Include some method to apply new configuration spaces.
    # - Apply necessary filters to reduce configurational space.
    # - Should be able to print out the accepted and non-accepted guesses
    # of configurational space, and pass on to the user any relevant information
    # - Interact with analysis object to print out energy contours of
    # accepted guesses (or simply islands of accepted and non-accepted
    # structures in the case of binary filters.)

    def __init__(self):

        from def_config_space import ConfigSpace

        self.conf_space = ConfigSpace()

    def apply_config_vector(self, METHOD):

        # Some method to apply to conf_space

        return None

