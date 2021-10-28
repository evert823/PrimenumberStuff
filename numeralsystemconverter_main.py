from int_in_base import int_in_base

# The int_in_base class contains the methods to convert between numeral systems

# We can create an int_in_base object with any base
a = int_in_base(89)

# We can alter the base of an existing int_in_base object instance
a.set_base(29)

# set_digits is used to assign a value, each argument being the respective digit (the digit itself is 10-based!)
a.set_digits(4, 19, 28, 1, 13, 7)

# The decimal_value method specifically converts to decimal system
print(str(a.decimal_value())) # expected output 96167052

# The convert_otherbase method returns another int_in_base object instance, having the same value in the new base
b = a.convert_to_otherbase(31)
print(b.digit) # expected output [3, 11, 4, 1, 23, 30]