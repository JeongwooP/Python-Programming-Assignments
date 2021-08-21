def maxlist(numlist):
    maximum=0
    for number in numlist:
        if maximum < number:
            maximum = number
    return maximum

math_score= [80, 50, 90, 75, 35]
english_score = [90,50, 70, 80, 100]
computer_score = [99, 45, 46, 34, 67, 80]
korean_score = [65, 43, 76, 83]

print('math_score=',math_score)
print('maxlist(math_score)')
print(maxlist(math_score))

print('english_score=',english_score)
print('maxlist(english_score)')
print(maxlist(english_score))

print('computer_score=',computer_score)
print('maxlist(computer_score)')
print(maxlist(computer_score))

print('korean_score=',korean_score)
print('maxlist(korean_score)')
print(maxlist(korean_score))
