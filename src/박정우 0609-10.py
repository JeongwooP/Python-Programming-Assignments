def Down(now, target):
    for floor in range(now, target-1, -1):
        print('This floor is',floor,'th floor.')
    print('you arrived at',target,'floor')

def Up(now, target):
    for floor in range(now, target+1):
        print('This floor is',floor,'th floor.')
    print('you arrived at',target,'floor')

inputlocation= int(input('which floor:'))
nowlocation= int(input('present floor:'))

if ((inputlocation == nowlocation) or (inputlocation < 1) or (6 < inputlocation)):
    print('press an other floor(1~6).')
else:
    if(nowlocation>inputlocation):
        Down(nowlocation,inputlocation)
    else:
        Up(nowlocation, inputlocation)
     
