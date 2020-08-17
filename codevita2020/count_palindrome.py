def generateNumbers(low, high):
    res = []
    for r in range(low, high+1):
        curr = str(r)
        # We add hours here
        for h in range(0,24):
            hcurr = curr+'0'+str(h) if h < 10 else curr+str(h)
            # Check for mins here 
            for m in range(0, 60):
                mcurr = hcurr+'0'+str(m) if m < 10 else hcurr+str(m)
                # And finally seconds here
                for s in range(0, 60):
                    scurr = mcurr+'0'+str(s) if s < 10 else mcurr+str(s)
                    # Palindrome check
                    if scurr[::-1] == scurr:
                      res.append(scurr)
    print(res)
    return len(res)

def main():
    m, n = map(int,input().split())
    res = generateNumbers(m, n)
    print(res)
    return res
main()