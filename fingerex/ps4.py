# ---------------------------------------------------------------------------- # 
# -------- *** MITx course 600.1x ** Online course on edx *** ---------------- #
# ------- Introduction to Computer Science and Programming using Python ------ #
# ------------------------ [Problem Set 4] ----------------------------------- #
# ---------------------------------------------------------------------------- #
# *** Problem Set 4 ***

# -- Problem 1 --
# ---------------------------------------------------------------------------- #

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
 
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
 
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
 
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n:
        score += 50
    return score


# -- Problem 2 --
# ---------------------------------------------------------------------------- #

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    output = hand.copy()
    for letter in word:
        if letter in output.keys():
            output[letter] -= 1
    return output

# -- Problem 3 --
# ---------------------------------------------------------------------------- #

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
 
    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    output = hand.copy()
    word_check = False
    if word in wordList:
        word_check = True
 
    letter_check = set(list(word)) <= set(output.keys())
 
    for letter in word:
        if letter in output.keys():
            output[letter] -= 1
 
    value_check = all(i >= 0 for i in output.values())
    
    if word_check == True and letter_check == True and value_check == True:
        return True
    else:
        return False

# -- Problem 4 --
# ---------------------------------------------------------------------------- #

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    sum = 0
    for value in hand.values():
        sum += value
    return sum

# -- Problem 5 --
# ---------------------------------------------------------------------------- #

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
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print('Current Hand:', end=' '); displayHand(hand)     
        # Ask user for input
        guess = str(input('Enter word, or a "." to indicate that you are finished: '))        
        # If the input is a single period:
        if guess == '.':        
            # End the game (break out of the loop)
            break            
        # Otherwise (the input is not a single period):
        else:        
            # If the word is not valid:
            if isValidWord(guess, hand, wordList) == False:            
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.', '\n')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += getWordScore(guess, n)
                print('"'+guess+'"', "earned", getWordScore(guess, n), "points. Total:", score, "points", '\n')
                # Update the hand 
                hand = updateHand(hand, guess)               

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if guess == '.':
        print('Goodbye! Total score:', score, 'points.')
    else:
        print('Run out of letters. Total score:', score, 'points.') 

# -- Problem 6 --
# ---------------------------------------------------------------------------- #

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
    while True:
        user_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if user_input == 'e':
            break
        elif user_input == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif user_input == 'r':
            try:
                playHand(hand, wordList, HAND_SIZE)
            except:
              print('You have not played a hand yet. Please play a new hand first!')                           
        else:
            print('Invalid command.')

# -- Problem 7 --
# ---------------------------------------------------------------------------- #

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
 
    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.
 
    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.
 
    4) After the computer or user has played the hand, repeat from step 1
 
    wordList: list (string)
    """
    while True:
        user_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if user_input == 'e':
            break
        elif user_input == 'n':
            while True:
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif play_mode == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')            
        elif user_input == 'r':
            try:
                hand
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif play_mode == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print('Invalid command.')
            except:
                print('You have not played a hand yet. Please play a new hand first!')
        else:
            print('Invalid command.')





# *** EOF ***
# ---------------------------------------------------------------------------- #