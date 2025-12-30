def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return None
    else:
        return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': division
}

num_1 = float(input('Введите первое число: '))
operator = input('Введите операцию (+, -, *, /): ')
num_2 = float(input('Введите второе число: '))

if operator in operations:
    result = operations[operator](num_1, num_2)
    if result == None:
        print('Ошибка: деление на 0 невозможно')
    else:
        print(f'Результат: {num_1} {operator} {num_2} = {result}')
else:
    print('Ошибка: неизвестная операция')