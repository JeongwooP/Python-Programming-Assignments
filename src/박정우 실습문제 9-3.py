def avg(numlist):
    sum=0
    average=0
    for element in numlist:
        sum=sum+element
    average=sum/5
    if (average>=60):
        result='PASS'
    else :
        result='FAIL'
    return result

score=[30,40,50,60,70]
print(avg(score))        
        
