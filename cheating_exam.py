d = int(input())
s = input()
sol = [' ' for x in range(len(s))]
#First 3
sol[0] = s[0]
sol[2*(d-1)] = s[1]
sol[4*(d-1)] = s[2]
sol[d-1] = s[len(s)-2]
sol[3*(d-1)] = s[len(s)-1]
for i in range(1,int((len(s)-5)/4)+1):
    sol[i] = s[3+4*(i-1)]
    sol[2*(d-1)-i] = s[3+4*(i-1)+1]
    sol[2*(d-1)+i] = s[3+4*(i-1)+2]
    sol[4*(d-1)-i] = s[3+4*(i-1)+3]
for i in reversed(s):
    if i == 'X':
        sol.pop()
print(''.join(sol))