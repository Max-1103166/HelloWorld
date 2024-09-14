numbers = list(range(1,100))

for number in numbers:
    is_prime_number = True
    if number == 1:
        is_prime_number = False
    for divider in numbers:
        if number > divider > 1:
            if number % divider == 0:
                is_prime_number = False
                break
    if is_prime_number:
        print(number)