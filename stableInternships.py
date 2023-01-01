# time complexity O( n^2 )
# space complexity O( n^2 )
def stableInternships(interns, teams):
    chosenInterns = {}
    freeInterns = list(range(len(interns)))
    currentChoiceForIntern = [0] * len( interns ) 

    teamMaps = []
    for team in teams:
        rank = {}
        for i , intern in enumerate( team ):
            rank[intern] = i
        teamMaps.append(rank)
        
    while len(freeInterns) > 0:
        internNum = freeInterns.pop()
        intern = interns[internNum]
        teamPref = intern[ currentChoiceForIntern[ internNum ] ]
        currentChoiceForIntern[internNum] += 1
        if teamPref not in chosenInterns:
            chosenInterns[teamPref] = internNum
            continue

        prevIntern = chosenInterns[teamPref]
        prevInternRank = teamMaps[teamPref][prevIntern]
        currInternRank = teamMaps[teamPref][internNum]

        if prevInternRank > currInternRank:
            freeInterns.append(prevIntern)
            chosenInterns[teamPref] = internNum
        else:
            freeInterns.append(internNum)
    return [[internNum , teamNum] for teamNum, internNum in chosenInterns.items()]
    

        
            
            
