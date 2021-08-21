list_fruit = ['apple', 'banana', 'tomato']
list_animal = ['bear', 'elephant','monkey']
list_instrument = ['guitar', 'piano', 'harmonica']

def length(list):
    sum=0
    for element in list:
        sum=sum+len(element)
    return sum
print('list_fruit =', list_fruit)
print('list_aniaml =',list_animal)
print('list_instrument =',list_instrument)
print("list_fruit's words length = ", length(list_fruit))
print("list_animal's words length = ", length(list_animal))
print("list_instrument's words length = ", length(list_instrument))
