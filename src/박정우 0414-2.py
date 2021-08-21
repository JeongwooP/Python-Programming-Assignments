pencils=int(input('구하고자 하는 연필 개수를 입력하시오.'))
pens=int(input('구하고자 하는 펜의 개수를 입력하시오.'))
total=(1000*pencils + 2000*pens)
if (total>10000):
        Final_price=total*0.9
        print('본 가격은', total,'이고 ''총 할인된 가격은', Final_price,'입니다')
        
