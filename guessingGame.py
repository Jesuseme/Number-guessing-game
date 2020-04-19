import random


def main():
    def game(guess, pool):
        print("--------------------------------------------")
        print("----------------" + mode + "-------------------")
        game_mode(guess, pool)

    def game_mode(guess, pool):
        print("--------------------------------------------")
        print("Guess the number I am thinking of 1 - " + str(pool) + " Guesses : " + str(guess))
        user = int(input("--->:"))
        computer = random.randint(1, pool)
        if int(user) == int(computer):
            print("You got it right! Guesses left: " + str(guess))
            replay()
        elif int(user) > pool:
            print("That number is over the range")
            game_mode(guess, pool)
        else:
            print("That was wrong, my number was " + str(computer))
            guess -= 1
            if guess == 0:
                print("Game Over!!")
                replay()
            else:
                game_mode(guess, pool)

    def replay():
        print("----------------------------")
        print("Would you like to play again:")
        ans = input("Y/N: ")
        if ans == "y" or ans == "Y":
            main()
        elif ans == "n" or ans == "N":
            print("Good Bye")
        else:
            print("Invalid output")
            replay()

    print("----------Number--Guessing--Game------------")
    print("------------------Welcome-------------------")
    print("Select Difficulty---------------------------")
    print("------1-Easy------2-medium------3-Hard-------")
    x = input("-->:")

    if x == "1":
        mode = "Easy mode"
        pool = 10
        guess = 6
        game(guess, pool)
    elif x == "2":
        mode = "Medium mode"
        pool = 20
        guess = 4
        game(guess, pool)
    elif x == "3":
        mode = "Hard mode"
        pool = 50
        guess = 3
        game(guess, pool)
    else:
        print("please enter valid input")


main()
