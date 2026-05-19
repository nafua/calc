
def square(number):
    """This raises
    an error message."""
    if number<1 or number>64:
        raise ValueError('square must be between 1 and 64')
        
    square_value =2 ** (number-1) #to show the number of grains on a given square
    return square_value


def total():
    fish= sum(2**(num-1) for num in range(1,65))
    return fish
