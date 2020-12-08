import copy


# read in boot sequence file
bootseq_file = open('day8_bootseq.txt', 'r')
lines = bootseq_file.readlines()
original_lines = lines

# initialise variables to keep track of commands run already and info on the file length
accumulator_count = 0
line_numbers_already_run = []
final_line_number = len(lines)
line_number = 0
command_line_number_to_replace = 0


# keep iterating over boot sequence commands until reach final line number in sequence
while line_number != final_line_number:

	line = lines[line_number].strip()
	command, step = line.split()[0], int(line.split()[1])

	
	# PART 1
	# immediately before any instruction is executed a second time, what value is in the accumulator?

	if line_number in line_numbers_already_run:
		
		# UNCOMMENT THIS TO STOP FOR PART 1
		#break


		# PART 2

		# if change a nop to a jmp or vice-versa, does this fix the infinite loop?

		# if end up in this statement, we have an infinite loop, so 
		# - reset line_numbers_already_run, 
		# - reset line_number to 0 and line to line, command and step to values for line 0
		# - reset accumulator_count to 0
		# - change a jmp to a nop or vice versa:
		#   - change the line according to how many times we have been in this if statment
		#   - first time = reset line 0, second time = reset line 1, etc
		#   - if command = acc, don't change this so just skip to next command
		# - reset lines to original lines in file first so changed lines are not permanent
		
		line_numbers_already_run = []
		line_number = 0
		accumulator_count = 0

		 # lazy way - this is to replace previous lines changed in last replacement back to original
		 # thus only one line changed in each iteration - not more and more lines as we iterate more and more
		lines = copy.deepcopy(original_lines)

		line = lines[line_number].strip()
		command, step = line.split()[0], int(line.split()[1])

		# we know the acc lines are correct so don't change these
		while lines[command_line_number_to_replace].split()[0] == 'acc':
			command_line_number_to_replace += 1
		
		# replace the line at line number command_line_number_to_replace that is nop to jmp and vice versa
		if lines[command_line_number_to_replace].split()[0] == 'nop':
			print('replacing line', command_line_number_to_replace, 'nop to jmp')
			lines[command_line_number_to_replace] = lines[command_line_number_to_replace].replace('nop', 'jmp')
		elif lines[command_line_number_to_replace].split()[0] == 'jmp':
			print('replacing line', command_line_number_to_replace, 'jmp to nop')
			lines[command_line_number_to_replace] = lines[command_line_number_to_replace].replace('jmp', 'nop')
		
		# this will be for the iteration after this one
		command_line_number_to_replace += 1



	# add line numbers alread run to list so can see if we've already run this line before
	line_numbers_already_run.append(line_number)

	# run steps in boot sequence
	# - nop means no operation so skip to next line
	# - acc means add value of step to accumulator_count and then skip to next line
	# - jmp means skip [step] number of lines
	if command == 'nop':
		line_number += 1
	elif command == 'acc':
		accumulator_count += step
		line_number += 1
	elif command == 'jmp':
		line_number += step


# final accumulator count (part 1 and 2) - need to uncomment break for part 1
print('Final accumulator count =', accumulator_count)