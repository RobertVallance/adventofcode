
# array to hod the expense values
expenses = []

# read in the expenses file
file_2020 = open('day1_2020.txt', 'r')

for line in file_2020:
	expenses.append(int(line))


### PART 1

# iterate over pairs of values in expenses list to find the ones that sum to 2020
for i in range(0, len(expenses)):

	for j in range(i+1, len(expenses)):

		# if a pair sums to 2020, multiply their values
		if (expenses[i] + expenses[j] == 2020):
			print(expenses[i]*expenses[j])


### PART 2

# iterate triplets pairs of values in expenses list to find the ones that sum to 2020
for i in range(0, len(expenses)):

	for j in range(i+1, len(expenses)):

		for k in range(j+1, len(expenses)):

			# if a triplet sums to 2020, multiply their values
			if (expenses[i] + expenses[j] + expenses[k] == 2020):
				print(expenses[i]*expenses[j]*expenses[k])