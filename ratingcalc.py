restart="Y"
while restart=="Y" or "y":
    #Asks for the necessary values
    playeronerawS=input("Insert the rating of player one: ")
    playertworawS=input("Insert the rating of player two: ")
    winnerraw=input("Insert the rating of the player who won. If draw, input 0: ")
    
    #Converts necessary values to floats
    playeronerawF=float(playeronerawS)
    playertworawF=float(playertworawS)
    winner=float(winnerraw)
    
    #Switches the ratings to satisfy the higher/lower part of the formula
    if playeronerawF>playertworawF:
      playerhigh=playeronerawF
      playerlow=playertworawF
     
    if playertworawF>=playeronerawF:
      playerhigh=playertworawF
      playerlow=playeronerawF
    
    #Establishes the difference between the two ratings and the “m” value
    d=(playerhigh-playerlow)
    m=0.025
    
    #Calculates the possible rating increases/decreases of different outcomes
    HW=10-(d*m)
    HWL=-HW
    HD=-d*m
    LD=d*m
    LW=(d*m)+10
    LWH=-LW
    
    #Defines maximum and minimum rating changes for each result
    if HW < 0.1:
        HW = 0.1
    if HW > 19.9:
        HW = 19.9
       
    if HWL > -0.1:
      HWL = -0.1
    if HWL < -19.9:
      HWL = -19.9
     
    if HD > -0.1:
      HD = 0
    if HD < - 4.9:
      HD = -4.9
    
    if LD < 0.1:
      LD = 0
    if LD > 4.9:
      LD = 4.9
     
    if LW < 0.1:
        LW = 0.1
    if LW > 19.9:
        LW = 19.9
       
    if LWH > -0.1:
      LWH = -0.1
    if LWH < -19.9:
      LWH = -19.9
    
    
    #Changes the ratings based on the rating decreases/increases
    if winner == 0:
        hfinalr=playerhigh+HD
        lfinalr=playerlow+LD
    elif winner == playerhigh:
        hfinalr = playerhigh+HW
        lfinalr = playerlow+HWL
    elif winner == playerlow:
        hfinalr = playerhigh+LWH
        lfinalr = playerlow+LW
     
    #Converts the numbers into strings and rounds them
    hfinalr=round(hfinalr, 1)
    lfinalr=round(lfinalr, 1)
       
    playerhi=str(playerhigh)
    playerlo=str(playerlow)
    hfinal=str(hfinalr)
    lfinal=str(lfinalr)
     
     
    #Sends out the new ratings!
    print(f"The player's rating that was {playerhi} is now rated {hfinal}!")
    print(f"The player's rating that was {playerlo} is now rated {lfinal}!")
    restart=input("Type Y if you would like to calculate again: ")
