def input_int(message=''):
    while True:
        result = int(input(message))
        return result


a = input_int('Введите a:')
b = input_int('Введите b:')

print(f'{a} + {b} = {a + b}')
