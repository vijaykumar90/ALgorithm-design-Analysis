import sys
import os
'''
Team Members:-
Team Member 1: Sai Vijay Kumar Surineela, U01096171 Surineela.2@wright.edu 
Team Member 2: Prabhu Charan Murari, U01099304   murari.4@wright.edu
Team Member 3: Manoj Kumar Reddy Avula, U01067535  avula.25@wright.edu  
'''

import numpy as np

def arrayRank(fileName):
    with open(fileName, "r") as fileLines:
        rankList = [ranking.strip() for ranking in fileLines]

    size = int(rankList[0])
    del rankList[0]

    rankArray = np.zeros((2*size,size+1), dtype=object)
    for i in range(2*size):
        rankArray[i, :] = rankList[i].split()

    return rankArray


'''
Assume 'G1 & G2' as genders.
First create an array of size n*n for the given input, with first element being the Gender in question and its other gender preferences.
Then create a dict 'prefGen' with gender in question as a key and its preferences as a list in the value.
Create two free lists, each lit contains all the members of the similar gender. 
Create a dict 'DG1' with each member of one gender as keys and its stable partners as value, these stable partner will be filled by the end.
Create another dict 'DG' with all the members and its partners.
Intialise a proposal count variable count with 0
while there are elements in G1:
    for each member A in G1:
        for each member B in the preference list of A:
            if B in free list of G2:
                remove B from free list of G2
                remove A from free list of G1
                Add B as value to A in DG1
                Add A as value to B in DG
                Add B as value to A in DG
                count = count + 1
                break from the loop and go to member of free list G1
            else: //this means that B is free it is paired
                fetch the current partner of B from DG
                fetch the index of cuurent partner from the prefGen[B]
                fetch the index of A from the prefGen[B]
                if index of current partner is less than index of A:
                    count = count + 1
                    continue to next pref of A
                else:
                    add current partner to free list of G1
                    remove A from free list of G1
                    update B as value to A in DG1
                    add A as value to B in DG
                    update B as value to A in DG
                    count = count + 1
                    break from the loop and go to member of free list G1
    
write the Dict DG1 to output.txt as follow:
A1 B1
A2 B2
A3 B3       
'''


def gsAlgorithm(inputName):
    rankArray = arrayRank(inputName)
    rankDict = {key[0]: list(key[1:]) for key in rankArray}
    genderSize = len(rankArray)/2
    freeFirstGender = list(rankArray[:int(genderSize), 0])
    freeSecondGender = list(rankArray[int(genderSize):, 0])
    genderPairs = {genderOne:"" for genderOne in list(freeFirstGender)}
    # M-W && W-M both present dict form
    allMem = freeFirstGender + freeSecondGender
    allMemDictPair = {mem:"" for mem in list(allMem)}
    count = 0
    while(len(freeFirstGender) > 0):
        for firstGenderMember in freeFirstGender:
            for memOfFirstGenMemPref in rankDict[firstGenderMember]:
                if memOfFirstGenMemPref in freeSecondGender:
                    freeFirstGender.remove(firstGenderMember)
                    freeSecondGender.remove(memOfFirstGenMemPref)
                    genderPairs[firstGenderMember] = memOfFirstGenMemPref
                    allMemDictPair[firstGenderMember] = memOfFirstGenMemPref
                    allMemDictPair[memOfFirstGenMemPref] = firstGenderMember
                    count = count + 1
                    break
                else:
                    
                    currentpartner = allMemDictPair[memOfFirstGenMemPref]
                    currentPartnerIndex = (rankDict[memOfFirstGenMemPref]).index(currentpartner)
                    expectingPartnerIndex = (rankDict[memOfFirstGenMemPref]).index(firstGenderMember)
                    if currentPartnerIndex < expectingPartnerIndex:
                        count = count + 1
                        continue
                    else:
                        freeFirstGender.append(currentpartner)
                        allMemDictPair[currentpartner] = ""
                        genderPairs[currentpartner] = ""
                        freeFirstGender.remove(firstGenderMember)
                        genderPairs[firstGenderMember] = memOfFirstGenMemPref
                        allMemDictPair[firstGenderMember] = memOfFirstGenMemPref
                        allMemDictPair[memOfFirstGenMemPref] = firstGenderMember
                        count = count + 1
                        break
    
    with open("Output.txt", 'w') as file:
        for key, value in genderPairs.items():
            file.write(f"{key} {value}\n")
        file.write(str(count))

    with open("OutputToBeVerified.txt", 'w') as file2:
        for key, value in genderPairs.items():
            file2.write(f"{key} {value}\n")
        file2.write(str(count))


def main():
    if len(sys.argv)!=2:
        sys.exit(1)
    inputName = sys.argv[1]
    gsAlgorithm(inputName)       


if __name__ == "__main__":
    main()
