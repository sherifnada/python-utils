"""
A python utilities library that helps me in my day to day work. 

Author: Sherif Nada, 2014
"""


def print2DListAsTable(twoDimensionalList):
	"""
	Takes a two-dimensional list and returns it in a table format that is easy
	to import into MS word/excel. 
	
	keyword arguments: twoDimensionalList - 2D list
	"""

	print "----------------------------------------"
	myPrettyString = ''
	for row in range(len(twoDimensionalList)):
		for item in range(len(twoDimensionalList[row])):
			myPrettyString += str(twoDimensionalList[row][item]) + "\t"

		myPrettyString += '\n'

	return myPrettyString