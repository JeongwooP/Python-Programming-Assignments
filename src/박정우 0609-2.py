def passorfail(scores):
    sum=0
    avg=0
    for element in scores:
        sum+=element
    avg=sum/len(scores)
    if avg>=60:
        result='pass'
    else:
        result='fail'
    return result

numlist=[30,40,50,60,70]
print(passorfail(numlist))
