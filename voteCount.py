"""
Author: George Krlevski
Date: 17/04/14
"""


import os.path


#1
def getCandidates(f):
    #Get candidates from file
    if os.path.exists(f):
        candidates=[]
        f=open(f,'r')
        for line in f:
            candidates.append(line.strip('\n'))
        return candidates
    else:
        print('ERROR: File does not exist')
        return ([])
    
        
#2
def parseVote(s):
    #returns 0 for an empty vote
    #returns -1 if there are any non digits
    #otherwise returns s
    s= s.strip()
    if s == "" or s== " ":
        return 0
    elif s.isdigit():
        return int(s)
    else:
        return -1
     
#3
def parsePaper(s,n):
    # sends each number in s to parseVote
    s= s.split(',')
    numbers=[]
    for each in s:
        numbers.append(parseVote(each))
        if parseVote(each)== -1:
            return ([],'non-digits')    
    try:
        if len(numbers)>n:
            return ([],'too long')
        elif sum(numbers)== 0:
            return ([],'blank')
        else:
            return (numbers,'')
    except:
        return ([],'blank')
        
    
#4
def getPapers(f,n):
    #use parsePaper for each line
    if os.path.exists(f):
        f=open(f,'r')
        papers=[]
        votes=[]
        votesList=[]
        formal=[]
        informal=[]
        for eachVote in f:
            votes.append(parsePaper(eachVote,n))
            
        for each in votes:
            papers.append(each)

        return papers        

    else:
        print( 'ERROR: File does not exist')
        return ([])
    
#5
def normalisePaper(p,n):
    result=[]
    p=list(p)
    for each in p:
        if n>= len(p):
            n=(n-len(p))
            p.extend([0]*n)
    for eachVote in p:
           result.append(eachVote/int(sum(p)))
    return result

#6
def normalisePapers(ps,n):
    normalised=[]
    for p in ps:
        normalised.append(normalisePaper(p,n))
    return normalised
    

#7
def countVotes(cs,ps):
    List=[]
    pos= 0
    for eachNumber in cs:
        x=0
        total=[]
        for eachVote in ps:
            x += (eachVote[pos])
        pos=pos+1
        total.append(x)
        total.append(str(eachNumber))
        List.append(total)
        List.sort(reverse= True)
    
    return List

#8
def printCount(c):
    for eachVote in c:
            print('%4.2f%2s'%(eachVote[0], eachVote[1]))   

#9
def main():
    
    candidates=input('Enter file name which contains candidates: ')
    papers= input('Enter file which contains ballot papers: ')

    f=candidates

    canD= getCandidates(f)
    n=len(candidates)

    p=papers
    papersGet= getPapers(p,n)
    cs= canD
    total=[]

    formal=[]
    informal=[]
    for each in total:
        if papersGet==[]:
            formal.append(each)
        else:
            informal.append(each)
 
    papersNormalise= normalisePapers(formal,n)
    ps= papersNormalise

    votesTotal= countVotes(cs, ps)
    print('Nerdvanian election 2014')
    print('\n'+'There were', len(informal),' informal votes')
    print ('There were', len(formal),' formal votes'+ '\n')

    votesCount= printCount(votesTotal)
    print(votesCount)# prints stats

    

    
        

