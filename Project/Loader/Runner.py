import DataParser, GameHandler, Comparator, pickle

# pip installs used
# pip install -U numpy
# pip install -U pickle

def getWinner(game):
    # winning with black is most impressive, then winning with white, then drawing with black, then drawing with white

    if game[0] == '1-0':
        return game[2]
    else:
        return game[3]

gamelist = DataParser.getfiles(r'D:\Design\TCEC files')

# games directly played between leela and stockfish
games = []

# games played with other ais
games2 = []

for gamestring in gamelist:
    gameData = GameHandler.gameHandler(gamestring)

    if gameData == []:
        continue
    
    if ((gameData[2] == 'LCZero') and (gameData[3] == 'Stockfish')) or ((gameData[3] == 'LCZero') and (gameData[2] == 'Stockfish')):
        games = games + [gameData]
    
    elif (gameData[2] == 'LCZero') | (gameData[3] == 'LCZero'):
        games2 = games2 + [gameData]

    elif (gameData[2] == 'Stockfish') | (gameData[3] == 'Stockfish'):
        games2 = games2 + [gameData]
    

# position-game pairs, positions from games directly played between leela and stockfish
d = {}

# position-game pairs, positions from games played with other ais
d2 = {}

# position-engine pairs
pos_Engine = {}

for game in games:

    # find out if the winner of the game is leela or stockfish
    winner = getWinner(game)
    leelaFish = (winner == 'LCZero') | (winner == 'Stockfish')

    # iterating over all game positions,
    for position in game[4]:

        # if leela or stockfish win a game attribute all those positions to them
        # there is an improvement here by moving the if out of the function, but that harms readability
        if leelaFish:
            pos_Engine[position] = winner

        # also add all the positions to d, and associate them to the game, 
        # then award the position to the engine who had a more impressive game with it, by changing the d2 game pair
        # We are comparing across games between leela and stockfish where the same position was reached
        if position in d:
            winner2 = getWinner(Comparator.comparison(d[position], game))
            if (winner2 == 'LCZero') | (winner2 == 'Stockfish'):
                pos_Engine[position] = winner2

        else:
            d[position] = game

for game in games2:

    # find out if the winner of the game is leela or stockfish
    winner = getWinner(game)
    leelaFish = (winner == 'LCZero') | (winner == 'Stockfish')

    # iterating over all game positions,
    for position in game[4]:

        # if leela or stockfish win a game attribute all those positions to them
        # there is an improvement here by moving the if out of the function, but that harms readability
        if leelaFish:
            pos_Engine[position] = winner

        # also add all the positions to d2, and associate them to the game, 
        # then award the position to the engine who had a more impressive game with it, by changing the d2 game pair
        # We are comparing across games between leela or stockfish with others where the same position was reached
        if position in d2:
            winner2 = getWinner(Comparator.comparison(d2[position], game))
            if (winner2 == 'LCZero') | (winner2 == 'Stockfish'):
                pos_Engine[position] = winner2

        else:
            d2[position] = game

l=0
s=0

for k in pos_Engine:
    if pos_Engine[k] == 'LCZero':
        l+=1
    elif pos_Engine[k] == 'Stockfish':
        s+=1

print('Leela = ',l,' Stockfish = ',s)


# export this dictionary for use
with open('Loader/pos_Engine.pkl', 'wb') as f:
    pickle.dump(pos_Engine, f)

