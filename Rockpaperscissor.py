from random import randint

#list of options
m=['Rock','Paper','Scissors']

#Random play to computer
comp=m[randint(0,2)]

player1=False

while player1==False:
    player1=input("Choose 'Rock', 'Paper', 'Scissors':- ")
    
    if player1==comp:
        print("It's a Tie")
        
    elif player1=='Scissors':
        if comp=='Rock':
            print("You lose", comp , "beats", player1)
        else:
            print("You Win", player1, "over", comp)

    elif player1=='Paper':
        if comp=='Scissors':
            print("You lose", comp , "beats", player1)
        else:
            print("You Win", player1, "over", comp)

    elif player1=='Rock':
        if comp=='Paper':
            print("You lose", comp , "beats", player1)
        else:
            print("You Win", player1, "over", comp)

    else:
        print("It's not a valid play. check input")

#if we set the player1 as False the game will go in infinite loop
    player1==True
    comp=m[randint(0,2)]
