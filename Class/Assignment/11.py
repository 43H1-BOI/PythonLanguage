# 11. Write a python program to demonstrate all operators – 
#       a) Arithmetic Operators 
#       b) Assignment Operators 
#       c) Comparison Operators 
#       d) Logical Operators 
#       e) Bitwise Operators 
#       f) Special Operators


# 11.a) Arithmetic Operators 
sum = 5 + 6
sub = 5 - 6
mul = 5 * 6
div = 5 / 6
mod = 5 % 6

# # Don't Write Print Statements
# print("5 + 6 =",sum)
# print("5 - 6 =",sub)
# print("5 * 6 =",mul)
# print("5 / 6 =",div)
# print("5 % 6 =",mod)


# 11.b) Assignment Operators 

a = 5 # Assignment
b = 4

a += 3      # a = a + 3
a -= 3.3    # a = a - 3.3
b *= 2      # a = a * 2
a /= 5      # a = a / 5
a %= 7      # a = a % 7


# 11.c) Comparison Operators

isLessThan = a > b  # less than
isGreaterThan = a < b # greater than or equals
isGTEQ = a <= b # greater than or equals
isLTEQ = a >= b # greater than or equals
isEquals = a == b # equals
notEquals = a != b # not equals

# These Will Return True and False
print(c,d,e,f)


'''
# 11. Write a python program to demonstrate all operators – 
#       a) Arithmetic Operators 
#       b) Assignment Operators 
#       c) Comparison Operators 
#       d) Logical Operators 
#       e) Bitwise Operators 
#       f) Special Operators


# 11.a) Arithmetic Operators 
sum_ = 5 + 6
sub = 5 - 6
mul = 5 * 6
div = 5 / 6
mod = 5 % 6
floordiv = 5 // 6
power = 5 ** 2


# 11.b) Assignment Operators 
a = 5   # Assignment
b = 4

a += 3      # a = a + 3
a -= 3.3    # a = a - 3.3
b *= 2      # b = b * 2
a /= 5      # a = a / 5
a %= 7      # a = a % 7
a //= 2     # a = a // 2
b **= 2     # b = b ** 2


# 11.c) Comparison Operators 
isGreater = a > b
isLess = a < b
isGTEQ = a >= b
isLTEQ = a <= b
isEqual = a == b
notEqual = a != b


# 11.d) Logical Operators 
logicalAnd = (a > 2) and (b < 10)
logicalOr  = (a < 2) or (b > 5)
logicalNot = not (a == b)


# 11.e) Bitwise Operators 
x, y = 6, 3   # 6 = 110, 3 = 011
bitAnd = x & y
bitOr  = x | y
bitXor = x ^ y
bitNot = ~x
bitLShift = x << 2
bitRShift = x >> 2


# 11.f) Special Operators 
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

isIdentity1 = (list1 is list2)       # False
isIdentity2 = (list1 is list3)       # True
isNotIdentity = (list1 is not list2)

isMember = (2 in list1)
isNotMember = (5 not in list1)


# ---- Print Results Section ----
print("Comparison:", isGreater, isLess, isGTEQ, isLTEQ, isEqual, notEqual)
print("Logical:", logicalAnd, logicalOr, logicalNot)
print("Bitwise:", bitAnd, bitOr, bitXor, bitNot, bitLShift, bitRShift)
print("Identity:", isIdentity1, isIdentity2, isNotIdentity)
print("Membership:", isMember, isNotMember)

'''