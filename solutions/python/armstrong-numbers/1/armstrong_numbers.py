def is_armstrong_number(number):
    digit_breakdown= [int(d) for d in str(number)] #this breaks down the number into a list
    length_number= len(digit_breakdown)
    result= list(map(lambda x: x**length_number, digit_breakdown))
    final_result= sum(result)
    if final_result == number:
        return True
    else:
        return False