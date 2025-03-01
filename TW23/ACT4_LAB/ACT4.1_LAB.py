A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

print("Elements in A and B:", len(A | B))
print("Elements in B that are not in A and C:", len(B - (A | C)))

print("i.", C - A) 
print("i.", A & C) 
print("ii.", (A & B) | (B & C)) 
print("iii.", (C & A) - B)
print("iv.", (A & C) - B)
print("v.", A & B & C)
print("vi.", B - (A | C))  