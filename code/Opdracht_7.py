def add(number_1, number_2):
    print(number_1 + number_2)

def subtract(number_1, number_2):
    print(number_1 - number_2)

def multiply(number_1, number_2):
    print(number_1 * number_2)

def divide(number_1, number_2):
    print(number_1 / number_2)

number_1 = int(input('Geef een getal: '))
number_2 = int(input('geef een tweede getal: '))
operator = input('kies de manier van rekenen (+,-,/,*)')

if operator == '+':
    add((number_1), number_2)
elif operator == '-':
    subtract(number_1, number_2)
elif operator == '/':
    divide(number_1, number_2)
elif operator == '*':
    multiply(number_1, number_2)


