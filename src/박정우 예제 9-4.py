list_score=[90,80,70,60,50]

def avg(score):
    sum=0
    for element in score:
       sum=sum+element
    average=sum/5
    return average

def highest(score):
    maximum=0
    for element in score:
        if maximum<element:
            maximum=element
    return maximum

def check(score):
    if avg(score)>=60:
        go='passed'
    else:
        go='failed'
    return go

print('score=',list_score)
print('averge = ',avg(list_score))
print('highest score = ',highest(list_score))
print('pass or fail = ', check(list_score))
        

    
