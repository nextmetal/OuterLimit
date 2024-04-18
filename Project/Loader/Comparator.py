def comparison(game1, game2):
    # finding the most impressive game between game1, game2

    # if both have a win of the same color then the quicker win is more impressive
    if (game1[0] == '0-1' and game2[0] == '0-1') or (game1[0] == '1-0' and game2[0] == '1-0'):
        if game1[1] < game2[1] :
            return game1
        else:
            return game2
        
    # if only one game ends in a win, then the win is more impressive
    elif game1[0] == '0-1' and game2[0] != '0-1':
        return game1
    elif game2[0] == '0-1' and game1[0] != '0-1':
        return game1
    elif game1[0] == '1-0' and game2[0] != '1-0':
        return game1
    elif game2[0] == '1-0' and game1[0] != '1-0':
        return game1
    
    # if both games end in a draw then the longer draw is more impressive
    elif game1[0] == '1/2-1/2' and game2[0] == '1/2-1/2':
        if game1[1] > game2[1] :
            return game1
        else:
            return game2