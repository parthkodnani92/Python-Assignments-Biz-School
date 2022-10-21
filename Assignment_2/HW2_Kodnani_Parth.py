#!/usr/bin/env python
# coding: utf-8

# * Name: Parth Kodnani 
# * Course: BUDT704 
# * Section: 0502
# * Date: 09/22/2021

# ## Basic Data Analysis Using a Deck of Cards
# 1. A game is created to perform data analysis on its results.
# 2. The game needs numeric cards with values 2 through 10.

# In[1]:


# Importing the necessary libraries

import random
import statistics


# ### Case 1
# Create a list to represent the values of all cards in the deck.

# In[13]:


# Creating the deck for basic data analysis
deck1 = [2,3,4,5,6,7,8,9,10]
deck2 = [2,3,4,5,6,7,8,9,10]
deck3 = [2,3,4,5,6,7,8,9,10]
deck4 = [2,3,4,5,6,7,8,9,10]

deck = [deck1, deck2, deck3, deck4]

print(deck)


# ### Case 2
# Determine the total number of points available in the deck.

# In[14]:


# Calculating total number of points available in the deck
sumDeck = 0

for i in deck:
    sumDeck = sumDeck + sum(i)
        
print(f'The Total Number of Points in the Deck: {sumDeck}')


# ### Case 3
# Using the deck you created, you will deal (distribute) the entire deck to two players. Create a function that will take in a card deck as a single parameter. The function will return a tuple of two lists, each with the same number of cards, randomly selected from the deck.

# #### Steps for Case 3
# 1. We create a function 'dealCards' which takes in the deck of cards as the parameter.
# 2. In the function, cards are randomly shuffled and appended to a list.
# 3. In this list, the first half elements are appended to one list and the second half elements are appended to second list.
# 4. A tuple is created and these 2 lists are added to the tuple and the tuple is returned.

# In[25]:


# Intializing 2 lists to hold the cards of the 2 players
cardList1 = []
cardList2 = []

# Creating a function to distribute all the elements randomly in the above lists
def dealCards(deck):
    openDeck = []
    for l in deck:
        random.shuffle(l) # Shuffling the cards inside individual deck
        openDeck.extend(l) # Adds all elements from a list to the main list
    random.shuffle(openDeck) # Shuffling the cards inside man list
    length = len(openDeck) 
    middle = length//2 
    cardList1 = openDeck[:middle]
    cardList2 = openDeck[middle:]
    listToTuple = (cardList1, cardList2) # Creating a tuple of the two lists
    
    return listToTuple 


# ### Case 4
# Prove the function works by invoking the function, showing the cards dealt to each player, the number of cards dealt to each player, and the sum of values of the cards dealt to each player.

# #### Steps for Case 4
# 1. When the function is called, the tuple is returned. We additionally extract the two lists individually.
# 2. We count the number of cards and the sum of cards in each list.

# In[28]:


# Invoking the function to store the two lists as separate lists and print out the tuple
listInTuple = dealCards(deck)
cardPlayer1, cardPlayer2 = dealCards(deck)
print("The Cards of the 2 Players: ", listInTuple, "\n")
print("Cards dealt to Player 1: ", cardPlayer1)
print("Cards dealt to Player 2: ", cardPlayer2, "\n")

# Printing the number of cards and sum of cards dealt 
sumTuple1 = sum(cardPlayer1)
countTuple1 = len(cardPlayer1)
print("Number of Cards dealt to Player 1 : ", countTuple1)
print("Sum of Cards dealt to Player 1: ", sumTuple1, "\n")

sumTuple2 = sum(cardPlayer2)
countTuple2 = len(cardPlayer2)
print("Number of Cards dealt to Player 2: ", countTuple2)
print("Sum of Cards dealt to Player 2: ", sumTuple2)


# ### Case 5
# 
# With each player having a set of cards, you will simulate a single game where each player will show the first two cards in their hand for a round. For each player, the two cards are summed together. The player with the higher score wins the round and gets all cards added to their set of cards. In the case of a tie, the next two first cards for each player. If a tie occurs multiple times, the cards need to be pulled until the tie is broken, or one of the players runs out of cards.

