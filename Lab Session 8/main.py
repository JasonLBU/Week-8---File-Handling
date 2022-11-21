if __name__ == "__main__":
    matches = []
    f = open("matches.txt", "r")
    for line in f:
        splitlist = line.split(" ") #split into 4 element lists
        if len(splitlist) != 4:
            print("[Error with match data]:", line, end="")
            continue
        try:
            splitlist[2] = int(splitlist[2])
            splitlist[3] = int(splitlist[3])
        except ValueError:
            print("[Invalid score]:",line,end="")
            continue
        matches.append(splitlist)
    f.close()
    print("R E S U L T S")
    HighestScore = 0
    HighestScoreTeam = ""
    for match in matches:
        homeTeam = match[0]
        awayTeam = match[1]
        homeScore = match[2]
        awayScore = match[3]

        if homeScore >  HighestScore:
            HighestScore = homeScore
            HighestScoreTeam = homeTeam
        if awayScore > HighestScore:
            HighestScore = awayScore
            HighestScoreTeam = awayTeam

        print(homeTeam," ",homeScore," : ",awayTeam," ",awayScore)
    print(f"Highest score: {HighestScore}")
    print(f"Highest score team: {HighestScoreTeam}")