# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    resp = -1
    # digitsIndexList = []
    # upperCaseIndexList = []
    # for i in range(len(S)):
    #     if S[i].isupper():
    #         upperCaseIndexList.append(i)
    #     if S[i].isdigit():
    #         digitsIndexList.append(i)
    # i=-1
    # for end in digitsIndexList:
    #     valid = False
    #     for index in upperCaseIndexList:
    #         if index >i and index < end:
    #             valid = True
    #             break
    #     if valid == True:
    #         resp = max(resp, end-i+1)
    #     i = end
    # if len(digitsIndexList) > 0:
    #     i = digitsIndexList[-1]
    #     end = len(S)-1
    #     valid = False
    #     for index in upperCaseIndexList:
    #             if index >i and index < end:
    #                 valid = True
    #                 break
    #     if valid == True:
    #         resp = max(resp, end-i+1)
    # return resp
    current = 0
    valid = False
    for letter in S:
        if letter.isupper():
            valid = True
        if not letter.isdigit():
            current+=1
        else:
            if valid == True:
                resp = max(resp, current)
            current = 0
            valid = False
    if valid == True:
        resp = max(resp, current)
    return resp



print solution("a0Bs")