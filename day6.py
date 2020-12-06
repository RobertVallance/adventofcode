

# read in file of customs declaration responses
declarations_file = open('day6_declarations.txt', 'r')
lines = declarations_file.readlines()

# initialise variables
group_responses = []                  # temporary container for all responses of each group member
count_any_member_has_response   = 0   # count for part 1
count_all_members_have_response = 0   # count for part 2


# loop over file
for line in lines:

	# if have a blank line (or at end of file), means we have reached end of 
	# an group's info, so save declaration response info for current group 
	# and reset group_responses list

	if line == '\n' or line == lines[-1]:

		# case where at end of file, want to save that last line
		if line == lines[-1]:
			
			# remove newlines at end of lines and split by whitespace
			line = line.strip()
			group_responses.append(line)
			
		#print(group_responses)

		


		# PART 1
		# for each group, count the number of questions to which ANYONE responded "yes" 
		# what is the sum of those counts?

		# each group member has their responses as one element in group_responses
		# so flatten this so each char of each group member now makes up one element
		group_responses_flattened = [item for sublist in group_responses for item in sublist]

		# there will be duplicates in the flattened array
		# first part wants the total number of UNIQUE elements so convert to set
		group_responses_set = set(group_responses_flattened)
		#print(group_responses_set)

		# count number of unique elements in the set and add this to 
		# the count_any_member_has_response var which keeps track of the total count
		# for all groups
		count_any_member_has_response += len(group_responses_set)






		# PART 2
		# for each group, count the number of questions to which EVERYONE answered "yes"
		# what is the sum of those counts?

		# easiest way is to look at first group member
		# how many of the characters for the first group member
		# appear for ALL the other group members
		for char in group_responses[0]:

			char_in_all_members = True

			# see if char exists for all other group members - if not then set
			# char_in_all_members to False
			for item in group_responses:
				
				if char not in item:

					char_in_all_members = False

			# if char appears for all members, add one to
			# count_all_members_have_response var which keeps track of the total count
			# for all groups
			if char_in_all_members == True:
				#print('char', char, 'exists for all members of this group')
				count_all_members_have_response += 1

		# finished processing this group so reset the temp var group_responses
		# so it can be filled again for the next group
		group_responses = []
	
	




	else:

		# we are still in the same group so continue adding 
		# group member responses to group_responses list
		line = line.strip()
		group_responses.append(line)
		



# print out final counts for parts 1 and 2
print('TOTAL COUNT FOR ANY MEMBER HAS RESPONSE =', count_any_member_has_response)
print('TOTAL COUNT FOR ALL MEMBER HAVE RESPONSES =', count_all_members_have_response)





