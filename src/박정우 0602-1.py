
def maxlist(numlist):
    maximum = 0
    for number in numlist:
        if maximum < number:
            maximum = number
    return maximum

def minlist(numlist):
    minimum = 100
    for number in numlist:
        if minimum > number:
            minimum = number
    return minimum

def gap(numlist):
    dif=maxlist(numlist)-minlist(numlist)
    return dif

math_score = [80, 50, 90, 75, 35]
eng_score = [90, 96, 93, 88, 91, 89, 85]

max_math=maxlist(math_score)
max_eng=maxlist(eng_score)

min_math=minlist(math_score)
min_eng=minlist(eng_score)

print('maximum math score = ', max_math)
print('maximum english score = ', max_eng)
print('minimum math score = ', min_math)
print('minimum english score = ', min_eng)
print('gap math score = ', gap(math_score))
print('gap english score = ', gap(eng_score))

gap_math=gap(math_score)


