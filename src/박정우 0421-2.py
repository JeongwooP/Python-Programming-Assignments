ID='abc'
password='123'
write1=input('id:')
write2=input('password:')
if (write1==ID):
    if (write2==password):
        print('logged in')
    else:
        print('log in failed:password error')
else:
    if (write2==password):
        print('log in failed:id error')
    else:
        print('log in failed:id and password error')
    
