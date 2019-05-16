#https://www.hackerrank.com/challenges/ctci-making-anagrams
def number_needed(a, b):
    list_a=list(a)
    list_b=list(b)
    list_a.sort();
    list_b.sort();
    list_int_a=[0]*26 #making empty list
    list_int_b=[0]*26   #making empty list
    num=0
    for i in a:
        c=ord(str(i))-97
        list_int_a[c]+=1
    for i in b:
        d=ord(str(i))-97
        list_int_b[d]+=1
    for i in range(0,26):
        num=num+abs(list_int_a[i]-list_int_b[i])
    return num

a = input().strip()
b = input().strip()
print(number_needed(a,b))
