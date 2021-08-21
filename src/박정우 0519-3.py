while(True):
    n=int(input('enter the number:'))
    if n==0:
        print('EXIT')
        break
    elif n%2==0:
        print(n, 'is even number')
    else:
        print(n,'is odd number')
