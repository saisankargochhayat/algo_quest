#https://www.hackerrank.com/challenges/time-conversion
#!/bin/python3
import sys
time = input().strip()
tim=[]
if time[0]=='1' and time[1]=='2' and time[8]=='A' and time[9]=='M':
    tim.append(0)
    tim.append(0)
    for i in range(2,8):
        tim.append(time[i])
elif time[8]=='A' and time[9]=='M':
    for i in range(0,8):
        tim.append(time[i])
elif time[0]=='1' and time[1]=='2' and time[8]=='P' and time[9]=='M':
    tim.append(time[0])
    tim.append(time[1])
    for i in range(2,8):
        tim.append(time[i])
elif time[8]=='P' and time[9]=='M':
    tim.append(str(int(time[0]+time[1])+12))
    for i in range(2,8):
        tim.append(time[i])
print(''.join(str(e) for e in tim).strip())