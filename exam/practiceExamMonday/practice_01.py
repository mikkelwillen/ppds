import random

def roll_dice(times, cheat = 0):
    score = 0
    for i in range(times):
        score += random.randint(1, 6)
    if (cheat == 1):
        score += 5
    return "score is", score

top_hits = [['Pos', 'Song', 'Artist', 'Peak'],['1', 'AS IT WAS', 'HARRY STYLES', '1'], ['2', 'BAD HABITS', 'ED SHEERAN', '1'], ['3', 'PERU', 'FIREBOY DML & ED SHEERAN', '2'], ['4', 'GO', 'CAT BURNS', '2'], ['5', 'SHIVERS', 'ED SHEERAN', '1'], ['6', 'RUNNING UP THAT HILL', 'KATE BUSH', '1'], ['7', 'HEAT WAVES', 'GLASS ANIMALS', '5'], ['8', 'WHERE ARE YOU NOW', 'LOST FREQUENCIES/CALUM SCOTT', '3'], ['9', 'AFRAID TO FEEL', 'LF SYSTEM', '1'], ['10', 'SEVENTEEN GOING UNDER', 'SAM FENDER', '3'], ['11', "WE DON'T TALK ABOUT BRUNO", 'GAITAN/CASTILLO/ADASSA/FELIZ', '1'], ['12', 'MAKE ME FEEL GOOD', 'BELTERS ONLY FT JAZZY', '4'], ['13', 'COLD HEART', 'ELTON JOHN & DUA LIPA', '1'], ['14', 'STARLIGHT', 'DAVE', '1'], ['15', 'GREEN GREEN GRASS', 'GEORGE EZRA', '3'], ['16', 'WHERE DID YOU GO', 'JAX JONES FT MNEK', '7'], ['17', 'ABCDEFU', 'GAYLE', '1'], ['18', 'BABY', 'AITCH/ASHANTI', '2'], ['19', 'ABOUT DAMN TIME', 'LIZZO', '3'], ['20', "I AIN'T WORRIED", 'ONEREPUBLIC', '3'], ['21', 'CRAZY WHAT LOVE CAN DO', 'DAVID GUETTA/HILL/HENDERSON', '5'], ['22', 'EASY ON ME', 'ADELE', '1'], ['23', 'DOWN UNDER', 'LUUDE FT COLIN HAY', '5'], ['24', 'B.O.T.A. (BADDEST OF THEM ALL)', 'ELIZA ROSE/INTERPLANETARY', '1'], ['25', "I'M GOOD (BLUE)", 'DAVID GUETTA & BEBE REXHA', '1'], ['26', 'LAST LAST', 'BURNA BOY', '4'], ['27', 'ANOTHER LOVE', 'TOM ODELL', '10']]

def tranpose_list():
    new_list = [[0]*len(top_hits)]*len(top_hits[0])
    for item in range(len(top_hits)):
        for subitem in range(len(top_hits[0])):
            new_list[subitem][item] = top_hits[item][subitem]
    return new_list