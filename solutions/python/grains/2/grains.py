def square(number):
    """this raises an error"""
    
    if number<1 or number>64:
        raise ValueError('square must be between 1 and 64')
        
    square_value =2 ** (number-1) #to show the number of grains on a given square
    return square_value


def total():
    total_fig= sum(2**(n-1) for n in range(1,65))
    return total_fig
