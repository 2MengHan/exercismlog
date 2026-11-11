def equilateral(sides):
    sides.sort()
    is_equilateral = False
    if sides[0]==sides[1] and sides [1]==sides[2]:
        is_equilateral = True
    if sides[0]<=0 or sides[1]<=0 or sides[2]<=0 or sides[0]+sides[1]<=sides[2]:
        is_equilateral = False
    return is_equilateral


def isosceles(sides):
    sides.sort()
    is_isosceles = False
    if sides[0] == sides[1] or sides[0]==sides[2] or sides[1]==sides[2]:
        is_isosceles = True
    if sides[0]<=0 or sides[1]<=0 or sides[2]<=0 or sides[0]+sides[1]<=sides[2]:
        is_isosceles = False
    return is_isosceles


def scalene(sides):
    sides.sort()
    is_scalene = not(isosceles(sides))
    if sides[0]<=0 or sides[1]<=0 or sides[2]<=0 or sides[0]+sides[1]<=sides[2]:
        is_scalene = False
    return is_scalene
