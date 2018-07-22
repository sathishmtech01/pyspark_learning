import os , subprocess

def killAllRunningJobs(oozieURL):
    runningJobs = subprocess.getoutput("oozie jobs -oozie " + oozieURL + " -jobtype coordinator | grep -i RUNNING |  awk -F \" \" '{print $1} " )
    print("Current Running Co-ordinator Jobs : " + runningJobs)
    input()
    for jobs in runningJobs:
        os.system("oozie job -oozie " + oozieURL + " -kill " + jobs)

if __name__ == '__main__':
    #oozie jobs -oozie http://localhost:11000/oozie/ -jobtype coordinator | grep -i RUNNING |  awk -F \" \" '{print $1}
    oozieURL = "http://localhost:11000/oozie/"
    print("oozie jobs -oozie " + oozieURL + " -jobtype coordinator | grep -i RUNNING |  awk -F \" \" '{print $1} ")
    killAllRunningJobs("http://localhost:11000/oozie/")