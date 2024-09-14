character_name = "John"
character_age = 20
is_male = True
print("My name is " +  character_name)
print("I am above " + str(character_age) + " years of age")
print("I am of a male gender")
print("I studied Economics at the university")
character_name = "Chucks"
print("I met a friend named " + character_name)


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 4))

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result




print(raise_to_power(4, 3))



number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in number_grid:
    for col in row:
        print(col)


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(5, 8))


number_grid = [
    [21, 12, 13],
    [31, 13, 14],
    [41, 14, 15],
    [51]
]
print(number_grid[1][1])


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(4, 6))


number_grid = [
    [12, 13, 31],
    [14, 15, 51],
    [16, 17, 71],
    [0]
]
print(number_grid[0][1])


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(4, 3))


try:
    answer = 10/2
    num = input("Enter a number: ")
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")



x = True
y = False

print("X and Y = ", x and y)
print("X or Y = ", x or y)
print("Not of X = ", not x)
print("Not of Y = ", not y)

num1 = 7
num2 = 5

print("Num2 % Num1 = ", num2 % num1)
print("Num1 // Num2 = ", num1 // num2)
print("Num2 != Num1 = ", num2 != num1)

for quant in range(99, 0, -1):
    if quant > 1:
        print(quant, " Bottles of beer on the wall", quant, "Bottles of bear")
        if quant > 2:
            suffix = str(quant) + " bottles of beer on the wall"
        else:
            suffix = "1 bottle of beer on the wall"

    elif quant == 1:
        print("1 bottle of bear on the wall, 1 bottle of bear")
        suffix = "No more bear on the wall"

    print("Take one down and pass it around", suffix)
    print("---")


for quant in range(99, 0, -1):
    if quant > 1:
        print(quant, "Bottles of beer on the wall,", "bottles of beer")
        if quant > 2:
            suffix = str(quant) + " bottles of beer on the wall"
        else:
            suffix = "1 bottle of beer on the wall"

    elif quant == 1:
        print("1 bottle of beer on the wall, 1 bootle of beer")
        suffix = "No more beer on the wall"

    print("Take one down and pass it around", suffix)
    print("---")


word_list = ["suscribe", "to", "kylie", "ying"]
for name in word_list:
    print(name)
    if name == "kylie":
        break
print("THE END")


count = 0
for x in range(1, 11):
    if x%2 == 0:
        count += 1
        print(x)
print(f"We have {count} even number")


count = 0
while count < 10:
    count += 1
    print("Number: ", count)
print("Good Bye")


secret_word = "bicycle"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    verdict = "Out of Guesses, YOU LOSE!"
else:
    verdict = "YOU WIN!"
print(verdict)



import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you're giving up")
else:
    print("Congratulation. You made it!")




#Nested While Loop
'''
print("Welcome to Guarranty Trust Bank")
restart = "Y"
chances = 3
balance = 100000
while chances >= 0:
    pin = int(input("Please Enter the 4 Digit Pin: "))
    if pin == (1234):
        print("You entered your Pin correctly\n")
        while restart not in ("n", "NO", "no", "N"):
            print("Please Press 1 For Your Balance\n")
            print("Please Press 2 To Make a Withdrawal\n")
            print("Please Press 3 To Pay in\n")
            print("Please Press 4 To Return Card\n")
            option = int(input("What would you like to choose?"))
            if option == 1:
                print("Your Account Balance is #", balance, "\n")
                restart = input("Would you like to go back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawal = float(input("How Much Would you like to withdraw? \n#500/#1000/#1500/#2000/#5000/#10000/#20000"))
                if withdrawal in (500, 1000, 1500, 2000, 5000, 10000, 20000):
                    balance = balance - withdrawal
                    print("\nYour Account Balance is #", balance)
                    restart = input("Would you like to go back? ")
                    if restart in ("n", "NO", "no", "N"):
                        print("Thank You.")
                        break
                elif withdrawal != [500, 1000, 1500, 2000, 5000, 10000, 20000]:
                    print("Invalid Amount, Please Try Again\n")
                    restart = ("y")
                elif withdrawal == 1:
                    withdrawal = float(input("Enter Your Desired Amount"))


            elif option == 3:
                Pay_In = float(input("How Much Would You Like to Pay In? "))
                balance = balance + Pay_Innce)
                restart = input("Would you like to go back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break
                print("\n Your balance is #", bala
'''

'''
            elif option == 4:
                print("Please wait whilst your card is returned....\n")
                print("Thank you for your service")
                break
            else:
                print("Please enter a correct number. \n")
                restart = ("y")
    elif pin != ("1234"):
        print("Incorrect Password")
        chances = chances - 1
        if chances == 0:
            print("\n No more entries.")
            break
'''

'''
print("Welcome to Guarranty Trust Bank")
resart = "Y"
chances = 3
balance = 100000
while chance >= 0:
    pin = int(input("Enter Your 4 Digit Pin: "))
    if pin == (1234):
        print("You entered your Pin correctly\n")
        while restart not in ("n", "NO", "no", "N"):
            print("Please Press 1 To Check Balance\n")
            print("Please Press 2 To Make Withdrawal\n")
            print("Please Press 3 To Pay In\n")
            print("Please Press 4 To Return Card\n")
'''


'''
print("Welcome to Guarranty Trust Bank")
restart = "y"
chance = 3
balance = 120000
while chance >= 0:
    pin = int(input("Please Enter Your 4 Digit Pin: "))
    if pin == (1234):
        print("You Have Entered Your Pin Correctly")
        while restart not in ("n", "NO", "no", "N"):
            print("Please Press 1 To Check Balance\n")
            print("Please Press 2 To Make Withdrawal\n")
            print("Please Press 3 To Pay In\n")
            print("Please Press 4 To Return Card\n")
            option = int(input("What Would You Like To Choose? "))
            if option == 1:
                print("Your Account Balance is #", restart, "\n")
                restart = input("Would You Like To Go Back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawal = int(input("How Much Would You Like To Withdraw? \n#500/#1000/#5000/#10000/#20000"))
                if withdrawal in (500, 1000, 5000, 10000, 20000):
                    balance = balance - withdrawal
                    print("\nYour Account Balance is #", balance)
                    restart = ("Would You Like To Go Back? ")
                    if restart in ("no", "NO", "no", "N"):
                        print("Thank You.")
                        break
                elif withdrawal != (500, 1000, 5000, 10000, 20000):
                    print("Invalid Amount, Please Try Again.\n")
                    restart = "y"

                elif withdrawal == 1:
                    print(float(input("Enter Desired Amount: ")))

            elif option == 3:
                Pay_In = float(input("How Much Will You Like To Pay In? "))
                balance = balance + Pay_In
                print("Your Account Balance is #", balance)
                restart = input("Would You Like To Go Back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break

            elif option == 4:
                print("Please Wait Whilst Your Card Is Returned....\n")
                print("Thank You For Banking With Us")
                break

            else:
                print("Please Enter The Correct Number: ")
                restart = "y"

    elif pin != ("1234"):
        print("\nIncorrect Pin, Try Aagin")
        chance = chance - 1
        if chance == 0:
            print("No More Entries")
'''



print("WELCOME TO GUARRANTY TRUST BANK")
restart = ("You")
chance = 3
balance = 200000
while chance >= 0:
    pin = int(input("Enter Your 4 Digit Pin: "))
    if pin == (1234):
        print("You Entered A Correct Pin")
        while restart not in ("n", "NO", "no", "N"):
            print("Please Press 1 To Check Balance.\n")
            print("Please Press 2 To Make Withdrawal.\n")
            print("Please Press 3 To Pay In.\n")
            print("Please Press 4 To Return Card.\n")
            option = int(input("What Would You Like To Choose? "))
            if option == 1:
                print("Your Account Balance is #", balance, "\n")
                restart = input("Would You Like To Go Back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawal = float(input("How Much Would You Like To Withdraw? \n#500/#1000/#2000/#5000/#10000/#20000"))
                balance = balance - withdrawal
                print("\n Your Account Balance is #", balance)
                restart = input("Would You Like To Go Back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break

                elif withdrawal != (500, 1000, 2000, 5000, 10000, 20000):
                    print("Invalid Amount. Please Try Agin")
                    restart = "y"
                elif withdrawal == 1:
                    print("Enter Your Desired Amount")

            elif option == 3:
                Pay_In = float(input("How Much Will You Like To Pay In? "))
                print("Your Accoumt Balance is #", balance)
                resart = input("Woukld You Like To Go Back")
                if restart in ("n", 'NO', "no", "N"):
                    print("Thank You.")
                    break
            elif option == 4:
                print("Please Wait Whilst Your Card Is Returned.")
                print("Thank You For Banking With Us.")
                break

            else:
                print("You Entered An Incorrect Number. Please Try Again.")
                restart = "y"

    elif pin != ("1234"):
        print("\nInvalid Pin. Please Try Again.")
        chance = chance - 1
        if chance == 0:
            print("No More Entries.")






print("WELCOME TO ACCESSS BANK")
restart = ("Y")
chance = 3
balance = 150000
while chance >= 0:
    pin = int(input("Enter Your 4 Digit Pin: "))
    if pin == (1234):
        print("You Have Entered A Correct Pin")
        while restart not in ("n", "NO", "no", "N"):
            print("Please Press 1 To Check Balance\n")
            print("Please Press 2 To Make Withdrawal\n")
            print("Please Press 3 To Pay In\n")
            print("Please Press 4 To Return Card\n")
            option = int(input("What Would You Like To Choose? "))
            if option == 1:
                print("Your Account Balance is #", balance, "\n")
                restart = input("Would You Like To Go Back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawal = float(input("How Much Would You Like To Withdraw? \n#500/#1000/#2000/#5000/#10000/#20000"))
                balance = balance - withdrawal
                print("\nYour Account Balance is #", balance)
                restart = input("Would You Like To Go Back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break
                elif withdrawal != (500, 1000, 2000, 10000, 20000):
                    print("You Entered An Invalid Amount, Try Again")
                    restart = "y"
                elif withdrawal == 1:
                    print("Enter Your Desired Amount")

            elif option == 3:
                Pay_In = float(input("How Much Would You Like To Pay In: "))
                balance = balance + Pay_In
                print("Your Account Balance is #", balance, "\n")
                restart = input("Would You Like To Go Back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break

            elif option == 4:
                print("Please Wait Whilst Your Card Is Returned......\n")
                print("Thank You For Banking With Us.")
                break

            else:
                print("You Entered An Incorrect Number. Please Try Again")
                restart = "y"

    elif pin != ("1234"):
        print("Invalid Pin, Please Try Again.")
        chance = chance - 1
        if chance == 0:
            print("No More Entries. Thank You.")



print("WELCOME TO SKYE BANK")
restart = "Y"
chance = 3
balance = 150000
while chance >= 0:
    pin = int(input("Enter Your 4 Digit Pin: "))
    if pin == (1234):
        print("You Entered a Correct Pin")
        while restart not in ("n", "NO", "no", "N"):
            print("Please Press 1 To Check Balance\n")
            print("Please Press 2 To Make Withdrawal\n")
            print("Please Press 3 To Pay In\n")
            print("Please Press 4 To Return Card\n")
            option = int(input("What Would You Like To Choose?: "))
            if option == 1:
                print("Your Account Balance is #", balance, "\n")
                restart = input("Would You Like To Go Back?")
                if restart in ("n", "NO", "no", "n"):
                    print("Thank You")
                    break

            elif option == 2:
                option2 = ("y")
                withdrawal = float(input("How Much Would You Like To Withdraw? \n#500/#1000/#2000/#5000/#10000/#20000"))
                balance = balance - withdrawal
                print("\n Your Account Balance is #", balance)
                restart = input("Would You Like To Go Back?")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break
                elif withdrawal != (500,1000, 2000, 5000, 10000, 20000):
                    print("You Entered A Wrong Amount. Try Again")
                    restart = "y"
                elif withdrawal == 1:
                    withdtrawal = float(input("Enter Your Desired Amount: "))


            elif option == 3:
                Pay_In = float(input("How Much Would You Like To Pay In"))
                balance = balance + Pay_In
                print("Your Account Balance is #", balance, "\n")
                restart = input("Would You Like To Go Back")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You.")
                    break


            elif option == 4:
                print("Please Wait, Whilst The Card Is Returned........\n")
                print("Thank You For Banking With Us")
                break

            else:
                print("You Entered An Incorrect Number. Try Again")
                restart = "y"

    if pin != ("1234"):
        print("\nInvalid Input. Try Again")
        chance = chance - 1
        if chance == 0:
            print("No More Entries")



number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in number_grid:
    for col in row:
        print(col)




print("WELCOME TO ACCESS BANK")
restart = "Y"
chance = 3
balance = 200000
while chance >= 0:
    pin = int(input("Enter Your 4 Digit Pin: "))
    if pin == (1234):
        print("You Entered A Correct Pin.")
        while restart not in ("n", "NO", "no", "N"):
            print("Please Press 1 To Check Balance\n")
            print("Please Press 2 To Make A Withdrawal\n")
            print("Please Press 3 To Pay In\n")
            print("Please Press 4 To Return Card\n")
            option = int(input("What Would You Like To Choose? "))
            if option == 1:
                print("Your Account Balance is #", balance, "\n")
                restart = input("Would You Like To Go Back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = "y"
                withdrawal = float(input("How Much Would You Like To Withdraw? \n#500/#1000/#2000/#5000/#10000/#20000"))
                balance = balance - withdrawal
                print("\nYour Account Balance is #", balance)
                restart = input("Would You Like To Go Back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank You")
                    break
                elif withdrawal != (500, 1000, 2000, 5000, 10000, 20000):
                    print("You Have Entered An Invalid Amount. Please Try Again!")
                    restart = "y"
                elif withdrawal == 1:
                    withdrawal = float(input("Enter Your Desired Amount: "))

            elif option == 3:
                Pay_In = float(input("How Much Would You Like To Pay In: "))
                balance = balance + Pay_In
                print("Your Account Balance is #", balance, "\n")
                restart = input("Would You Like To Go Back? ")
                if restart in ("n", "NO", "no", "n"):
                    print("Thank You")
                    break

            elif option == 4:
                print("Please Wait Whilst Your Card Is Returned....")
                print("Thank You For Banking With Us.")
                break

            else:
                print("You Have Entered An Incorrect Number. Try Again!")
                resatart = "y"

    if pin != ("1234"):
        print("Invalid Password. Try Again!")
        chance = chance - 1
        if chance == 0:
            print("No More Entries")



