n = int(input())
for i in range(n):
    m = input()
    try:
        evaluation = int(eval(m))
        print(evaluation)
    except ZeroDivisionError:
        print("Division by zero encountered")
