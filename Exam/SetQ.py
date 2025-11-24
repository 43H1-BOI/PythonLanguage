X = [1,2,3,4]
Y = (3,4,5,6)
Z = {3,4}

X , Y , Z = frozenset(X) , frozenset(Y) , frozenset(Z)

# diffXY = X - Y
diffXY = X.difference(Y)

# symDiffXY = X ^ Y
symDiffXY = X.symmetric_difference(Y)

# intersectionXYZ = X & Y & Z
intersectionXYZ = X.intersection(Y,Z)

# supersetXZ = X >= Z
supersetXZ = X.issuperset(Z)

# subsetXZ = X <= Z
subsetXZ = X.issubset(Z)

disjointXZ = Z.isdisjoint(X)

print(X , Y , Z)
print(diffXY,symDiffXY,intersectionXYZ,supersetXZ,subsetXZ,disjointXZ, sep = "\n")