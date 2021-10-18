import math

class factorfinder:
    def SmallestFactorGT1(self, pnumber):
        if type(pnumber) != int:
            return -1
        if pnumber < 2:
            return -1

        if pnumber % 2 == 0:
            return 2
        if pnumber % 3 == 0:
            return 3
        if pnumber % 5 == 0:
            return 5
        
        MySqrt = math.floor(math.sqrt(pnumber))

        a = 7

        #Pattern +4 +2 +4 +2 +4 +6 +2 +6 avoids muliples of 2, 3 and 5

        while a <= MySqrt:
            if pnumber % a == 0:
                return a
            a += 4
            if pnumber % a == 0:
                return a
            a += 2
            if pnumber % a == 0:
                return a
            a += 4
            if pnumber % a == 0:
                return a
            a += 2
            if pnumber % a == 0:
                return a
            a += 4
            if pnumber % a == 0:
                return a
            a += 6
            if pnumber % a == 0:
                return a
            a += 2
            if pnumber % a == 0:
                return a
            a += 6
    
        
        return pnumber

    def IsPrime(self, pnumber):
        return (self.SmallestFactorGT1(pnumber) == pnumber and pnumber != -1)
