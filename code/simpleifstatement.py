is_on = True

def questionaire(loop):
    print("How are you?")
    question_one = input("")
    if question_one == "Good":
        print("nice")
        loop = False

    elif question_one == "Bad":
        print("why")
        reason = input("")
        if len(reason) > 0:
            print("That sucks")
            loop = False
        elif len(reason) == 0:
            print("Answer the question")
    questionaire(loop)


while is_on:
    questionaire(is_on)

