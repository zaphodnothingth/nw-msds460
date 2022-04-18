import time
import random
from deuces import Card, Deck, Evaluator
import numpy as np

p = 4 # number of players

deck = Deck()
evaluator = Evaluator()

epochs = 10

hand_count = []

for e in range(epochs):
    n_min = 100 # min number of games to play
    n = 0 # number of games played
    wins = [0]*p
    avg_std = 1000

    while n < n_min or (abs(avg_std-.25))/.25 > .5:
        board = deck.draw(5)

        hands = []
        for i in range(p):
            hands.append(deck.draw(2))
        winner = evaluator.hand_summary(board, hands)
        wins[winner] += 1
        
        deck.shuffle()
        n += 1
        avg_std = np.std(wins)/np.sqrt(n)
        if n % 10000 == 0:
            print('games elapsed: ', n, '  - fairness: ', abs(avg_std-.25)/.25)
            print('\t', wins)
        
    print('\n\n\n epoch: ', e)
    print(n)
    print(wins)
    print(avg_std)
    
    hand_count.append(n)


print("average hands to fairness", np.mean(hand_count))