#!/usr/bin/env python3
import random
class markov:
    def __init__(self, name, stay, go, back):
        self.name = name
        self.stay = stay
        self.go = go
        self.back = back
rain = markov("rain", 2, 4, 3)
clear = markov("clear", 3, 2, 1)
snow = markov("snow", 4, 2, 3)
def weathergen(A, B, C):
    chain = [[A.name, A.stay, A.go, A.back], [B.name, B.stay, B.go, B.back], [C.name, C.stay, C.go, C.back]]
    random.shuffle(chain)
    i = 0
    w = 0
    e = 1
    print(chain)
    while i != 7:
        if random.randint(0,chain[w][e]) == chain[w][e]:
            print(chain[w][0])
            i += 1
            random.shuffle(chain)
        elif random.randint(0,chain[w][e+1]) == chain[w][e+1]:
            print(chain[w+1][0])
            i += 1
            random.shuffle(chain)
        elif random.randint(0,chain[w][e+2]) == chain[w][e+2]:
            print(chain[w+2][0])
            i += 1
            random.shuffle(chain)
        else:
            random.shuffle(chain)
weathergen(clear, rain, snow)
