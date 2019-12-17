p = 'L,8,R,10,L,10,R,10,L,8,L,8,L,10,L,8,R,10,L,10,L,4,L,6,L,8,L,8,R,10,L,8,L,8,L,10,L,4,L,6,L,8,L,8,L,8,R,10,L,10,L,4,L,6,L,8,L,8,R,10,L,8,L,8,L,10,L,4,L,6,L,8,L,8'#.replace('L', '_').replace('R', '.')

A = 'L,8,R,10,L,10'
B = 'L,4,L,6,L,8,L,8'
C = 'R,10,L,8,L,8,L,10'

p = p.replace(A, 'A')
p = p.replace(B, 'B')
p = p.replace(C, 'C')

print(p)
print(A)
print(B)
print(C)
