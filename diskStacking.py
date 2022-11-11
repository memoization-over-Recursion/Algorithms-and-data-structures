#time complexity O( n^2 )
#space complexity O( n )
def diskStacking(disks):
    disks.sort(key = lambda x: x[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    maxIdx = 0
    for i in range(1,len(disks)):
        current = disks[i]
        for j in range(0,i):
            other = disks[j]
            if(areValid(other , current)):
                if(heights[i] <= current[2] + heights[j]):
                    heights[i] = current[2] + heights[j]
                    sequences[i] = j
        if(heights[i] >= heights[maxIdx]):
            maxIdx = i

    return buildSeq(disks , sequences , maxIdx)
    pass

def areValid(o , c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

def buildSeq(disks , seq , id):
    sequences = []
    while(id is not None):
        sequences.append(disks[id])
        id = seq[id]
    return list(reversed(sequences))