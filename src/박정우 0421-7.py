eng=int(input('english score?'))
math=int(input('math score?'))
total=eng+math
if total<110:
    print('불합격')
elif eng >=40:
    if math>=40:
        print('합격')
    else:
        print('불합격:수학 점수가 부족합니다')
else:
    print('불합격: 영어 점수가 부족합니다')
