# John has a fascination with numbers. He likes numbers that have their digits in increasing order like 149, 468, 789, etc. 
# He does not like numbers that don't follow this rule like 543, 664, 299, etc.

# Given a number N as input, find the largest number less than or equal to N which will appeal to John's liking.

# Input

# An integer N which is less than 1,000,000.

# Output

# An integer less than or equal to N, which appeals to John's peculiar rules.

# For example:

# If the input number is 1234 then this number already has its digits in increasing order, and hence, the output would be the same number i.e. 1234.

# If the input number is 998 then this number doesn’t have its digits in increasing order and we will decrement this number by 1 in each iteration till we reach the number 789 which follows the desired order.


def largestNonDecreasingNums(num):
    num_str = str(num)
    num_list = [int(s) for s in num_str]
    r = len(num_list) - 1
    l = r - 1
    while l >= 0:
        # print(num_list, l, r)
        # Check for left > right
        if num_list[l] >= num_list[r]:
            num_list[l] -= 1
            num_list[r] = 9
        
        # Now to check if the right + 1 < right
        if r != len(num_list) - 1 and num_list[r+1] <= num_list[r]:
            l = r
            r += 1
        else:
            l -= 1
            r -= 1
    num_list = map(str, num_list)
    res = ''.join(num_list)
    return int(res)

print(largestNonDecreasingNums(1234))  # 1234
print(largestNonDecreasingNums(998))  # 789
print(largestNonDecreasingNums(299))  # 289
print(largestNonDecreasingNums(1000000))

# def increasingNumber(number):
#     str_num = str(number)
#     num_list = [int(num) for num in str_num]

#     # keep two pointers, starting from the right
#     rdigit = len(num_list) - 1
#     ldigit = rdigit - 1

#     while ldigit >= 0:
#         # print(num_list, ldigit, rdigit)

#         # if left digit >= right digit, decrement left digit by 1, and assign right digit as 9
#         if num_list[ldigit] >= num_list[rdigit]:
#             num_list[ldigit] -= 1
#             num_list[rdigit] = 9
        
#         #print(num_list)
#         # if right digit is >= the digit next to it, increment both pointers ans go through them again.
#         if rdigit != len(num_list)-1 and num_list[rdigit+1] <= num_list[rdigit]:
#             ldigit = rdigit
#             rdigit = rdigit + 1 
#         # else if right digit is > left digit, decrement both ptrs
#         else:
#             ldigit -= 1
#             rdigit -= 1

#     return num_list
#     # concatenate list and return number

# print(increasingNumber(1000000))