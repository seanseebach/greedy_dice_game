def main():

    import random
    import time

    rules = """
The game is called Greedy.

The rules are simple:
Players go around in a circle rolling 2 dice with the goal of "locking in" at over 100 points.

Your score is the sum of your dice roll.
Once you have a score you can either keep rolling or lock in your score.
When you lock in a score you start at that score on the next round.

If you roll a 1, that turn''s rolls do not count and you go back to previous score.
If you roll two 1''s, then your turn is over and you go back to a 0 score.
If you roll doubles that are not 1''s, then you double the sum and add it to your score.

Once a player has chosen to lock in at over 100, the final round starts.
After that, everyone gets one turn to try to beat the winner.
The player with the most points after this round wins!

Are you ready to start playing Greedy?  (Press Enter)"""

    print(rules)

    input()
    # Gets the player count and players
    print('How many people will be playing Greedy? (Type a number and press Enter)')
    playerCount = input()
    #playerCount = 2
    print(str(playerCount) + ' players will be playing.  What are their names?  (Type each name, followed by pressing Enter)')
    playerCount = int(playerCount)
    playerList = []
    for i in range(0,playerCount):
        playerName = input()
        playerList.append(playerName)
    #playerList = ['Sean','Devin']
    playerDict = {i : 0 for i in playerList}
    print('The list of players is: ' + str(playerList)+'\nEveryone starts with a score of 0.')
    print('\nLet''s Play Greedy! (Press Enter)')
    #imports random for dice

    min = 1
    max = 6

    over100LockIn = 'no'
    while over100LockIn == 'no': #the main game loop.  if all players scores are less than 100, game continues
        for player in playerDict:
            print('\n'+player + ', it''s your turn!  Your current score is ' + str(playerDict[player]) + '.')
            print('Press Enter to roll dice.')
            input()
            rollAgain = 'y'
            turnOver = 'n'
            turnScore = 0
            while (rollAgain == 'y' or rollAgain == '') and turnOver == 'n':
                print('Rolling dice...\n')
                time.sleep(1)
                roll1 = random.randint(min,max)
                roll2 = random.randint(min,max)
                print(str(roll1) + ', ' + str(roll2))
                if roll1 == 1 and roll2 == 1: #rolling snake eyes
                    print('Finish your beer!  Your turn is over.')
                    turnScore = 0
                    playerDict[player] = 0
                    turnOver = 'y'
                    break
                elif roll1 == 1 or roll2 == 1: #rolling one 1
                    print('Your turn is over.')
                    turnScore = 0
                    turnOver = 'y'
                    break
                elif roll1 == roll2: #rolling doubles
                    roll1 = roll1*2
                    roll2 = roll2*2
                    turnScore = turnScore + roll1 + roll2
                    print('Doubles!  Your current score is ' + str(playerDict[player] + turnScore) + ', but YOU. HAVE. TO ROLL AGAIN.')
                    print('Ready? (Press Enter)')
                    input()
                    #rollAgain = 'y'
                elif roll1 != roll2: #normal roll
                    turnScore += roll1 + roll2
                    print('Current score is ' + str(playerDict[player] + turnScore) + '... Roll again? (Press Enter to roll again, Type ''n'' and press enter to lock in score)')
                    rollAgain = input() #decide to end turn or not
            playerDict[player] += turnScore
            print('You are locked in at: ' + str(playerDict[player]))
            print('The current scores are: ' + str(playerDict))
            print('Press Enter to continue.')
            input()
            if playerDict[player] > 100:
                over100LockIn = 'yes'
                currentWinner = player
                currentHighScore = playerDict[player]
                print(player + ' has locked in at ' + str(playerDict[player]) + '!')
                break
    print('This means that we are going into the final round!')
    print('The current scores are: ' + str(playerDict))
    print('Ready for the final round? (Press Enter)')
    input()

    for player in set(playerDict) - {currentWinner}:  #game loop after someone has locked in over 100
        print(player + ', it''s your turn!  Your current score is ' + str(playerDict[player]) + ' and the number to beat is ' + str(currentHighScore) + '.')
        turnScore = 0
        rollAgain = 'y'
        turnOver = 'n'
        while (rollAgain == 'y' or rollAgain == '') and turnOver == 'n':
            print('Press Enter to roll.')
            input()
            print('Rolling dice...')
            time.sleep(1)
            roll1 = random.randint(min,max)
            roll2 = random.randint(min,max)
            print(str(roll1) + ', ' + str(roll2))
            if roll1 == 1 and roll2 == 1: #rolling snake eyes
                print('Finish your beer!')
                turnScore = 0
                playerDict[player] = 0
                turnOver = 'y'
                break
            elif roll1 == 1 or roll2 == 1: #rolling one 1
                print('Turn over')
                turnScore = 0
                turnOver = 'y'
                break
            elif roll1 == roll2: #rolling doubles
                roll1 = roll1*2
                roll2 = roll2*2
                turnScore = turnScore + roll1 + roll2
                print('Doubles!  Your current score is ' + str(playerDict[player] + turnScore) + ', but YOU. HAVE. TO ROLL AGAIN.')
                print('Ready?')
                input()
                rollAgain = 'y'
            elif roll1 != roll2: #normal roll
                turnScore += roll1 + roll2
                print('Current score is ' + str(playerDict[player] + turnScore) + '... Roll again? (y/n)')
                rollAgain = input() #decide to end turn or not
        playerDict[player] += turnScore
        if(playerDict[player] > currentHighScore):
            currentHighScore = playerDict[player]
            currentWinner = player
            print(player + ' is the new current winner with ' + str(playerDict[player]) + ' points.\n')


    print('The game is over!\n' + currentWinner + ' wins with ' + str(currentHighScore) + ' points!')
    
if __name__ == "__main__":
    main()
