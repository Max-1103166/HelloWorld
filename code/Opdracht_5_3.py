is_on = True

while is_on:
    chosen_number = input("geef een getal: ")
    if chosen_number != ".":
        numbers = list(range(2, int(chosen_number)))
        number = int(chosen_number)
        for divider in numbers:
            if number % divider == 0:
                print(f"{number} is geen prime getal")
                break
            else:
                print(f"{number} is een prime getal")
                break
    else:
        print("totziens")
        is_on = False