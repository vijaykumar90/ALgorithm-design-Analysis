
'''
CS7200: Algorithm Design and Analysis, Assignment 2

Greedy algorithm for job scheduling on these two machines



Team Members: -

Team Member 1: Sai Vijay Kumar Surineela, U01096171 Surineela.2@wright.edu 

Team Member 2: Prabhu Charan Murari, U01099304   murari.4@wright.edu

Team Member 3: Manoj Kumar Reddy Avula, U01067535 avula.25@wright.edu  
'''
import sys

def inputParsing(fileName):

    with open(fileName, "r") as fileLines:
        strList = [ranking.strip() for ranking in fileLines]

    del strList[0]
    jobsInfo = []
    for i in strList:
        jobDetails = i.split()
        # print(jobDetails[2])
        # jobDetails[0] = int(jobDetails[0])
        jobDetails[1] = int(jobDetails[1])
        jobDetails[2] = int(jobDetails[2])
        jobsInfo.append(jobDetails)
    return jobsInfo


def scheduling(jobs, outputFileName):
    jobs.sort(key=lambda x: x[2])
    
    machine1 = []
    machine2 = []
    machine1LastEndTime = 0
    machine2LastEndTime = 0
    
    for eachJob in jobs:
        jobID = eachJob[0]
        jobStart = eachJob[1]
        jobEndTime = eachJob[2]
        if jobStart >= machine1LastEndTime:
            machine1LastEndTime = jobEndTime
            machine1.append(jobID)
        elif jobStart >= machine2LastEndTime:
            machine2LastEndTime = jobEndTime
            machine2.append(jobID)
    
    totalJobsPossible = str(len(machine1) + len(machine2))
    machine1 = " ".join(map(str, machine1))
    machine2 = " ".join(map(str, machine2))
    # print(f"m1 {machine1[0]} {machine1[1]}")
    with open(outputFileName, 'w') as file:
        file.write(f"{totalJobsPossible}\n")
        file.write(f"{machine1}\n")
        file.write(f"{machine2}\n")
    return 0



def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    
    outputFileName = (sys.argv[1]).replace("Input", "Output")
    
    jobs = inputParsing(sys.argv[1])
    scheduling(jobs, outputFileName)
    


if __name__ == "__main__":
    main()

# PsuedoCode

# The input file will have # 0f jobs, JobId, startTime, endTime.
# The output file should have # of jobs possible, jobs possible on M1 and jobs possible on M2 on 2 Machines with least overlapping.
# All the Jobs are sorted on earliest End time using sort() which has a time complexity of O(nlog(n)), relies on Timesort sorting technique.

"""
Pusedo code starts...
Sort all the jobs based on end time in ascending manner.
Initate a empty list for Jobs on Machine1.
Initate a empty list for Jobs on Machine2.
Initalise a int variable to zero which stores the last end time of the job that run on Machine1, machine1LastEndTime.
Initalise a int variable to zero which stores the last end time of the job that run on Machine2, machine2LastEndTime.
for indiviual job in sorted Jobs:
    store JobID, JobStartTime, JobEndTime from indiviual job.
    if a new job start time is equal or greater than machine1 LastEndTime:
        update the machine1 LastEndTime to new job end time.
        add the new jobs ID to List of jobs that can run Machine1.
    else:
        update the machine2 LastEndTime to new job end time.
        add the new jobs ID to List of jobs that can run Machine2.

totalJobs is the toatl # of jobs that can run on 2 machine is summation of elements in Machine1 & Machine2.
Join all jobs in machine 1 with a space gap, which is to be printed in output file.
Join all jobs in machine 1 with a space gap, which is to be printed in output file.

"""
# Greedy Heuristics used is Earliest Finish Time Maximizing the number of non-overlaping jobs on two machines, with a time complexity of O(nlog(n)).
"""
Example to Illustrate Correctness:

Consider the following list of jobs:
5
1 5 7
2 0 3
3 6 8
4 3 6
5 1 4

Execution:

1. Sort the Jobs by End Time:
    - Sorted Job Ids: 2, 5, 4, 1, 3.
    - Job 2 is assigned to M1.
    - Job 5 and Job 2 overlaps, so it is assigned to M2.
    - Job 4, after Job 2 ends, assigned to M1.
    - Job 1, after Job 5 ends, assigned to M2.
    - Job 3, after Job 4 ends, assigned to M1.

    Result:
    - 5
    - M1: Jobs [2, 4, 3]
    - M2: Jobs [1, 5]
"""
