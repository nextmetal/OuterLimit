import numpy, pickle, Pos2NPos, Mirror

# pip installs used
# pip install -U numpy
# pip install -U pickle

with open('Loader/pos_Engine.pkl', 'rb') as f:
    pos_Engine = pickle.load(f)

posN_Set_X = numpy.empty((len(pos_Engine.keys())*2, 71))
engine_Set_Y = numpy.empty(len(pos_Engine.keys())*2)

npos = 0
# ln = 0

for position in pos_Engine.keys():

    '''
    ---> Diagnosis code

    print(position)

    l = Pos2NPos.pos2NPos(position)

    if len(l)!=71:
        ln += 1

    print(len(l))
    print(ln)
    print(l)
    
    '''

    # posList is the fen position converted to a list of numbers
    posList = numpy.array(Pos2NPos.pos2NPos(position))

    posN_Set_X[npos] = posList
    
    # note in this classification function we will use 1 for stockfish and 0 for leela  
    if pos_Engine[position] == 'Stockfish':
        engine_Set_Y[npos] = 1
    else:
        engine_Set_Y[npos] = 0
    
    print(npos + 1)
    print()
    npos += 1

    # posList2 is the vertically flipped version of posList 
    posList2 = numpy.array(Mirror.mirror(posList))
    
    posN_Set_X[npos] = posList2
    
    # note in this classification function we will use 1 for stockfish and 0 for leela  
    if pos_Engine[position] == 'Stockfish':
        engine_Set_Y[npos] = 1
    else:
        engine_Set_Y[npos] = 0

    print(npos + 1)
    print()
    npos += 1

# export these arrays to numpy for use
numpy.save('posN_Set_X.npy', posN_Set_X)
numpy.save('engine_Set_Y.npy', engine_Set_Y)