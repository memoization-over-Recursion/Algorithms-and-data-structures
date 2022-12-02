#time complexity O( n )
#space complexity O( d )
def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo( topManager , reportOne , reportTwo ).l
    
def getOrgInfo(top , one , two):
    numOfReports = 0
    for dReports in top.directReports:
        orgInfo = getOrgInfo(dReports , one , two)
        if orgInfo.l is not None:
            return orgInfo
        numOfReports += orgInfo.n
        
    if top == one or top == two:
        numOfReports += 1
    lowestCommon = top if numOfReports == 2 else None

    return OrgInfo( lowestCommon , numOfReports )

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

class OrgInfo:
    def __init__(self , l , n):
        self.l = l
        self.n = n