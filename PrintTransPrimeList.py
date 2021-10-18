import math
import random
from datetime import datetime
from factorfinder import factorfinder

def PrintList(pnumberlength, i):
    for j in range(0, len(i)):
        print(str(i[j]))

def IsTransPrimeList(pnumberlength, i):
    global AttemptCounter
    
    if PrintAttemptCounter == True:
        AttemptCounter += 1
        if AttemptCounter % 100000 == 0:
            print(str(AttemptCounter) + " attempts and testing this one : ")
            PrintList(pnumberlength, i)

    s = []
    cs = []
    ci = []

    for j in range(0, pnumberlength):
        s.append("")
        cs.append("")
        ci.append(0)
    for j in range(0, len(i)):
        s[j] = str(i[j])
    
    for j1 in range(0, len(i)):
        cs[j1] = ""
        for j2 in range(0, len(i)):
            cs[j1] = cs[j1] + s[j2][j1]
    
    for j in range(0, len(i)):
        ci[j] = int(cs[j])
    
    for j in range(0, len(i)):
        if ci[j] < n_start or myfactorfinder.IsPrime(ci[j]) == False:
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


def LoopOverAllPrimes(pnumberlength, i):

    if len(i) >= pnumberlength:
        if IsTransPrimeList(pnumberlength, i):
            print("Valid TransPrimeList : ")
            PrintList(pnumberlength, i)
    else:

        for i1 in range(n_start, n_end + 1):
            nozeroes = True
            if len(i) == 0:
                s = str(i1)
                if s.find("0") > -1:
                    nozeroes = False

            if nozeroes == True and myfactorfinder.IsPrime(i1) == True:
                local_i = i.copy()
                local_i.append(i1)
                LoopOverAllPrimes(pnumberlength, local_i)
                del local_i

# Main program starts here
# Set PrintAttemptCounter to True to see progress - recommended from 7 or 8 digits

AttemptCounter = 0
PrintAttemptCounter = False

myfactorfinder = factorfinder()

mynumberlengthstr = input("How many digits should the prime numbers have? --> ")
mynumberlength = int(mynumberlengthstr)

n_start = 10 ** (mynumberlength - 1)
n_end = (10 ** mynumberlength) - 1

print("Option a : random search")
print("Option b : systematic search")
myoption = input("Type a or b please --> ")

if myoption.upper() == "A":
    OneRandomTransPrimeList(mynumberlength)
if myoption.upper() == "B":
    LoopOverAllPrimes(mynumberlength, [])
