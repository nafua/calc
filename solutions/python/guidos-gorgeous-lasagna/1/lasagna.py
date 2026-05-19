"""Functions used in preparing Guido's gorgeous lasagna!

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME= 40



def bake_time_remaining(time_in_oven):
    """Remove 'pass' and complete the 'bake_time_remaining()' function ."""
    time_remaining= int(EXPECTED_BAKE_TIME-time_in_oven)
    return time_remaining

    pass



def preparation_time_in_minutes(number_of_layers):
    """Define the 'preparation_time_in_minutes()' 
function"""
    time_in_minutes= int(2*number_of_layers)
    return time_in_minutes
    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """"define the 'elapsed_time_in_minutes()' function"""
    time_elapsed= number_of_layers*2 + elapsed_bake_time
    return time_elapsed
    
"""Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """

# TODO: Remember to go back and add docstrings to all your functions
