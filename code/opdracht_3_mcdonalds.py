hot_drinks_list = ["Koffie", "Cappuccino" , "Chocolade melk"]
cold_drinks_list = ["Coca Cola", "Cola Zero" , "7-Up", "Fanta","Fristi"]
burgers_list = ["Hamburger", "Cheeseburger", "Big Mac", "Quater Pounder"]
def incorrect_response():
    print("not an appropriate answer, try again later.")
    exit()

def burgers():
    burger_kind = input("Wat voor burger wilt u hebben?\n"
                        "1.Hamburger\n"
                        "2.Cheeseburger\n"
                        "3.Big Mac\n"
                        "4.Quater Pounder\n"
                        "> ")
    burger_kind = burger_kind.replace(" ", "")
    return burger_kind

def hot_drinks():
    hot_drink = input("1.Koffie\n"
                      "2.Cappucino\n"
                      "3.Chocolade melk\n"
                      "> ")
    hot_drink_type = hot_drink.replace(" ", "")
    return hot_drink_type

def cold_drinks():
    cold_drink = input("1.Coca Cola\n"
                       "2.Cola Zero\n"
                       "3.7-Up\n"
                       "4.Fanta\n"
                       "5.Fristi\n"
                       "> ")
    cold_drink_type = cold_drink.replace(" ", "")
    return cold_drink_type


eating_location = input("Hier opeten of meenemen? [1/2] ")
if eating_location == "1":
    print("Hier opeten")
elif eating_location == "2":
    print("Meenemen")
else:
    incorrect_response()
burg_or_drink = input("Burgers of drankjes? [1/2] ")
if burg_or_drink == "1":
    burger_choice = burgers()
    #chat gpt had de if statement voor de cold drinks gemaakt en ik heb hem aangepast voor burgers
    if burger_choice in ["1", "2", "3"]:
        print(f"U heeft gekozen voor {cold_drinks_list[int(burger_choice) - 1]}")
    elif burger_choice == "4":
        qp_cheese= input("Wil je de Quater pounder met kaas? [y/n]")
        if qp_cheese == "y":
            print("U heeft gekozen voor een Quater Pounder met kaas")
        elif qp_cheese == "n":
            print("U heeft gekozen voor een Quater Pounder zonder kaas")




elif burg_or_drink == "2":
    hot_or_cold = input("Wil je warme of koude drankjes? [1/2] ")
    if hot_or_cold == "1":
        hot_drink_choice = hot_drinks()
        # chatgpt had de if statement voor de cold drinks gemaakt en ik heb hem aangepast voor hotdrinks
        if hot_drink_choice in ["1", "2", "3", "4", "5"]:
            print(f"U heeft gekozen voor {cold_drinks_list[int(hot_drink_choice) - 1]}")
        else:
            incorrect_response()

    elif hot_or_cold == "2":
        cold_drink_choice = cold_drinks()
        # chatgpt made this if statement
        if cold_drink_choice in ["1", "2", "3", "4", "5"]:
            print(f"U heeft gekozen voor {cold_drinks_list[int(cold_drink_choice) - 1]}")
        else:
            incorrect_response()
    else:
        incorrect_response()

if eating_location == "1":
    print("Bedankt voor het bestellen, en eetsmakkelijk in ons restaurant")
elif eating_location == "2":
    print("Bedankt voor het bestellen, en eetsmakkelijk in ons restaurant")