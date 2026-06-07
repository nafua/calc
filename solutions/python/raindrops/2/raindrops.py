def convert(number):
    result= ''
    if number%3 == 0:
        result+= str('Pling')
    if number%5 ==0:
        result+= str('Plang')        
    if number%7 == 0:
        result+= str('Plong')

    return result or str(number)
