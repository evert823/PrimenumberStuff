# This class represents a number expressed as the digits in it's own base
# e.g. having base 2, digits [1, 0, 0, 1] it will display decimal_value() as 9
# Use convert_to_otherbase(...) to get the digits in the other base
class int_in_base():
    def __init__(self, pbase):
        if type(pbase) != int:
            raise Exception("An integer was expected.")
        if pbase < 2:
            raise Exception("An integer >= 2 was expected.")
        self.base = pbase
        self.digit = [0]

    def set_base(self, pbase):
        self.__init__(pbase)

    def set_digits(self, *digits):
        self.digit = []
        for dg in digits:
            if type(dg) != int:
                raise Exception("A list of integers was expected.")
            if dg > self.base - 1 or dg < 0:
                raise Exception("Each digit should be >= 0 and <= base - 1.")
            self.digit.append(dg)

    def decimal_value(self):
        nd = len(self.digit)
        n = 0

        for i in range(0, nd):
            n += self.digit[i] * (self.base ** (nd - (i + 1)))
        return n
    
    def convert_to_otherbase(self, potherbase):
        result = int_in_base(potherbase)
        result.digit.clear()

        n = self.decimal_value()

        nd = 0
        while potherbase ** (nd + 1) <= n:
            nd += 1

        j = 0

        while j <= nd:
            k = n // (potherbase ** (nd - j))
            result.digit.append(k)
            n -= k * (potherbase ** (nd - j))
            j += 1
        
        return result

    def set_digits_from_base_10(self, pvalue):
        if type(pvalue) != int:
            raise Exception("An integer was expected.")
        if pvalue < 0:
            raise Exception("An integer >= 0 was expected.")

        n = pvalue

        self.digit.clear()

        nd = 0
        while self.base ** (nd + 1) <= n:
            nd += 1

        j = 0

        while j <= nd:
            k = n // (self.base ** (nd - j))
            self.digit.append(k)
            n -= k * (self.base ** (nd - j))
            j += 1

    def digitcharmapping(self):
        return ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b",
                "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", )

    def digitstring(self):
        if self.base > 36:
            raise Exception("digitstring method not supported for bases > 36.")
        
        dcm = self.digitcharmapping()

        s = ""

        for j in range(0, len(self.digit)):
            s += dcm[self.digit[j]]
        
        del dcm

        return s

    def set_digits_from_digitstring(self, pstring):
        if self.base > 36:
            raise Exception("set_digits_from_digitstring method not supported for bases > 36.")

        self.digit.clear()

        dcm = self.digitcharmapping()

        for j in range(0, len(pstring)):
            a = dcm.index(pstring[j])
            
            if a >= self.base:
                raise Exception("digitstring not eligible for base " + str(self.base))

            self.digit.append(a)

    def flipdigits(self):
        helpdigit = self.digit.copy()
        self.digit.clear()

        j = len(helpdigit)

        while j > 0:
            j -= 1
            self.digit.append(helpdigit[j])
