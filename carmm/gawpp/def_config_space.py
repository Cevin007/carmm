# How best to structure and define the configuration space - within the Gawpp class or outside?

# For now, let's just test out the factory functionality for a config space -
# it will always have i) the structure, ii) some form of variable to iterate
# over and iii) some scope to cover

# A config space object should be defined within the Gawpp object, and
# should be an ordered, compact representation of the

class ConfigSpace():

    # Should define:
    # - The objects used to generate the total configuration space
    # - Combine the configuration objects to create the full number of configurations
    # - Be wrappable (ie., extendable to new configuration space methods for specific
    # scenarios.
    # - Partition configurations into accepted and non-accepted configurations.
    # - Stores the energy of a given configuration.
    # - Configurations should be permutable - they can be applied in any order.
    # - The application of filters should necessarily eliminate certain
    # structures from subsequent filter applcations.

class AngleConfigSpace():

    # Should define:
    # a) what is being rotated (and the connectivity of atoms it is being rotated around),
    # b) the scope of the property (between which angles and at what intervals)
    # c) the method used to rotate to obtain the structure
    # d) a descriptive string of the property

class PositionConfigSpace():

    # Should define:
    # a) the object being moved
    # b) the scope (which positions are available)
    # c) the translation method (how it is moved to create the new structure)
    # d) a descriptive string of the property

class SpeciesConfigSpace():

    # Should define:
    # a) the target atoms being interchanged
    # b) the scope (the number and possible positions for the species to be interchanged into)
    # c) the interchange method (how the species is replaced)
    # d) a descriptive string of the property
