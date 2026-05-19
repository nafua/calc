def is_armstrong_number(number):
    digit_breakdown= [int(num) for num in str(number)] #this breaks down the number into a list
    length_number= len(digit_breakdown)
    result= sum(num**length_number for num in digit_breakdown)
    return result== number