Shirts=int(input('How many shirts?'))
Sweaters=int(input('How many sweaters?'))
Total=10000*Shirts+30000*Sweaters
Final_price1=Total*0.95
Final_price2=Total*0.85
if Total<=100000:
    print('Final price is',Final_price1,)
else :
    print('Final price is',Final_price2,)
