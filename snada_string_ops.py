"""
A python utilities library that helps me in my day to day work.

Author: Sherif Nada, 2014
"""


def two_d_list_as_table(two_dimensional_list):
    """
    Takes a two-dimensional list and returns it in a table format that is easy
    to import into MS word/excel.

    Args:
        twoDimensionalList - 2D list

    Returns:
        A string
    """

    print "----------------------------------------"
    my_pretty_string = ''
    for row in range(len(two_dimensional_list)):
        for item in range(len(two_dimensional_list[row])):
            my_pretty_string += str(two_dimensional_list[row][item]) + "\t"

        my_pretty_string += '\n'

    return my_pretty_string
