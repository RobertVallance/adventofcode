
def loop_through_inner_bags(i, bag_file, contained_bags):

	print(contained_bags)

	for x, contained_bag in enumerate(contained_bags):

		contained_bag_name = ' '.join(contained_bag.split()[1:3])
		print(contained_bag_name)

		for j, line_j in enumerate(bag_file):

			# ignore line we are aleady on - want to see if other lines have this bag as principal bag
			if i == j:
				continue

			else:

				# principal bag defined by first two words in line
				principal_bag  = ' '.join(line_j.split()[:2])

				if contained_bag_name == principal_bag:

					contained_bag_dict = {}
					contained_bag_dict[contained_bags[x]] = ' '.join(line_j.split()[4:])
					contained_bags[x] = contained_bag_dict


	print(contained_bags)
	return contained_bags





# dictionary to hold bag colours
bag_colours_dict = {}

# open bag file and loop over lines, appending bag colours to dictionary
bag_file = open('day7_bagcolours.txt', 'r')

for i, line_i in enumerate(bag_file):

	# principal bag defined by first two words in line
	principal_bag  = ' '.join(line_i.split()[:2])

	# contained bags defined fourth word onwards in line (and remove final full stop on line)
	contained_bags = ' '.join(line_i.split()[4:])
	contained_bags = contained_bags.replace('.', '')

	# separate the contained bags split by comma
	contained_bags = contained_bags.split(', ')

	contained_bags = loop_through_inner_bags(i, bag_file, contained_bags)

	# create key-value pairs for principal bag as key, contained bags as value
	bag_colours_dict[principal_bag] = contained_bags



		



for key, value in bag_colours_dict.items():
	print(key, value)

