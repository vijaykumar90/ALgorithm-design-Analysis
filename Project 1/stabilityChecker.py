import sys
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

def outputPairsMethod(fileName):
    with open(fileName, "r") as fileLines:
        rankList = [ranking.strip() for ranking in fileLines]

    rankList.pop()
    size = len(rankList)
    outputArray = np.zeros((size,2), dtype=object)
    for i in range(size):
        outputArray[i, :] = rankList[i].split()

    return outputArray

'''
Assume 'G1 & G2' as genders.
First create an array of size n*n for the given Input.txt, with first element being the Gender in question and its other gender preferences.
Then create a dict 'prefGen' with gender in question as a key and its preferences as a list in the value.
Create an array 'output' of size n*2 for the given OutputToBeVerified.txt, as[[A1, B1],[A2, B2]....].
Create a List LG2 with all the members of G2 from slicing the list output.
for i in range(n):
    member A of G1 is output[i][0]
    member B of G2 is output[i][1]
    preferenceA is preference list of A from prefGen[A]
    for B' from the list preferenceA:
        if B' == B: // this means that B is perfect match for A, also the loop will not go below the member of B
            break out of the loop and go to next Pair.
        find index ind of B' from LG2, also the index is same for partner of B' in output
        find the current partner of B', A' from the index above using output[ind][0]
        preferenceB from prefGen[B]
        rankA' is the rank of A' from preferenceB
        rankA is the rank of A from preferenceB
        if rankA' is more than rankA:
            return False which means unstable

return True, which means stable

print the result stable or not to verified.txt


'''

def stabilityChecker(inputFile, outputFile):
    rankArray = arrayRank(inputFile)
    rankDict = {key[0]: list(key[1:]) for key in rankArray}
    output = outputPairsMethod(outputFile)
    size = len(output)
    allSecondGenders = [column[1] for column in output]
    for i in range(size):
        firstGender = output[i][0]
        secondGender = output[i][1]
        firstGenderList = rankDict[firstGender]
        for preference in firstGenderList:
            if preference == secondGender:
                break            
            ind = allSecondGenders.index(preference)
            currentSecondGenPartner = output[ind][0]
            preferenceList = rankDict[preference]
            currentPartnerRank = preferenceList.index(currentSecondGenPartner)
            expectedPartnerRank = preferenceList.index(firstGender)
            if expectedPartnerRank < currentPartnerRank:
                return False
    
    return True

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
    else:
        inputName = sys.argv[1]
        outputName = sys.argv[2]
        res = stabilityChecker(inputName, outputName)
    
    
        if res:
            with open("Verified.txt", 'w') as file:
                file.write("stable")
        else:
            with open("Verified.txt", 'w') as file:
                file.write("unstable")

if __name__ == "__main__":
    main()
    
    


