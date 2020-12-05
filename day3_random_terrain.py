import numpy as np

nrows = np.random.randint(10, 50)
ncols = np.random.randint(10, 50)

terrain_array = np.random.rand(nrows, ncols)



#print(nrows, ncols)

terrain_file = open('day3_random_terrain.txt', 'w')

for i in range(nrows):

	for j in range(ncols):

		if terrain_array[i][j] > 0.8:
			terrain_file.write('#')
		else:
			terrain_file.write('.')

	terrain_file.write('\n')


		
