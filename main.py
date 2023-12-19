import random
while True:
    choice=['rock', 'paper', 'scissors']

    computer=random.choice(choice)

    player=None
    while player not in choice:
        player=input('rock or paper or scissors :').lower()

    if player==computer:
        print('computer :',computer)
        print('player :',player)
        print('Tie')
    elif player=='rock':
        if computer== 'paper':
            print('computer :',computer)
            print('player :',player)
            print('u lose')
        if computer== 'scissors':
            print('computer :',computer)
            print('player :',player)
            print('u win')    

    elif player=='paper':
        if computer== 'scissors':
            print('computer :',computer)
            print('player :',player)
            print('u lose')
        if computer== 'rock':
            print('computer :',computer)
            print('player :',player)
            print('u win')        


    elif player=='paper':
        if computer== 'scissors':
            print('computer :',computer)
            print('player :',player)
            print('u lose')
        if computer== 'rock':
            print('computer :',computer)
            print('player :',player)
            print('u win')              
    play_again =input("play agina:(yes|no) :").lower()
    if play_again !='yes':
        break
print('bye')
