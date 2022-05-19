def determine_game_winner(computer, human,  number_of_gesture):
    i = 0
    ii = 0
    if(computer==human):
        return(TIE)
    winners = {
      "column 1": [ROCK, PAPER, SCISSORS,SPOCK,LIZARD,AIR,FIRE,HUMAN,GUN,WOLF,DEVIL],
      "column 2": [SCISSORS, LIZARD, FIRE, HUMAN, WOLF,
                   ROCK, SPOCK, AIR, GUN, DEVIL,
                   PAPER, LIZARD, AIR, HUMAN, WOLF,
                   ROCK, SCISSORS, FIRE, GUN, DEVIL,
                   PAPER, SPOCK, AIR,GUN, DEVIL,
                   ROCK, SPOCK, FIRE, GUN, DEVIL,
                   PAPER, SPOCK, LIZARD, AIR, WOLF,
                   ROCK, SCISSORS, FIRE, HUMAN, WOLF,
                   PAPER, SPOCK, LIZARD, AIR, DEVIL,
                   ROCK, SCISSORS, FIRE, HUMAN, GUN]
    }
    df = pd.DataFrame(winners, columns = ['column 1, column 2'])
    for ind in df.index:
        for i in range(number_of_gesture):
            if (computer == winners[i][0]):
                for ii in range((number_of_gesture+1)//2-1):
                    if (human == winners[i][ii]):
                        return (COMPUTER)               
            return (PLAYER)