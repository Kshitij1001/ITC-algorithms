import itc_basics as b


class Node:
    def __init__(self, pr, sy):
        self.prob = pr
        self.symb = sy
        self.code = []
        self.p1: Node = None
        self.p2: Node = None

    def L(self):
        return len(self.code)


probs = b.probInput()  # [0.25, 0.15, 0.12, 0.1, 0.08, 0.3]
symbs = b.symbInput()  # ['m2', 'm3', 'm4', 'm5', 'm6', 'm1']
while True:
    minOrmax: str = input('Minimum variance(1) or maximum variance(2)? (enter either 1 or 2)')
    if not (minOrmax == '1' or minOrmax == '2'):
        print(minOrmax + ' is an invalid option')
    else:
        break

gen0 = []
for x in range(len(probs)):
    gen0.append(Node(probs[x], symbs[x]))
gen0.sort(key=lambda y: y.prob, reverse=True)

ranks = [gen0]
gen: list = gen0
print([pop.symb for pop in gen])

for i in range(len(gen0) - 2):
    print([pop.prob for pop in gen])
    sumPro = gen[-2].prob + gen[-1].prob
    new = Node(sumPro, None)
    new.p1, new.p2 = gen[-2], gen[-1]
    gen = gen[:-2]
    flg = True
    if minOrmax == '1':
        # For minimum variance
        for k in range(len(gen)):
            if sumPro >= gen[k].prob:
                gen = gen[:k] + [new] + gen[k:]
                flg = False
                break
        if flg:
            gen.append(new)
    else:
        # For maximum variance
        for k in range(len(gen) - 1, -1, -1):
            if sumPro <= gen[k].prob:
                gen = gen[:k + 1] + [new] + gen[k + 1:]
                flg = False
                break
        if flg:
            gen = [new] + gen
    if len(gen) == 0:
        break
    ranks.append(gen)
print([pop.prob for pop in ranks[-1]])
ranks[-1][0].code, ranks[-1][1].code = [0], [1]


def backCode(lol: Node):
    if not (lol.p1 is None):
        lol.p1.code = lol.code + [0]
        lol.p2.code = lol.code + [1]
        backCode(lol.p1)
        backCode(lol.p2)


backCode(ranks[-1][0])
backCode(ranks[-1][1])

for i in gen0:
    print(i.symb, i.code, i.L(), sep=': ')
h = b.h(probs)
var, Lbar = b.varMean([n.prob for n in gen0], [n.L() for n in gen0])
print('Entropy is: ', h)
print('Average length is: ', Lbar)
print('Variance is: ', var)
print('Efficiency is: ', h * 100 / Lbar, '%')
