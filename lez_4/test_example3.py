
def total_passing_yards(filename, player):
    '''
    We want to make a function that takes in the filename of the dataset and
    the name of a player as input and then outputs the total number of passing yards that
    player achieved in the dataset.
    The file is a csm file with an header and 8 or more columns.
    Column 4 is the player's name and column 8 is the number of passing yards for that player

    >>> total_passing_yards('_4_test_example3_data.txt', 'Marco')
    350
    '''

    total_yards = 0
    with open(filename, 'r') as file:
        for line in file:
            columns = line.strip().split(',')
            if columns[3] == player:
                total_yards += int(columns[7])
    return total_yards


import doctest
doctest.testmod(verbose=True)
