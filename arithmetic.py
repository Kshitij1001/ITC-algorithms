import itc_basics as b

probabilities: list = b.probInput()
symbols: list = b.symbInput()

ladder: list = [0]
for i in probabilities:
    ladder.append(round(i + ladder[-1], 9))
ladder[-1] = 1
while True:
    encode_or_decode: str = input('Wanna encode(1) or decode(2)?   ....   (Enter either 1 or 2) ')
    if not (encode_or_decode == '1' or encode_or_decode == '2'):
        print('Invalid input')
    else:
        break


def newLadder(oldLadder: list, numb: int):
    gapp = round(oldLadder[numb + 1] - oldLadder[numb], 9)
    nextLadder: list = [oldLadder[numb]]
    for jj in probabilities:
        nextLadder.append(round(nextLadder[-1] + jj * gapp, 9))
    nextLadder[-1] = oldLadder[numb + 1]
    return nextLadder


if encode_or_decode == '1':
    toEncode = input('enter the sequence of symbols to encode: ').split(' ')
    print(ladder)
    for k in toEncode:
        for i in range(len(symbols)):
            if k == symbols[i]:
                ladder = newLadder(ladder, i)
                break
        print(ladder)
    ans = (ladder[-1] + ladder[0]) / 2
    print('The encoded value (mean) is: ', ans, 'and for lower bound is: ', ladder[0])
    print('The encoded binary value (mean) is: ' + b.probability_in_binary(
        ans) + ' and for lower bound is: ' + b.probability_in_binary(ladder[0]))
else:
    message = []
    toFind = float(input('Enter probability to find out: '))
    print(ladder)
    done = 0
    for i in range(100):
        for j in range(len(symbols)):
            if ladder[j] <= toFind < ladder[j + 1]:
                message.append(symbols[j])
                if ladder[j] == toFind:
                    done += 1
                    if done == 2:
                        break
                ladder = newLadder(ladder, j)
                break
        if done == 2:
            break
        print(ladder)
    print('The decoded message is: ', message)
