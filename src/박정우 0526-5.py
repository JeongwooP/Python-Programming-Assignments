def avg(smt):

    b=0
    c=0
    
    for element in smt:
        b=b+element
    c=b/len(smt)
    return c

something=[10, 20 ,30, 40]
print(avg(something))
