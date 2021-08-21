random=input('구구단프로그램을 실행하실려면 아무키나 입력하시오:')
s_num=0
for element in range(0, 9):
    element+=1
    s_num=0
    while (True):
        print(element,'x',s_num,'=',element*s_num)
        s_num+=1
        if (s_num>=10):
            break
