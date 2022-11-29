#time complexity O( ((2n)!) / (n+1)!(n)!)
#space complexity O( ((2n)!) / (n+1)!(n)!)
def generateDivTags(numberOfTags):
    answer = []
    generate(numberOfTags , numberOfTags , "" , answer)
    return answer

def generate(open , close , current , answer):
    if(open > 0):
        newPr = current + "<div>"
        generate(open-1 , close , newPr , answer)

    if( open < close ):
        newPr = current + "</div>"
        generate(open , close-1 , newPr , answer)

    if(close == 0):
        answer.append(current)
    
