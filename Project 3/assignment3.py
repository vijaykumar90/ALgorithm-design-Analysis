'''
CS7200: Algorithm Design and Analysis, Assignment 3

Interleaving of 2 strings


Team Members: -

Team Member 1: Sai Vijay Kumar Surineela, U01096171 Surineela.2@wright.edu 

Team Member 2: Prabhu Charan Murari, U01099304   murari.4@wright.edu

Team Member 3: Manoj Kumar Reddy Avula, U01067535 avula.25@wright.edu  
'''
from itertools import combinations
import sys

def splitString(s, max):
    siz = len(s)
    subSTR = []
    for sub in range(1, max+1):
        subsets = combinations(range(1, siz), sub-1)
        for subNum in subsets:
            res = []
            begin = 0
            for ind in subNum:
                res.append(s[begin:ind])
                begin = ind
            res.append(s[begin:])
            subSTR.append(res)
    return subSTR


def dynamicProgramme(s1Split, s2Split, s3):
            s1SplitLen = len(s1Split)
            s2SplitLen = len(s2Split)
            s3Len = len(s3)
            dp = [[[False] * (s3Len + 1) for _ in range(s2SplitLen + 1)] for _ in range(s1SplitLen + 1)]
            dp[0][0][0] = True

            for x in range(s1SplitLen+1):
                for y in range(s2SplitLen+1):
                    for z in range(1, s3Len+1):
                        # if z == 0:
                        #     continue

                        s3FilledLenght = z - len(s1Split[x-1])
                        s3FilledLenght2 = z - len(s2Split[y-1])
                        if s3[s3FilledLenght:z] == s1Split[x - 1] and z >= len(s1Split[x - 1]) and dp[x - 1][y][s3FilledLenght] and x > 0:
                            dp[x][y][z] = True
                        if s3[s3FilledLenght2:z] == s2Split[y - 1] and z >= len(s2Split[y - 1]) and dp[x][y - 1][s3FilledLenght2] and y > 0:
                            dp[x][y][z] = True

            return dp

def backtrack(s1Split, s2Split, dp, s3):
            count =0
            s1SplitLen = len(s1Split)
            s2SplitLen = len(s2Split)
            s3Len = len(s3) ##
            interleaving = []
            if dp[s1SplitLen][s2SplitLen][len(s3)]:
                count += 1
                # s1SplitLen, s2SplitLen, s3Len = s1SplitLen, s2SplitLen, len(s3)
                while s1SplitLen > 0 or s2SplitLen > 0:
                    if  dp[s1SplitLen - 1][s2SplitLen][s3Len - len(s1Split[s1SplitLen - 1])] and s1SplitLen > 0 and s3Len >= len(s1Split[s1SplitLen - 1]):
                        interleaving.append((s1Split[s1SplitLen - 1], "s1"))
                        s3Len = s3Len - len(s1Split[s1SplitLen - 1])
                        s1SplitLen = s1SplitLen - 1
                    elif dp[s1SplitLen][s2SplitLen - 1][s3Len - len(s2Split[s2SplitLen - 1])] and s2SplitLen > 0 and s3Len >= len(s2Split[s2SplitLen - 1]):
                        interleaving.append((s2Split[s2SplitLen - 1], "s2"))
                        s3Len = s3Len - len(s2Split[s2SplitLen - 1])
                        s2SplitLen = s2SplitLen - 1
                interleaving.reverse()
            return count, interleaving



def checkInterleaving(s1, s2, s3):
    s1Len = len(s1)
    s2Len = len(s2)
    s3Len = len(s3)
    s1Subs = splitString(s1, (s3Len+1)//2)
    s2Subs = splitString(s2, (s3Len+1)//2)
    if (s1Len + s2Len) != s3Len:
        return False, 0, []
    
    interleavingsCount = 0
    ans = []
    for s1Split in s1Subs:
        for s2Split in s2Subs:
            diff = abs(len(s1Split) - len(s2Split))
            if diff > 1:
                continue
            

            dp = dynamicProgramme(s1Split, s2Split, s3)
            count, interleaving = backtrack(s1Split, s2Split, dp, s3)
            interleavingsCount = interleavingsCount + count
            if (count>0):
                 ans.append(interleaving)
    
    if interleavingsCount > 0:
         return True, ans, interleavingsCount
    else:
         return False, ans, interleavingsCount


def outputDesign(ans):
    s1 = []
    s2 = []
    for strSub, strNo in ans:
        if strNo == "s1":
            s1.append(strSub)
        elif strNo == "s2":
            s2.append(strSub)
    return f"s1 substrings: {', '.join(s1)}\n" + f"s2 substrings: {', '.join(s2)}\n"

def main():
    inputFile = sys.argv[1]
    with open(inputFile, 'r') as inp:
        s1 = inp.readline().strip()
        s2 = inp.readline().strip()
        s3 = inp.readline().strip()

    boolValue, ans, count = checkInterleaving(s1, s2, s3)

    outputFile = inputFile.replace("Input", "Output")
    with open(outputFile, 'w') as res:
        if boolValue:
            res.write(f"Interleaving exists: {boolValue}, Count of interleavings: {count}\n")
            subsValue = outputDesign(ans[0])
            res.write(subsValue)
        else:
             res.write(f"Interleaving exists: {boolValue}, Count of interleavings: 0\n")

if __name__ == "__main__":
    main()
            


# Psuedocode:
'''
Interleaving of 2 strings s1 and s2 forms s3
if len of s3 is not equal to sum of s1 and s2, it is a wrong interleaving.
splitString() splits a string and forms all possible substrings
We have 3 more central menthods checkInterleaving(), dynamicProgramme(), backtracking()
checkInterleaving() passes s1, s2 and s3 to for forming a 3d Dynamic programming matrix
dynamicProgramming():
    form a 3d matrix "dp" with all values filled with False value, with x-axis as s1 subtsring, y-axis as s2 substring, z-axis as s3
    dp[0][0][0] = True
    for x in range(s1SplitLen+1):
        for y in range(s2SplitLen+1):
            for z in range(1, s3Len+1):
                # Checking the match of substring from s1 with s3
                if last portion of s3 == current s1 substring and x>0 & z has more space left than previous x & dp[previous x][y][previous z] == True:
                    dp[x][y][z] = True
                # Checking the match of substring from s2 with s3
                if last portion of s3 == current s2 substring and y>0 & z has more space left than previous y & dp[x][y-1][previous z] == True:
                    dp[x][y][z] = True
    return dp

backtracking():
    if dp[s1SplitLen][s2SplitLen][len(s3)]:
        count += 1
        while s1SplitLen > 0 or s2SplitLen > 0:
            # check for s1
            interleaving.append((s1Split[s1SplitLen - 1], "s1"))
            s3Len = s3Len - len(s1Split[s1SplitLen - 1])
            s1SplitLen = s1SplitLen - 1
            #similarly check for s2
            interleaving.append((s2Split[s2SplitLen - 1], "s2"))
            s3Len = s3Len - len(s2Split[s2SplitLen - 1])
            s2SplitLen = s2SplitLen - 1
            
'''

'''
Informal argument for its correctness
s1: aabcc
s2: dbbca 
s3: aadbbcbcac

Interleaving exists: True, Count of interleavings: 36
s1 substrings: aa, bc, c
s2 substrings: db, bca
'''

'''
Time complexity is exponential because of generation of substrings
Space complexity is exponential because of generation of substrings
'''