# #### Steps for Case 5
# 1. We create a function 'sumDrawPlayer' which returns the 2 cards drawn by each player and the sum of those 2 cards.
# 2. We create another function 'cardGame', which takes in the cards of the players as parameters.
# 3. The function 'sumDrawPlayer' gets called twice, for each player.
# 4. The sum of cards of both the players is compared. The player having the highest sum gets all the cards appended to their list.
# 5. Incase of a tie, we initialise an empty list 'buffer', which temporarily holds the drawn cards for that round. In the next round, whoever gets the higher score, first gets the 'buffer' cards uploaded to the list and then the drawn cars for that round. 'buffer' gets cleared then
# 6. The number of rounds are initialised to 1 and it increments after every comparison.
# 7. A while loop is present which checks the condition that if player 1 or 2 has finished their set of cards or the number of rounds played is 25, then the loop stops running.
# 7. Finally, the sum of the cards is calculated at the end of 25 rounds. The player with the highest sum wins the game.

# In[29]:


buffer = [] # Initialising a list to hold the cards during a tie

# Creating a function to provide the drawn cards and the sum of the drawn cards of players
def sumDrawPlayer(lst):
    popPlayer = [lst.pop(0), lst.pop(0)]
    sumPlayer = sum(popPlayer)
    return sumPlayer, popPlayer

def cardGame(cardPlayer1,cardPlayer2):    
    noOfRound = 1 # Initialising the number of rounds
    
    # Looping through until either player wins or 25 rounds are over
    while cardPlayer1 and cardPlayer2 and (noOfRound <= 25):
        print("Round: ", noOfRound, "\n")

        # Player 1 draws card and Sum is calculated
        sumCards1, popCards1 = sumDrawPlayer(cardPlayer1)
        print("Drawn Cards of Player 1: ", popCards1)
        print("Sum of Cards of Player 1: ",sumCards1, "\n")

        # Player 2 draws card and Sum is calculated
        sumCards2, popCards2 = sumDrawPlayer(cardPlayer2)
        print("Drawn Cards of Player 2: ", popCards2)
        print("Sum of Cards of Player 2: ", sumCards2, "\n")
        
        # Comparing the sums to check which player wins
        if sumCards1 > sumCards2:
            if buffer:
                for i in buffer:
                    cardPlayer1.extend(i) # Cards in buffer, if any, are appended to Player 1's cards 
                buffer.clear() 
            cardPlayer1.extend(popCards1 + popCards2)
            noOfRound += 1 # Round increments
            print("Cards of Player 1: ", cardPlayer1)
            print("Cards of Player 2: ", cardPlayer2, "\n\n")
        elif sumCards1 < sumCards2:
            if buffer:
                for i in buffer:
                    cardPlayer2.extend(i) # Cards in buffer, if any, are appended to Player 2's cards
                buffer.clear()
            cardPlayer2.extend(popCards1 + popCards2)
            noOfRound += 1 # Round increments
            print("Cards of Player 1: ", cardPlayer1)
            print("Cards of Player 2: ", cardPlayer2, "\n\n")
        elif sumCards1 == sumCards2:
            buffer.append(popCards1 + popCards2)  
            print("Cards of Player 1: ", cardPlayer1)
            print("Cards of Player 2: ", cardPlayer2)
            print("Cards kept aside due to draw: ", buffer, "\n\n")
            

    # Comparing the final scores of the players
    print("Number of Rounds played: ", (noOfRound-1), "\n")
    scorePlayer1 = sum(cardPlayer1)
    scorePlayer2 = sum(cardPlayer2)
    if scorePlayer1 > scorePlayer2:
        print("Winner of the Game: Player 1")
    elif scorePlayer1 < scorePlayer2:
        print("Winner of the Game: Player 2")
    elif scorePlayer1 == scorePlayer2:
        print("The Players have Equal Scores. Its a tie!")

    pass  
    


# ### Case 6
# Prove the function works by invoking it.

# In[30]:


# Invoking the function to play the game
cardGame(cardPlayer1, cardPlayer2)


# ### Case 7
# Simulate running the game 50 times. Identify the final scores for the winning and losing player in each game. Across all 50 games, create descriptive statistics (i.e., minimum, maximum, and mean) for the winning and losing scores. Identify one inference you can make from performing this analysis. 

# #### Steps for Case 7
# 1. We initialize 3 variables; 'PLAYER_1', 'PLAYER_2' and 'TIE'. While comparing the final scores of the 2 players, we return the scores of both players along with the player who won the round.
# 2. The functions, 'dealCards' and 'cardGame', are called in a for loop which runs 50 times. This gives us the final scores of each player and the winning player for 50 games.
# 3. We initialize 3 lists; 'winningScores', 'losingScores', 'tieScores'.
# 4. The winning scores gets appended to 'winningScores' and the losing scores gets appended to 'losingScores'. If there's a tie, the points of cards get appended to 'tieScores'.
# 5. We print the scores for each game now.
# 6. We create descriptive statistics(minimum, maximum, range, mean, median, mode, standard deviation and variance) to study the given data.

