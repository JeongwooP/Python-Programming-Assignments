
def gaplist(numlist):
    maximum = 0
    for number in numlist:
        if maximum < number:
            maximum = number

    minimum = 100
    for number in numlist:
        if minimum > number:
            minimum = number
            
    return maximum-minimum

math_score = [80, 50, 90, 75, 35]
eng_score = [90, 96, 93, 88, 91, 89, 85]



print('gap math score = ', gaplist(math_score))
print('gap english score = ', gaplist(eng_score))




