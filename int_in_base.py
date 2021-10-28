# This class represents a number expressed as the digits in it's own base
# e.g. having base 2, digits [1, 0, 0, 1] it will display decimal_value() as 9
# Use convert_otherbase(...) to get the digits in the other base
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

