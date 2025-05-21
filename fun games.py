def ng():
    import random
    a=random.randint(1,50)
    while True:
        x=int(input("enter a number: "))
        if x>a:
            print("guess a smaller number")
        elif x<a:
            print("guess a higher number")
        else:
            print("congratulations! you won")
            break 

def RPS():
    import random
    a=("R","P","S")
    b=random.choice(a)
    while True:
        u=input("enter your choice: ").upper()
        if (b=='R' and u=='S') or (b=='S' and u=='P') or (b=='P' and u=='R'):
            print(f"bot chose {b} and you chose {u} so the bot won")
        elif (b=='R' and u=='R') or (b=='S' and u=='S') or (b=='P' and u=='P'):
            print(f"bot chose {b} and you chose {u} so the match is a tie")
        else:
            print(f"bot chose {b} and you chose {u} so congratulations! you won")
        break
    
while True:
    print( 
    ''' fun games
    1=ng
    2=RPS
    0=quit
    ''')
    x=int(input("enter a number to play the games: "))
    if x==1:
        ng()
    elif x==2:
        RPS()
    elif x==0:
        print("you are quitting the game")
        break
    else:
        print("the game you selected is not available")        
