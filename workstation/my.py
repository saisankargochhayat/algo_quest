t = int(input())
for test in range(t):
    n = int(input())
    matrix = []
    matrix.append(str(input()))
    matrix.append(str(input()))
    total_hash = matrix[0].count('#') + matrix[1].count('#')
    topptr = 0
    botptr = 1
    topctr = 0
    botctr = 0
    topalive = True
    botalive = True
    for i in range(len(matrix[0])):
    # Iteration 1
        if not botalive and not topalive:
            break
        if topalive:
            if topptr == 0:
                if matrix[0][i] == '#':
                    topptr = 0
                    topctr += 1
                    if matrix[1][i] == '#':
                        topptr = 1
                        topctr += 1
                elif topctr != 0:
                    topalive = False
            else:
                if matrix[1][i] == '#':
                    topptr = 1
                    topctr += 1
                    if matrix[0][i] == '#':
                        topptr = 0
                        topctr += 1
                elif topctr != 0:
                    topalive = False
        if botalive:
            if botptr == 0:
                if matrix[0][i] == '#':
                    botptr = 0
                    botctr += 1
                    if matrix[1][i] == '#':
                        botptr = 1
                        botctr += 1
                elif botctr != 0:
                    botalive = False
            else:
                if matrix[1][i] == '#':
                    botptr = 1
                    botctr += 1
                    if matrix[0][i] == '#':
                        botptr = 0
                        botctr += 1
                elif botctr != 0:
                    botalive = False
    if topctr == total_hash or botctr == total_hash:
        print("yes")
    else:
        print("no")
