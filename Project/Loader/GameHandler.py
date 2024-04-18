import io, chess.pgn, re

def gameHandler(gamestring):

    pgn = io.StringIO(gamestring)
    game = chess.pgn.read_game(pgn)

    board = game.board()
    positionList = []

    # put the positions in a list and return it
    for move in game.mainline_moves():
        positionList = positionList + [board.fen().split(' - ')[0]]
        board.push(move)

    positionList = positionList + [board.fen().split('-')[0]]

    patternWhitePlayer = re.compile(r"White \"([a-zA-Z]*?)[^a-zA-Z]")
    patternBlackPlayer = re.compile(r"Black \"([a-zA-Z]*?)[^a-zA-Z]")
    patternResult = re.compile(r"Result \"([0-2\/\-]*)\"")

    result = re.search(patternResult, gamestring)
    if result is None:
        return []

    whitePlayer = re.search(patternWhitePlayer, gamestring)

    blackPlayer = re.search(patternBlackPlayer, gamestring)

    gameLength = len(positionList)

    gameData = [result.group(1), gameLength, whitePlayer.group(1), blackPlayer.group(1), positionList]

    return gameData
