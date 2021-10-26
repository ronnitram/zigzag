#!/usr/bin/python3

import sys
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser()


def isPalindrome(instr):
	return instr == instr[::-1]


def getLongestPalindrome(instr):
	max = 0
	longeststr = ""
	start = 0
	while (max < len(instr) - start):
		end = len(instr)
		tmpstr = instr[start:end]
		# Check if the first character in the substring exist (reverse find)
		match = tmpstr.rfind(instr[start])
		while (match > 0):
			# Update end index of the substring and check if palindrome
			end = match + 1
			tmpstr = tmpstr[:end]
			if isPalindrome(tmpstr):
				# Overwrite the current longest palindrome word.
				if len(tmpstr) > max:
					max = len(tmpstr)
					longeststr = tmpstr
					start = start + max
				break;
			else:
				# Current substring is not palindrome, offset subtring adjust end index and try to find a match again.
				end -= 1
				tmpstr = tmpstr[:end]
				match = tmpstr.rfind(instr[start])
		else:
			start+=1

	if max == 0:
		print("No Palindromic Substring Found.")
	else:
		print(longeststr)


def palindromeCut(instr):
	words = list()
	start = 0
	tmpword = ""
	count = 0
	while (start <len(instr)):
		tmpword += instr[start]
		end = len(instr)
		tmpstr = instr[start:end]
		# Check if the first character in the substring exist (reverse find)
		match = tmpstr.rfind(instr[start])
		while (match > 0):
			# Update end index of the substring and check if palindrome
			end = match + 1
			tmpstr = tmpstr[:end]
			if isPalindrome(tmpstr):
				start = start + len(tmpstr)
				# remove last character in tmpword since it is the start character of the palindrome word
				tmpword = tmpword[:-1]
				if len(tmpword) > 0:
					# Add accumulated characters to the list
					words.append(tmpword)
					tmpword = ""
				
				# Add palindrome word to the list
				words.append(tmpstr)
				count += 1
				break;
			else:
				# Current substring is not palindrome, offset subtring adjust end index and try to find a match again.
				end -= 1
				tmpstr = tmpstr[:end]
				match = tmpstr.rfind(instr[start])
		else:
			start+=1

	# Add accumulated characters to the list
	words.append(tmpword)
	print(str(count)+ " //",end=" ");
	delimiter = " | "
	print(delimiter.join(words));


if __name__ == '__main__':
	# Optional level argument
	parser.add_argument('--level', type=int, nargs='?', default = 1,
						help='An optional level argument [values: 1-3]')

	# String argument
	parser.add_argument('input_string', help='Input string argument')
	# Parse
	args = parser.parse_args()
	inputStr = args.input_string.lower()

	if args.level < 1 or args.level > 3:
		parser.error("Please select a level from 1-3")
	elif args.level == 1:
		if isPalindrome(inputStr):
			print("true // it's written the same forward and backward")
		else:
			print("false // it's not written the same forward and backward")
	elif args.level == 2:
		getLongestPalindrome(inputStr)
	elif args.level == 3:
		palindromeCut(inputStr)