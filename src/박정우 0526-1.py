
def add(num1, num2):
    result = (num1 + num2)
    return result

def sub(x, y):
    result = (x - y)
    return result

def mul(num1, num2):
    result = (num1 * num2)
    return result

def div(num1, num2):
    result = (num1 / num2)
    return result

a=int(input('number1:'))
b=int(input('number2:'))

print(a,'+',b,'=',add(a,b))

num = sub(a,b)
print(a,'-',b,'=',num)

num = mul(a,b)
print(a,'x',b,'=',num)

num = div(a,b)
print(a,'/',b,'=',num)

