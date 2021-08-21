ID=input('enter your id')
PW=input('enter your password')
limit=len(ID)
limit1=len(PW)
if (limit<=10):
    if (limit1<=10):
        print('회원가입 성공')
    else:
        print('회원가입 실패: password 길이가 10을 초과')
else:
    if (limit1<=10):
        print('회원가입 실패: id 길이가 10을 초과')
    else:
        print('회원가입 실패: id와 password 길이가 10을 초과')

