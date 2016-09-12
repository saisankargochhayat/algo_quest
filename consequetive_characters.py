
n=int(input())
for i in range(n):
    word=list(input())
    ans=list()
    res_ind = 1
    ip_ind = 1
    ch=word[0]
    ans.append(ch)
    for i in range(1,len(word)):
        if word[i]!=ch:
            ans.append(word[i])
            ch=word[i]
    ans="".join(ans)
    print(ans)












# one list approach to delete same characters
# n=int(input())
# for i in range(n):
#     word=list(input())
#     res_ind = 1
#     ip_ind = 1
#     while ip_ind != len(word):
#         if word[ip_ind] != word[ip_ind-1]:
#             word[res_ind] = word[ip_ind]
#             res_ind += 1
#         ip_ind+=1
#     word="".join(word[0:res_ind])
#     print(word)
