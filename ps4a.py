# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST = "words.txt"


def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# Problem #1: Scoring a word
#


def getWordScore(word, n):
    score = 0
    for i in range(len(word)):
        for key, value in SCRABBLE_LETTER_VALUES.items():
            if key == word[i]:
                score += 1
    score = score * (len(word))
    if len(word) == n:
        score += 50
    return score


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")  # print all on the same line
    print()  # print an empty line


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#


def updateHand(hand, word):
    output = hand.copy()
    for letter in word:
        if letter in output.keys():
            output[letter] -= 1
    return output


#
# Problem #3: Test word validity
#


def isValidWord(word, hand, wordList):
    newHand = hand.copy()
    counter = 0
    if word in wordList:
        for char in word:
            if char in newHand:
                if newHand[char] >= word.count(char):
                    counter += 1
                else:
                    return False
                    break
        if counter == len(word):
            return True
    else:
        return False
    return False



#
# Problem #4: Playing a hand
#


def calculateHandlen(hand):
    n = 0
    for i in range(len(hand)):
        n += 1
    return n


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    score = 0
    word = ""
    # Keep track of the total score

    while True:
        displayHand(hand)

        word = input('Enter word, or a "." to indicate that you are finished: ')
        if input() == ".":
            print("Your total score was %s points! Please play again!" % getWordScore(word, n))
            break
        else:
            if not isValidWord(word, hand, wordList):
                print("Sorry that is not a valid word, please try again")
                print("")
            else:
                score += getWordScore(word, n)
                hand = updateHand(hand, word)
            if all(value == 0 for value in hand.values()):
                print("Run out of letters. ", end="")
                break
            print("Total score: " + str(score) + " points.")


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function

    count = 0
    n = 7

    print("Welcome to the game!")

    while True:
        command = input("Please input n if you would like to play a new hand, r to play the last hand,"
                        " and e to exit the game")
        if command == "r":
            if count == 0:
                print("You have not played a hand yet")
            else:
                hand = hand.copy(n)
                playHand(hand, wordList, n)
                count += 1

        elif command == 'n':
            hand = dealHand(n)
            playHand(hand, wordList, n)
            count += 1

        elif command == "e" or ".":
            break

        else:
            print("Invalid command")


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
