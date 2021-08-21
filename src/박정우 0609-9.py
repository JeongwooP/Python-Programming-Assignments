def pcutprice(contractprice, period):
    if period<=6:
        cutprice=contractprice
    elif period>6 &period<=12:
        cutprice=contractprice*0.1
    else:
        cutprice=contractprice*0.2
    return cutprice

def ccutprice(contractprice, cardcode):
    if cardcode==11:
        cutprice=contractprice*0.05
    elif cardcode==12:
        cutprice=contractprice*0.08
    elif cardcode==13:
        cutprice=contractprice*0.12
    return cutprice

cp=int(input('계약 금액을 입력하시오:'))
p=int(input('사용 개월 수를 입력하시오:'))
cc=int(input('카드코드를 입력하시오:'))

finalprice=cp-(pcutprice(cp, p)+ccutprice(cp, cc))
print('최종요금은',finalprice,'입니다')