# In[31]:


# Initialising given variables for the return statement
PLAYER_1 = "Player1"
PLAYER_2 = "Player2"
TIE      = "Tie"

def cardGame(cardPlayer1, cardPlayer2):
    noOfRound = 1 # Initialising the number of rounds

    # Looping through until either player wins or 25 rounds are over
    while cardPlayer1 and cardPlayer2 and noOfRound <= 25:
        # Player 1 draws card and Sum is calculated
        sumCards1, popCards1 = sumDrawPlayer(cardPlayer1)

        # Player 2 draws card and Sum is calculated
        sumCards2, popCards2 = sumDrawPlayer(cardPlayer2)
        
        # Round increments
        noOfRound += 1

        # Comparing the sums to check which player wins
        if sumCards1 > sumCards2:
            if buffer:
                for i in buffer:
                    cardPlayer1.extend(i)
                buffer.clear()
            cardPlayer1.extend(popCards1 + popCards2)          
        elif sumCards1 < sumCards2:
            if buffer:
                for i in buffer:
                    cardPlayer2.extend(i)
                buffer.clear()
            cardPlayer2.extend(popCards1 + popCards2)
        else:
            buffer.append(popCards1 + popCards2)

    # Returning the final scores of the two players and the winner of that game
    scorePlayer1 = sum(cardPlayer1)
    scorePlayer2 = sum(cardPlayer2)
    if scorePlayer1 > scorePlayer2:
        print("Player 1 wins")
        return scorePlayer1, scorePlayer2, PLAYER_1
    elif scorePlayer1 < scorePlayer2:
        print("Player 2 wins")
        return scorePlayer1, scorePlayer2, PLAYER_2
    elif scorePlayer1 == scorePlayer2:
        print("Its a tie!")
        return scorePlayer1, scorePlayer2, TIE

    pass


# In[32]:


# Initialising the lists to store winning, losing and tie scores
winningScores = []
losingScores  = []
tieScores     = []

# Looping through to find the winning and losing scores for 50 games
for _ in range(50):
    cardPlayer1, cardPlayer2 = dealCards(deck)
    scores = cardGame(cardPlayer1, cardPlayer2)
    if scores[2] == PLAYER_1: 
        winningScores.append(scores[0])
        losingScores.append(scores[1])
        
    elif scores[2] == PLAYER_2:
        winningScores.append(scores[1])
        losingScores.append(scores[0])
        
    elif scores[2] == TIE:
        tieScores.append(scores[1])

    print(f'{scores}\n')
    
# Printing the winning and losing score of each game
print("Winning Score for each Game:\n", winningScores, end = "\n\n")
print("Losing Score for each Game:\n", losingScores, end = "\n\n")
print("Tie Score for each Game:\n", tieScores, end = "\n\n")

# Creating descriptive statistics on the given data
minWinScore = min(winningScores)
print("Minimum Win Score: ", minWinScore)
maxWinScore = max(winningScores)
print("Maximum Win Score: ", maxWinScore)
print("Range of the Winning Score: ", (maxWinScore - minWinScore))
meanWinScore = statistics.mean(winningScores)
print("Mean Win Score: ", meanWinScore)
medianWinScore = statistics.median(winningScores)
print("Median Win Score: ", medianWinScore)
modeWinScore = statistics.mode(winningScores)
print("Mode Win Score: ", modeWinScore)
stdDevWinScore = statistics.stdev(winningScores)
print("Standard Deviation of Win Score: ", stdDevWinScore)
varWinScore = statistics.variance(winningScores)
print("Variance of Win Score: ", varWinScore, end = "\n\n")

minLoseScore = min(losingScores)
print("Minimum Lose Score: ", minLoseScore)
maxLoseScore = max(losingScores)
print("Maximum Lose Score: ", maxLoseScore)
print("Range of the Losing Score: ", (maxLoseScore - minLoseScore))
meanLoseScore = statistics.mean(losingScores)
print("Mean Lose Score: ", meanLoseScore)
medianLoseScore = statistics.median(losingScores)
print("Median Lose Score: ", medianLoseScore)
modeLoseScore = statistics.mode(losingScores)
print("Mode Lose Score: ", modeLoseScore)
stdDevLoseScore = statistics.stdev(losingScores)
print("Standard Deviation of Lose Score: ", stdDevLoseScore)
varLoseScore = statistics.variance(losingScores)
print("Variance of Lose Score: ", varLoseScore, end = "\n\n")


