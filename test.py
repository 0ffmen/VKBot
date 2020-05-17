import time

# options
a = 0
b = 1000
print ( f'Загадай число от {a} до {b}' )

#func
def print_rules():
    rules = '''Если я угадаю, напиши "=",
 если твое число меньше, то введи "<" ,
 а если больше, то ">"
 и нажми на Enter.'''
    print() #empty
    print(rules)
    print()
    
# time
time.sleep(1)
print('Загадал?')
time.sleep(1)
print('Тогда поехали')
time.sleep(1)
print_rules()
time.sleep(1)

#code
steps = 0

while True:
    if a > b:
        print( 'Что-то пошло не так...')
        print( 'Попробуй заново')
        break
    if a == b:
        print (f'Твое число {a}')
        print (f'Потребовалось {steps} шагов')
        break
        
    steps += 1

    number = ( a + b ) // 2
    answer = input (f'Это {number}? ')

    if answer == '=':
        print ('Ура, я отгадал!')
        print(f'Потребовалось шагов: {steps}')
        break
    elif answer == '<':
        b = number - 1
    elif answer == '>':
        a = number + 1
    else: 
	    print ('Не понял, на всякий случай повторю правила')
	    print_rules()
	    steps -= 1