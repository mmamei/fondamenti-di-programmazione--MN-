
def most_students(classroom):
    '''
    classroom is a list of list containing letters (string)
    '' to represent an empty seat
    's' to represent a student
    I want to find the largest number of new students we could add in a single row 
    in the classroom. (Equivalently, we’re looking for the largest number of empty seats in
    any row.)

    >>> most_students([['s', 's', '', 's', ''],\
                       ['s', '', 's', '', 's'],\
                       ['', 's', '', 's', ''],\
                       ['s', 's', 's', 's', 's']])
    3
    '''
    max_empty_seats = 0
    for row in classroom:
        empty_seats = row.count('')
        if empty_seats > max_empty_seats:
            max_empty_seats = empty_seats
    return max_empty_seats


import doctest
doctest.testmod(verbose=False)
