import itc_basics as b

probabilities: list = b.probInput()
symbols: list = b.symbInput()

toEncode = input('enter the word to encode: ').split(' ')

ladder: list = [0]
for i in probabilities:
    ladder.append(round(i + ladder[-1], 9))
ladder[-1] = 1
print(ladder)
for k in range(len(toEncode)):
    for i in range(len(symbols)):
        if toEncode[k] == symbols[i]:
            lower = ladder[i]
            upper = ladder[i + 1]
            gap = round(upper - lower, 9)
            ladderNew = [lower]
            for j in probabilities:
                ladderNew.append(round(ladderNew[-1] + j * gap, 9))
            ladderNew[-1] = upper
            ladder = ladderNew
            break
    print(ladder)
ans = (ladder[-1] + ladder[0]) / 2
print('The encoded value is: ', ans)
print('The encoded binary value is: ' + b.probability_in_binary(ans))
