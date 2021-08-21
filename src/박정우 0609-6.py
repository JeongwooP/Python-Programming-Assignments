
def sec_to_h_m_s(second):
    if second<24*60*60:
        hour = int(second/(60*60))
        second=second-hour*60*60
        minute=int(second/60)
        second=second - minute*60
        second = second
        print(hour,'시',minute,'분',second,'초 입니다')
    else:
        message='하루치를 입력하시오'
        print(message)

s=int(input('초 입력:'))
sec_to_h_m_s(s)
    

            
