age=int(input("what's your age?"))

if age<=7:
    print('kindergarten')
    t1=1000
    print('fee:',t1)
elif age <=13:
    print('elementary')
    t2=2000
    print('fee:',t2)
elif age <=16:
    print('middle school')
    t3=3000
    print('fee:',t3)
elif age <=19:
    print('high school')
    t4=4000
    print('fee:',t4)
elif age <=23:
    print('university student')
    t5=5000
    print('fee:',t5)
else:
    print('adult')
    t6=6000
    print('fee:',t6)
