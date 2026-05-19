def isvalidtriangle(sides):
    a, b, c = sides
    return (
        a > 0 and b > 0 and c > 0 and
        a + b >= c and
        b + c >= a and
        a + c >= b
    )

def equilateral(sides):
    if not isvalidtriangle(sides):
        return False
    a, b, c = sides
    return a == b == c 


def isosceles(sides):
    if not isvalidtriangle(sides):
        return False
    return sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2]


def scalene(sides):
    if not isvalidtriangle(sides):
        return False
    a,b,c= sides
    return a != b and a!= c and b !=c
