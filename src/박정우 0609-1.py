def avg(list):
    sum=0
    avg=0
    for element in list:
        sum=sum+element

    avg=sum/len(list)

    return avg

list=[90,80,70,60,50]
print(avg(list))