# #### Observations and Analysis
# 1. We can observe that the Minimum Losing Score is 0 which is the minimum sum in the list. We can also observe that the Maximum Winning Score is 216 which is the maximum sum in the list.
# 2. The Range of the 2 Sets are almost Equal.
# 3. The Sum of the Means and Medians of the 2 Sets is equal to 216 which is the Total Points in the Deck.
# 4. The Standard Deviation of both the sets is almost equal, which means that curves of the normal distribution graphs of both the sets is almost the same.

# ### Case 8
# Determine the lowest total number of points a player started with, but still won the game. Calculate the percentage of games that had a winner who started the game with a lower total number of points compared to their opponent. Identify one inference you can make from performing this analysis. 

# #### Steps for Case 8
# 1. We store the initial values for each round. While comparing the final scores of the 2 players, we return the scores of both players along with the player who won the round and a tuple of the initial scores of both the players.
# 2. We initialise the variable 'lowestScore' to infinity to find the lowest score with which a player began but went on to win that game.
# 3. We also initialise another variable 'countWinsWithLowScore' which counts the lowest scores with which a player began but went on to win those games.
# 4. We find the percentage of the lowest scores with which a player began but went on to win those games.

# In[37]:


def cardGame(cardPlayer1, cardPlayer2):
    noOfRound = 1 # Initialising the number of rounds
    initialScores = (sum(cardPlayer1), sum(cardPlayer2)) # Storing the initial scores of each round
    
    # Looping through until either player wins or 25 rounds are over
    while cardPlayer1 and cardPlayer2 and noOfRound <= 25:
        # Player 1 draws card and Sum is calculated
        sumCards1, popCards1 = sumDrawPlayer(cardPlayer1)

        # Player 2 draws card and Sum is calculated
        sumCards2, popCards2 = sumDrawPlayer(cardPlayer2)
        
        # Round increments
        noOfRound += 1

        # Comparing the sums and checking which is greater
        if sumCards1 > sumCards2:
            if buffer:
                for i in buffer:
                    cardPlayer1.extend(i)
                buffer.clear()
            cardPlayer1.extend(popCards1 + popCards2)          
        elif sumCards1 < sumCards2:
            if buffer:
                for i in buffer:
                    cardPlayer2.extend(i)
                buffer.clear()
            cardPlayer2.extend(popCards1 + popCards2)
        else:
            buffer.append(popCards1 + popCards2)

    # Returning the initial score, final scores of the two players and the winner of that game
    scorePlayer1 = sum(cardPlayer1)
    scorePlayer2 = sum(cardPlayer2)
    if scorePlayer1 > scorePlayer2:
        return scorePlayer1, scorePlayer2, PLAYER_1, initialScores
    elif scorePlayer1 < scorePlayer2:
        return scorePlayer1, scorePlayer2, PLAYER_2, initialScores
    elif scorePlayer1 == scorePlayer2:
        return scorePlayer1, scorePlayer2, TIE, initialScores

    pass


# In[38]:


lowestScore = float('inf') # Initialising the variable to infinity to find the lowest score
countWinsWithLowScore = 0
noOfRounds = 50

for _ in range(50):
    cardPlayer1, cardPlayer2 = dealCards(deck)
    scores = cardGame(cardPlayer1, cardPlayer2)
    if scores[2] == PLAYER_1: 
        # Checking lowest score of Player 1 
        if lowestScore > scores[3][0]:
            lowestScore = scores[3][0]
            
        # Checking initial scores of Player 1
        if scores[3][0] < scores[3][1]:
            countWinsWithLowScore += 1
            
    elif scores[2] == PLAYER_2:
        # Checking lowest score of Player 2
        if lowestScore > scores[3][1]:
            lowestScore = scores[3][1]
        
        # Checking initial scores of Player 2
        if scores[3][1] < scores[3][0]:
            countWinsWithLowScore += 1
            
    elif scores[2] == TIE:
         pass
    
percentage = (countWinsWithLowScore / noOfRounds) * 100


print("Minimum Score a Player started with but still Won the Game: ", lowestScore, "\n")
print(f'Number of Scores which started at a Lower Score but Won the Game: {countWinsWithLowScore}')
print(f'Percentage of Scores which started at a Lower Score but Won the Game: {percentage:.2f}%\n')


# #### Analysis and Observation
# 1. We can observe that the minimum score a player can start with but still win the game is always less than 108.
# 2. When the function is run multiple times, trend shows that the Percentage of scores which started at a Lower Score but Won the Game is usually below 30%, meaning usually there are about 15 games in which player starting with a lower score goes on to win the round.

# "I pledge on my honor that I have not given nor received any unauthorized assistance on this assignment."
# #### --Parth Kodnani
