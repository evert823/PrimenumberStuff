from datetime import datetime
from factorfinder import factorfinder

def PrintDateTime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    del now

def PrintNextPrime():
    doquit = False
    displayfactorfrom = -1

    s = input("From what size do you want found factors to be displayed? --> ")
    try:
        displayfactorfrom = int(s)
    except:
        doquit = True

    while doquit == False:
        print("                                    ----+----0----+----0----+----0----+----0")
        mynumberstr = input("Type your candidate number here --> ")
    
        try:
            mynumber = int(mynumberstr)
        except:
            doquit = True

        if doquit == False:
            PrintDateTime()
            f = myfactorfinder.SmallestFactorGT1(mynumber)
            if f < mynumber and f >= displayfactorfrom:
                print(str(f) + " is a factor of " + str(mynumber))
            while f < mynumber:
                mynumber += 1
                f = myfactorfinder.SmallestFactorGT1(mynumber)
                if f < mynumber and f >= displayfactorfrom:
                    print(str(f) + " is a factor of " + str(mynumber))
            print(str(mynumber))

            PrintDateTime()

myfactorfinder = factorfinder()

PrintNextPrime()
