# read in passwords file

file_passwords = open('day2_passwords.txt', 'r')

valid_passwords_count_part_1 = 0
valid_passwords_count_part_2 = 0

for line in file_passwords:

	# split each line in file so space char is used as a boundary
	split_line = line.split()

	# upper and lower policy bounds are first element in split_line and either side of the hyphen
	policy_lower_bound = int(split_line[0].split('-')[0])
	policy_upper_bound = int(split_line[0].split('-')[1])

	# policy character is second element in split_line (removing the colon)
	policy_char = split_line[1].replace(':', '')

	# password is third and final element in split_line
	password = split_line[2]

	print(policy_lower_bound, policy_upper_bound, policy_char, password)

	### PART 1

	# check if the policy character count abides by the upper and lower policy bounds
	policy_char_count = password.count(policy_char)

	if (policy_char_count >= policy_lower_bound) and (policy_char_count <= policy_upper_bound):
		valid_passwords_count_part_1 += 1
		#print('OK')


	### PART 2

	# policy bounds are now character positions.
	# exactly one of these positions must contain the given letter

	if ((password[policy_lower_bound-1] == policy_char) and (password[policy_upper_bound-1] != policy_char)) \
		or ((password[policy_lower_bound-1] != policy_char) and (password[policy_upper_bound-1] == policy_char)):
		valid_passwords_count_part_2 += 1
		#print('OK')





print('PART 1', valid_passwords_count_part_1)
print('PART 2', valid_passwords_count_part_2)

