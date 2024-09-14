import time

stay_on = True
cache = {}

def zeef_van_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    current_prime = 2
    while current_prime * current_prime <= limit:
        if is_prime[current_prime]:
            for multiple in range(current_prime * current_prime, limit + 1, current_prime):
                is_prime[multiple] = False
        current_prime += 1
    
    prime_numbers = []
    for number in range(2, limit + 1):
        if is_prime[number]:
            prime_numbers.append(number)
    
    return prime_numbers

def check_in_cache(number):
    if number in cache:
        print(f"{number} zit in de cache")
        return cache[number]
    else:
        print(f"{number} zit niet in cache")
        result = zeef_van_eratosthenes(number)
        cache[number] = result
        return result

while stay_on:
    chosen_number = int(input("kies een getal: "))
    if chosen_number == "":
        stay_on = False
    if chosen_number:
        start_time = time.time()
        result = check_in_cache(chosen_number)
        end_time = time.time()
        print(f"Priemgetallen tot gekozen nummer {chosen_number}: {result}")
        print(f"{round((end_time - start_time) * 1000,2)} milliseconden")
