# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(Y, A, B, W):
    # write your code in Python 2.7
    response = 0
    leapYear = (Y%4 == 0)
    daysDic = {"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6}
    monthDic = { 1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    #monthDic = ["null", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    maxDaysofMonth = { "January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
    if leapYear:
        maxDaysofMonth = { "January":31, "February":29, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
    monthDic2 = { "January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    actualDate = ( monthDic2[A], 1)
    weekDay = getDayofTheWeek(actualDate, W, daysDic,monthDic, maxDaysofMonth)
    if weekDay != 0:
        actualDate = getNextSunday(actualDate, weekDay, maxDaysofMonth, monthDic)
    while actualDate[0] <= monthDic2[B]:
        actualDate = getNextSaturday(actualDate, 0, maxDaysofMonth, monthDic)
        if actualDate[0] <= monthDic2[B]:
            response +=1
        actualDate = getNextSunday(actualDate, 6, maxDaysofMonth, monthDic)
    return response

def getDayofTheWeek(actualDate, W, daysDic, monthDic, maxDaysofMonth):
    diff = 0
    for month in range(1, actualDate[0]+1):
        if month != actualDate[0]:
            diff += maxDaysofMonth[monthDic[month]]
        else:
            diff += actualDate[1]-1
    return (daysDic[W] + diff)%7

def getNextSunday(actualDate, weekDay, maxDaysofMonth, monthDic):
    actualDate  = ( actualDate[0], actualDate[1] + 7 - weekDay )
    if actualDate[1] > maxDaysofMonth[monthDic[actualDate[0]]]:
        actualDate = (actualDate[0]+1, actualDate[1] - maxDaysofMonth[monthDic[actualDate[0]]])
    return actualDate

def getNextSaturday(actualDate, weekDay, maxDaysofMonth, monthDic):
    if weekDay == 6:
        actualDate = ( actualDate[0], actualDate[1] +7 )
    else:
        actualDate  = ( actualDate[0], actualDate[1] + 6 - weekDay)
    if actualDate[1] > maxDaysofMonth[monthDic[actualDate[0]]]:
        actualDate = (actualDate[0]+1, actualDate[1] - maxDaysofMonth[monthDic[actualDate[0]]])
    return actualDate

print solution(2014, 'April', 'May', 'Wednesday')