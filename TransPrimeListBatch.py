from factorfinder import factorfinder
import random

def PrintList(pnumberlength, i):
    global file2
    for j in range(0, len(i)):
        file2.write(str(i[j]) + "\n")


def IsTransPrimeList(pnumberlength, i):
    global AttemptCounter
    
    s = []
    cs = []
    ci = []

    for j in range(0, pnumberlength):
        s.append("")
        cs.append("")
        ci.append(0)
    for j in range(0, len(i)):
        s[j] = str(i[j])
    
    if s[0].find("0") > -1:
        return False
    es = s[len(i) - 1]
    if es.find("0") > -1 or es.find("2") > -1 or es.find("4") > -1 or es.find("5") > -1 or es.find("6") > -1 or es.find("8") > -1:
        return False
    
    AttemptCounter += 1
    if AttemptCounter % 10 == 0:
        file3 = open("TransPrimeListBatchOutput.log", 'a')
        file3.write(str(AttemptCounter) + " attempts\n")
        file3.close()

    for j1 in range(0, len(i)):
        cs[j1] = ""
        for j2 in range(0, len(i)):
            cs[j1] = cs[j1] + s[j2][j1]
    
    for j in range(0, len(i)):
        ci[j] = int(cs[j])
    
    for j in range(0, len(i)):
        if myfactorfinder.IsPrime(ci[j]) == False:
            return False

    return True


def OneRandomTransPrimeList(pnumberlength):
    i = []
    for j in range(0, pnumberlength):
        i.append(0)

    TransPrimeListFound = False
    while TransPrimeListFound == False:
        for j in range(0, len(i)):
            i[j] = 1
            while myfactorfinder.IsPrime(i[j]) == False:
                i[j] = random.randint(n_start, n_end + 1)
        
        TransPrimeListFound = IsTransPrimeList(pnumberlength, i)

    if TransPrimeListFound == True:
        PrintList(pnumberlength, i)


global file2
global AttemptCounter

AttemptCounter = 0

myfactorfinder = factorfinder()

file1 = open("TransPrimeListBatchInput.txt", 'r')
Lines = file1.readlines()
file1.close()

mynumberlength = int(Lines[0])

n_start = 10 ** (mynumberlength - 1)
n_end = (10 ** mynumberlength) - 1

file2 = open("TransPrimeListBatchOutput.txt", 'w')
file3 = open("TransPrimeListBatchOutput.log", 'w')
file3.write("Started\n")
file3.close()

OneRandomTransPrimeList(mynumberlength)

file2.close()
