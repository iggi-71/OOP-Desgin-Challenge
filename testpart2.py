import random
from words import word_list_cs
from words import word_list_nfl


# def get_word():     #selects random number that is from the words file and is turned to all uppercase
#     word = random.choice(word_list_cs)
#     return word.upper()



# this is the host of the game
class Host:
    def __init__(self, name, day): 
        self.name = name
        self.day = day

    def greet(self):    #greet method to greet the user
        print("Hello my name is " + hostt + ", and I'm your Host. We welcome you on a nice " + days)
        print("Let's play Hangman!")

    def changeHost(self, name):     #modify the name attribute
        num = random.randint(1, 2)
        if num == 1:
            name = "Steve"
        elif num == 2:
            name = "Betty"
        return name

    def changeDay(self, day):     #modify the day attribute
        num = random.randint(1, 2)
        if num == 1:
            day = "Saturday"
        elif num == 2:
            day = "Sunday"
        return day

host = Host("Steve", "Sunday")
hostt = Host("iggi", 10).changeHost("steve")

day = Host("Steve", "Sunday")
days = Host("iggi", 10).changeDay("friday")



class Player:
    def __init__(self, name, topic, score): 
        self.name = name
        self.topic = topic
        self.score = score

    def highScore(self, score):
        print("High score is " + str(score))

    def selectTopic(self, topic):
        select = input("would you the topic to be about: \n 1. Computer Science \n 2. NFL Players \n Input Number Here: ")
        if select == 1:
            topic = word_list_cs[0]
        elif select == 2:
            topic = word_list_nfl
        else:
            topic = word_list_cs[0]
        return topic


p1 = Player("iggi", "cs", 2)

'''
def get_word():     #selects random number that is from the words file and is turned to all uppercase
    word = random.choice(word_list_cs)
    return word.upper()
'''


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:    #only runs if the amount of tries is greater than 1
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:    #this is if you already guess the letter
                print("You already guessed the letter", guess)
            elif guess not in word:     #if the letter guessed is not in the list
                print(guess, "is not in the word.")
                tries -= 1      #you get 6 tries if you guess a letter that is not in the word it subtractes a 1
                guessed_letters.append(guess)   #the guess is then added to words guessed list
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                """,
                # head, torso, both arms, and one leg
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                """,
                # head, torso, and both arms
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |      
                    -
                """,
                # head, torso, and one arm
                """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -
                """,
                # head and torso
                """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                """,
                # head
                """
                    --------
                    |      |
                    |      O
                    |    
                    |      
                    |     
                    -
                """,
                # initial empty state
                """
                    --------
                    |      |
                    |      
                    |    
                    |      
                    |      
                    -
                """
    ]
    return stages[tries]


def main():
    # p1.selectTopic("cs")
    word = str(Player("iggi", "10", 0).selectTopic("cs"))
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = str(Player("iggi", "10", 0).selectTopic("cs"))
        play(word)


if __name__ == "__main__":
    p1.highScore(0)
    host.greet()
    main()