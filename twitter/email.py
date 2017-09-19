
import re

def hideEmail(n):
    lengthOfUsername = n.find('@')
    hiddenEmail = n[0]+'*****'+n[lengthOfUsername-1]+n[lengthOfUsername:]
    print("E:"+hiddenEmail)
def phnNumber(n):
    num=list(n)
    counter = 0
    cleared = list()
    for i in range(len(num)):
        if num[i].isdigit() or num[i]=='+':
            cleared.append(num[i])
    modifiedNum=str()
    for i in range(len(cleared)-1,-1,-1):
        if cleared[i].isdigit():
            if counter>3:
                cleared[i]='*'
        counter+=1
    countrycode = len(cleared)-10
    output = ''
    if countrycode > 0:
        output+=''.join(cleared[0:countrycode])
        output+='-'
    output+='***-***-'
    output+= ''.join(cleared[len(cleared)-4:])
    print("P:"+output)
if __name__ == '__main__':
    while(1):
        try:
            n=input().strip()
        except EOFError:
            break
        if n == '':
            break
        if(n[0]=='E'):
            res=hideEmail(n[2:])
        elif (n[0]=='P'):
            res=phnNumber(n[2:])
        else:
            break
        