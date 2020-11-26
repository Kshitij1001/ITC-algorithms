import math as m


def lb(n):
    return m.log(n, 2)


def h(lst):
    return -sum([k * lb(k) for k in lst])


def mean(prob, l):
    return sum([prob[i] * l[i] for i in range(len(prob))])


def varMean(prob, l):
    av = mean(prob, l)
    return mean(prob, [k ** 2 for k in l]) - av ** 2, av


def probInput():
    return [float(x) for x in input('Enter probabilities: ').split(' ')]


def symbInput():
    return input('Enter symbols: ').split(' ')


def probability_in_binary(probability, bits_precision=10):
    ans: str = '0.'
    for i in range(bits_precision):
        probability *= 2
        x = int(probability)
        probability -= x
        ans = ans + str(x)
    return ans.rstrip('0')
