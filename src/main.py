import random
import webbrowser

from words import words

url = "https://github.com/RajParsaniya"


def main():
    print('\n\n-----------------------------------------------------------------------')
    print('| Options                 | Use                                       |')
    print('-----------------------------------------------------------------------')
    print('| (1) Start New Game      | To start a new game.                      |')
    print('| (2) About Developer     | To see information about the developer    |')
    print('| (3) Game Rule           | To Know rules of the game.                |')
    print('| (4) Exit                | To Quit/Exit the game.                    |')
    print('-----------------------------------------------------------------------\n')

    entered_choice = input('Enter your choice : ')

    if entered_choice == '1':
        start_game()
    elif entered_choice == '2':
        about()
    elif entered_choice == '3':
        rule()
    elif entered_choice == '4':
        quit_game()
    else:
        main()


def start_game():
    name = input("\nEnter your name : ")
    print("\nAll the best", name)

    word = random.choice(words)
    print('\n--------------------------')
    print("|  Guess the characters  |")
    print('--------------------------\n')
    guesses = ""

    turns = 6

    while turns > 0:

        failed = 0

        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")

                failed += 1

        if failed == 0:
            print("\n\n-------------------")
            print("|     You Win     |")
            print("-------------------")
            print("\nThe Word Is : ", word)
            main()
            break

        guess = input("\n\nGuess The Character: ")
        guesses += guess

        if guess not in word:
            turns -= 1
            print("\nWrong")
            print("You Have", +turns, "More Guesses\n")
            if turns == 0:
                print("\n\n--------------------")
                print("|     You Lose     |")
                print("--------------------")
                print("\nThe Word Is : ", word)
                main()


def rule():
    print('\n\n---------------------------')
    print('|        Game Rule        |')
    print('---------------------------\n')
    print('-> The rules of Hangman are fairly simple')
    print('-> It is a traditional two or more player game where one player thinks of a word and the others tries to '
          'guess it by trying to find each of the missing letters.')
    print(
        '-> If the puzzle has not been solved after 7 guesses, the player trying to guess the word has lost the game.')
    main()


def about():
    print('\n\n---------------------------------')
    print('|        About Developer        |')
    print('---------------------------------\n')
    print('-> Design By Raj Parsaniya')

    key_press = input('-> Do you want to explore more projects (Y/N) : ')

    if key_press == 'Y' or key_press == 'y':
        webbrowser.open_new_tab(url)
    else:
        main()


def quit_game():
    exit()


if __name__ == '__main__':
    main()
