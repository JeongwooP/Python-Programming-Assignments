def price(totalprice):
    sum=totalprice*10/11
    tax=totalprice/11
    return print('제품가격은',sum,'원, 부가가치세는',tax,'원입니다')
    
tp=int(input('소비자 가격을 입력하시오:'))
price(tp)
