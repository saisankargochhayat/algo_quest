# A magic number is defined as a number which can be expressed as a power of 5 or sum of unique 
# powers of 5. First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….
# Write a function to find the nth Magic number.
def magicnum(n):
    pow = 1
    ans = 0
    while(n):
        pow *=5
        #and operator performs bitwise and
        if n & 1:
            ans += pow
        
        #shifts to the right by 1
        n = n>>1
    return ans
if __name__ == "__main__":
    n = int(input())
    print(magicnum(n))