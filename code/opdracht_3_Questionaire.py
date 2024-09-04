print("online or offline")
question_1 = input("")

def incorrect_answer():
    print("not a suitable answer, try again")

def approval_rules():
    is_approved = input("Did you get approved? [y/n] ")
    return is_approved

def admin_question():
    is_admin = input("Are you an administrator? [y/n] ")
    return is_admin

if question_1.lower() == "online":
    is_admin = admin_question()
    if is_admin.lower() == "y":
        print("a")
    elif is_admin.lower() == "n":
        is_approved = approval_rules()
        if is_approved == "y":
            print("b")
        elif is_approved == "n":
            print("c")
        else:
            incorrect_answer()


elif question_1.lower() == "offline":
    is_admin = admin_question()
    if is_admin.lower() == "y":
        print("a")
    elif is_admin.lower() == "n":
        is_approved = approval_rules()
        if is_approved == "y":
            print("b")
        elif is_approved == "n":
            print("c")
        else:
            incorrect_answer()
    else:
        incorrect_answer()
else:
    incorrect_answer()

