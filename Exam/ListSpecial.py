list = [1,[2,3,4],['a','b',[5,6]],7]
print(list)

list[1].append(9)
print(list)

list[2][2].remove(6)
print(list)

list[2].insert(2,'c')
print(list)

list[1].pop(1)
print(list)

del list[2][3][0]
print(list)