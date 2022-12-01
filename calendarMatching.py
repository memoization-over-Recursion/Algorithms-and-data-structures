#time complexity O( c1 + c2 )
#space complexity O( c1 + c2 )
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCal = updateCal(calendar1 , dailyBounds1)
    updatedCal1 = updateCal(calendar2 , dailyBounds2)
    mergedCalendar = mergeCalenders( updatedCal , updatedCal1 )
    print( mergedCalendar )
    flattenedCal = flattenCalendar( mergedCalendar )
    return getAvaliableTimes( flattenedCal , meetingDuration )

def mergeCalenders(updatedCal , updatedCal1):
    merged = []
    i , j = 0 , 0
    while( i < len( updatedCal ) and j < len( updatedCal1 ) ):
        if( updatedCal[ i ][ 0 ] < updatedCal1[ j ][ 0 ] ):
            merged.append( updatedCal[ i ] )
            i += 1
        else:
            merged.append( updatedCal1[ j ] )
            j += 1
    while( i < len( updatedCal )):
        merged.append(updatedCal[i])
        i+=1
    while( j < len( updatedCal1 )):
        merged.append(updatedCal1[j])
        j+=1
    return merged

def flattenCalendar( cal ):
    flattened = [cal[0][:]]
    for i in range( 1 , len( cal ) ):
        curMeeting = cal[i]
        prevMeeting = flattened[-1]
        currentStart , currentEnd = curMeeting
        previousStart , previousEnd = prevMeeting
        if(previousEnd >= currentStart):
            newPrevMeeting = [previousStart , max( previousEnd , currentEnd )]
            flattened[-1] = newPrevMeeting
        else:
            flattened.append(curMeeting[:])

    return flattened
    

def getAvaliableTimes( cal , dur ):
    answer = []
    for i in range( 1 , len( cal ) ):
        start = cal[ i - 1 ][ 1 ]
        end = cal[ i ][ 0 ]
        avaliableDuration = end - start
        if(avaliableDuration >= dur):
            answer.append([start , end])

    return list( map( lambda t : [minutesToTime(t[0]) , minutesToTime(t[1]) ] , answer ))
        
        
def minutesToTime( time ):
    hours = time // 60
    minutes = time % 60
    hours = str( hours )
    minutes = '0'+str(minutes) if minutes < 10 else str(minutes)
    return hours + ":" + minutes
            
def updateCal( cal , bounds ):
    calender = cal[:]
    calender.insert(0 , ["00:00" , bounds[0] ] )
    calender.append([bounds[1] , "23:59"])
    return list(map( lambda minutes : [ timeToMinutes(minutes[0]), timeToMinutes(minutes[1]) ] , calender))
    
def timeToMinutes( calenderEntry ):
    hours , minutes = list(map(int , calenderEntry.split(":")))
    return hours * 60 + minutes
    