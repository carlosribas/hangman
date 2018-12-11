import random

SCORES = []


class Hangman:

    def __init__(self):
        print("#######################################")
        print("# The Engineering Challenge - 3D Hubs #")
        print("#######################################\n")

        get_input = raw_input("Type 1 to play, 2 to check your highest score, or any other entry to exit: ")
        if get_input == '1':
            self.play_game()
        elif get_input == '2':
            print("")
            if SCORES:
                print("Your highest score: %s" % max(SCORES, key=int))
                self.__init__()
            else:
                print("You have not played yet!\n")
                self.__init__()
        else:
            exit()

    def play_game(self):
        guesses = 0
        letters_used = ""
        score = 50
        word_options = ["3dhubs", "marvin", "print", "filament", "order", "layer"]
        selected_word = random.choice(word_options)
        hide_word = [" _ "] * len(selected_word)

        print("This word has %s letters. Try to guess!" % len(selected_word))
        self.the_hangman_picture(guesses)
        print("".join(hide_word) + "\n")

        while guesses < 6:
            guess = raw_input("Guess a letter: ")
            print("")

            if guess in selected_word and guess not in letters_used:
                print("Good guess!")
                letters_used += guess + " "
                self.the_hangman_picture(guesses)
                print(" " + self.game_update(guess, selected_word, hide_word, score))
                print("Letter(s) used: " + letters_used + "\n")
            elif guess not in selected_word and guess not in letters_used:
                print("Ops, try again!")
                guesses += 1
                letters_used += guess + " "
                score -= 10
                self.the_hangman_picture(guesses)
                print(" " + "".join(hide_word))
                print("Letter(s) used: " + letters_used + "\n")
            else:
                print "Choose a different letter! \n"

    def the_hangman_picture(self, guesses):
        print("________      ")
        print("|      |      ")

        if guesses == 1:
            print("|      0      ")
            print("|      |      ")
            print("|             ")
            print("|             ")

        elif guesses == 2:
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")

        elif guesses == 3:
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")

        elif guesses == 4:
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")

        elif guesses > 4:
            print("|      0      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
            print("Game over!\n")
            self.__init__()

        else:
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")

    def game_update(self, guess, selected_word, hide_word, score):
        i = 0

        while i < len(selected_word):
            if guess == selected_word[i]:
                hide_word[i] = guess
                i += 1
            else:
                i += 1

        result = "".join(hide_word)

        if result == selected_word:
            SCORES.append(score)
            print("##################################################")
            print("# CONGRATULATIONS!                                ")
            print("# You got it right, the word was '%s'.            " % result)
            print("# Your total score was: %s                        " % score)
            print("##################################################\n")
            self.__init__()
        else:
            return result


start_game = Hangman()
