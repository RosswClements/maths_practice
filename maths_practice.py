import random
def main():
    on = True
    while on == True:
        print("What would you like to practice?")
        op = input("+ , - , x , % , or quit: ").lower()
        if op == "+":
            plus()

        elif op == "-":
            sub()

        elif op == "x":
            mul()

        elif op =="%":
            div()

        else:
            print("You have quit, goodbye!")
            quit()


def plus():
    count = 0
    rand1 = random.randint(1,12)
    rand2 = random.randint(1,12)
    print(f"What is {rand1} + {rand2} ?")
    ans = input("")
    result = rand1 + rand2
    correct = False
    while correct == False:
        if int(ans) == result:
            print(f"Well done! The answer was {result}")
            correct = True
            main()
        else: 
            if count == 2:
                print(f"Better luck next time, the answer was {result}")
                main()
            else:
                print("Try again")
                print(f"What is {rand1} + {rand2} ?")
                ans = input("")
                count +=1

def sub():
    count = 0
    rand1 = random.randint(1,12)
    rand2 = random.randint(1,12)
    print(f"What is {rand1} - {rand2} ?")
    ans = input("")
    result = rand1 - rand2
    correct = False
    while correct == False:
        if int(ans) == result:
            print(f"Well done! The answer was {result}")
            correct = True
            main()
        else: 
            if count == 2:
                print(f"Better luck next time, the answer was {result}")
                main()
            else:
                print("Try again")
                print(f"What is {rand1} - {rand2} ?")
                ans = input("")
                count +=1

def mul():
    count = 0
    rand1 = random.randint(1,12)
    rand2 = random.randint(1,12)
    print(f"What is {rand1} x {rand2} ?")
    ans = input("")
    result = rand1 * rand2
    correct = False
    while correct == False:
        if int(ans) == result:
            print(f"Well done! The answer was {result}")
            correct = True
            main()
        else:
            if count == 2:
                print(f"Better luck next time, the answer was {result}")
                main()
            else:
                print("Try again")
                print(f"What is {rand1} x {rand2} ?")
                ans = input("")
                count +=1

def div():
    count = 0
    rand1 = random.randint(1,12)
    rand2 = random.randint(1,12)
    print(f"What is {rand1} % {rand2} ?")
    ans = input("")
    result = rand1 / rand2
    result = round(result, 3)
    correct = False
    while correct == False:
        if int(ans) == result:
            print(f"Well done! The answer was {result}")
            correct = True
            main()
        else: 
            if count == 2:
                print(f"Better luck next time, the answer was {result}")
                main()
            else:
                print("Try again")
                print(f"What is {rand1} % {rand2} ?")
                ans = input("")
                count +=1


main()