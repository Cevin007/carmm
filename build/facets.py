#TODO: How about we change facets to "highest_index_facet", and it just generates all possible facets up to this number?
# I would prefer it as a list of facets, so that we can generate just one face if thats the requirement.
# I'm also going to change this so it doesn't write by default, as I'd prefer it to return an object
def generate(bulk_model, layers=2, facets=[(1,1,1)], supercell =(1,1,1), vacuum=10, save=False):
	'''
	Function to create variety of different facets

	Parameters:

	bulk_model: Atoms object or string
		specify the unit cell of the bulk geometry.
	layers: int
		specify the repeating layers along the direction defined in 'axis' of the 'center' function
	facets: list of array of ints
		specify the list of facets required as output
	supercell: array of ints
		specify the periodicity of the supercell; (x,y,z).   # can this just be an int?  - No, has to be an array #
	vacuum: float
		specifies the vacuum addition to the slab in the direction of 'axis-' of the 'center' function

	'''

	from ase.build import surface

	#input bulk geometry
	#if string, check if atomic label, in which case we don't read from file
	if isinstance(bulk_model, str) and len(bulk_model) > 2:
		from ase.io import read
		bulk_model = read(bulk_model)

	slabs = []
	#loop for all surfaces
	for face in facets:
		# cut the slab in face, last number is the number of layers
		slab = surface(bulk_model,(face),layers)
		# create a supercell and make it periodic as specified in the input
		slab.repeat(supercell)
		# introduce vaccum around the supercell in z direction
		slab.center(vacuum=vacuum, axis=2)
		# Add model to the list of slabs
		slabs.append(slab)

	# Now writes all files at the end
	if save:
		_save(facets, slabs)

	return facets, slabs

def _save(facets, models):
	'''
	Method to write all structures to file; hidden from user

	Parameters:

	facets: list of array of ints
		List of facets required as output
	slabs: list of atom objects
		Auxiliary variable used for performing operations on each face of the facets 

	'''

	from ase.io import write

	for i in range(len(facets)):
		face = facets[i]
		write(str(face[0])+str(face[1])+str(face[2])+'.in', models[i])

def create_supercell(atoms, repeat_a, repeat_b, repeat_c=1):
	'''
	Method to convert and return any atoms object into a supercell

	Parameters:

	Atoms: Atoms object
		Incoming structure
	repeat_a: Integer
		Extension in x-direction
	repeat_b: Integer
		Extension in y-direction
	repeat_c: Integer
		Extension in z-direction
	'''

	return atoms*(repeat_a, repeat_b, repeat_c)