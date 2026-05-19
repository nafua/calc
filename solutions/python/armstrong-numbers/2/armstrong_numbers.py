def is_armstrong_number(number):
    digit_breakdown= [int(d) for d in str(number)] #this breaks down the number into a list
    length_number= len(digit_breakdown)
    result= sum(d**length_number for d in digit_breakdown)
    return result== number