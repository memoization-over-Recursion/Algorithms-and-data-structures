# time complxity O( v + e )
# space complexity O( v )
def degreesOfSeparation(friendsLists, personOne, personTwo):
    d1 = getDegreeOfSperation(friendsLists , personOne )
    d2 = getDegreeOfSperation(friendsLists , personTwo )
    dOver6One = getDOSOverSix( friendsLists , d1 )
    dOver6Two = getDOSOverSix( friendsLists , d2 )

    if dOver6One == dOver6Two:
        return ""

    return personOne if dOver6One < dOver6Two else personTwo

def getDegreeOfSperation(friends , f ):
    d = {}
    v = {}
    que = [{"person" : f , "degree" : 0}]
    while len(que) > 0:
        p = que.pop(0)
        person , degree = p["person"] , p["degree"]
        d[person] = degree
        for friend in friends[person]:
            if friend in v:
                continue
            v[friend] = True
            que.append( {"person" : friend , "degree" : degree + 1 })
    for person in friends:
        if person not in v:
            d[person] = float("inf")
    return d

def getDOSOverSix( friends , deg ):
    num = 0
    for person in friends:
        if deg[person] > 6:
            num += 1
    return num
        