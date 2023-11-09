#los elementos no se puede repetir
#NO estan organizados por indices
#son inmutables

mi_set = set([1,2,3,4,5])
mi_set = set((1,2,3,4,5))
print(type(mi_set))
print(mi_set)


otro_set = {1,3,5,7}
print(type(otro_set))
print(len(otro_set))
print(2 in mi_set)

s1 = {1,2,3,4}
s2 = {5,4,7,8}
s3 = s1.union(s2)
print(s3)

s1.add(35)
print(s1)

s1.remove(3)
print(s1)

s1.discard(3)
print(s1)

s1.pop()
print(s1)

s1.clear()
print(s1)