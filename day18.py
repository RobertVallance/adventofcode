
import math

def extract_innermost_parentheses(expression):

	"""

	Extract string in innermost brackets in expression

	Parameters
	----------
	- expression (a string containing the expression to check)

	Returns
	-------
	- expression_in_bracket (string in the innermost brackets of expression)

	"""

	expression_in_bracket = ''

	for i, char in enumerate(expression):

		# if have a ')' then we know we are at the end of an innermost bracket so break out 
		# and save the final string
		if char == ')':
			break
		# if chae is '(' then reset string and start appending again
		# acts as a catch in case there are multiple inner brackets -
		# just want to save from the innermost one
		if char == '(':
			expression_in_bracket = ''
			continue
		expression_in_bracket += char

	return expression_in_bracket


def evaluate_expression_part_1(expression):

	"""

	Expression is evalated left to right instead of following BIDMAS

	Parameters
	----------
	- expression (a string containing the expression to evaluate)

	Returns
	-------
	- value (the result of evaluating expression)

	"""

	expression = expression.split()

	value = 0
	operation = '+'

	# see if char a '+' or '*'
	# if so then add or multiply the subsequent char onto value
	for char in expression:
		if char == '+': 
			operation = '+'
			continue
		elif char == '*': 
			operation = '*'
			continue

		if operation == '+':
			value += int(char)
		elif operation == '*':
			value *= int(char) 

	return value


def evaluate_expression_part_2(expression):

	"""

	Now, addition and multiplication have different precedence levels.
	Instead, addition is evaluated before multiplication.

	Parameters
	----------
	- expression (a string containing the expression to evaluate)

	Returns
	-------
	- value (the result of evaluating expression)

	"""

	expression = expression.split()

	print('expression before =', expression)

	# do addition first
	# if have '+ in expression', add the values either side of it together
	# then replace the '+' with this value and finally
	# remove the values either side of the former '+'
	while '+' in expression:
		for i, char in enumerate(expression):
			value = 0
			if char == '+': 
				value += int(expression[i+1]) + int(expression[i-1])
				expression[i] = str(value)
				del expression[i+1]
				del expression[i-1]


	# now do multiplication
	# remove the instances of '*'
	# and multiply the remaining elements in the list together
	for i, char in enumerate(expression):
		if char == '*': 
			del expression[i]
	expression = list(map(int, expression))
	value = math.prod(expression)		

	return value






###
### MAIN CODE
###


if __name__ == '__main__':

	part = 'PART 2'
	
	sum_final_values = 0

	# read file and loop over lines, adding the expression value to sum_fnal_values
	with open('day18_homework.txt', 'r') as homework_file:
	#with open('test.txt', 'r') as homework_file:

		for line in homework_file:
			line = line.strip()
			print(line)

			# while have '(' in line, means we want to keep finding and evaluating the innermost expression
			# in brackets until we have no brackets left
			while '(' in line:
				exp = extract_innermost_parentheses(line)

				if part == 'PART 1':
					exp_value = evaluate_expression_part_1(exp)
				elif part == 'PART 2':
					exp_value = evaluate_expression_part_2(exp)

				# remove expression in brackets and replace with evaluated expression
				line = line.replace('('+exp+')', str(exp_value))
				print(line)

			if part == 'PART 1':
				final_value = evaluate_expression_part_1(line)
			elif part == 'PART 2':
				final_value = evaluate_expression_part_2(line)
			
			sum_final_values += final_value

			
	print(part, 'SUM FINAL VALUES =', sum_final_values)

