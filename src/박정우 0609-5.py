def tri_area(bottom, height):
    area = float(0.5*bottom*height)
    return area

b=int(input('밑변 입력:'))
h=int(input('높이 입력:'))

print('삼각형의 면적은',tri_area(b,h))
    
