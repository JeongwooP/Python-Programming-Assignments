def longest(num1, num2, num3):
    maximum=''
    if((len(num1)>len(num2)) and (len(num1)>len(num3))):
        maximum=num1
    elif((len(num2)>len(num3)) and (len(num2)>len(num1))):
        maximum=num2
    elif((len(num3)>len(num2)) and (len(num3)>len(num1))):
        maximum=num3
    else:
       print('wrong')
    return print('the longest word is',maximum)

def shortest(num1, num2, num3):
    minimum=''
    if((len(num1)<len(num2)) and (len(num1)<len(num3))):
        minimum=num1
    elif((len(num2)<len(num3)) and (len(num2)<len(num1))):
        minimum=num2
    elif((len(num3)<len(num2)) and (len(num3)<len(num1))):
        minimum=num3
    else:
        print('wrong')
    return print('the shortest word is', minimum)




