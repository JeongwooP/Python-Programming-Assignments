score = [90,80,70,60,50]

def average(list):
    sum=0
    avg=0
    for element in list:
        sum=sum+element
    avg=sum/len(list)
    return avg

print('score=', score)
print('average =', average(score))
