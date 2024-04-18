piece_Num = {'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6, 'p': -1, 'n': -2, 'b': -3, 'r': -4, 'q': -5, 'k': -6, 'E' : 0}
move_Num = {'w' : 1, 'b' : -1}
square_Num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


def pos2NPos(position):
    newPos = []
    fenList = position.split()

    # this takes care of the 64 squares of the board
    for char in fenList[0]:
        if char.isalpha():
            newPos = newPos + [(piece_Num[char]/6)]
        elif char.isdigit():
            for x in range(int(char)):
                newPos = newPos + [0]
    
    # this describes whose move it is
    newPos = newPos + [move_Num[fenList[1]]]

    
    # since length of our output list is static, but length of our input 
    # string is variable, we need to fill appropriate list entries with zeroes

    if len(fenList) == 3:

        
        # handling fenList[2] is en passant target square, only en passant target 
        # square can have a digit in it (as opposed to castling indicators)
        if any(char.isdigit() for char in fenList[2]):
            
            # if this is reached we must place 4 zeroes for the castling nodes
            newPos = newPos + 4*[0]

            for char in fenList[2]:
                if char.isaplha():
                    newPos = newPos + [square_Num[char]]
                    surplus-=1
                elif char.isdigit():
                    newPos = newPos + [9-int(char)]
                    surplus-=1
        
        # this describes which castling manoeuvers are still possible
        # and keeps track of all the castling manoevers
        else:
            surplus = 4

            # if this is reached we must populate 4 nodes for the
            # castling manoeuvers, and place 2 zeroes at the end
            for char in fenList[2]:

                newPos = newPos + [piece_Num[char]]
                surplus-=1
        
            newPos = newPos + (surplus+2)*[0]

    elif len(fenList) == 4:

        surplus=6
        
        # this describes which castling manoeuvers that are still possible
        for char in fenList[2]:
            newPos = newPos + [piece_Num[char]]
            surplus-=1

        # this describes the square that en passant will happen on
        # coordinates have been shifted to the 4th quadrant to match dataset
        # this is a convention for fen; first we take x coordinate, then y
        # For any rank, squares begin from the first file and go to the eighth. (x: 1-8)
        # For any file, squares begin from from the eighth rank and end with the first. (y: 1-8)
        for char in fenList[3]:

            # for the x coordinate
            if char.isaplha():
                newPos = newPos + [square_Num[char]]
                surplus-=1

            # for the y coordinate
            else:
                newPos = newPos + [9-int(char)]
                surplus-=1
        
        newPos = newPos + surplus*[0]
    
    else:
        newPos = newPos + [0, 0, 0, 0, 0, 0]

        

    # print(newPos)
    # print(len(newPos))

    return newPos