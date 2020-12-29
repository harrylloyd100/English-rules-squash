import csv
import matplotlib.pyplot as plt
import random

def game(ra, rb):
    proba = (ra) / (ra +rb)
    scoreA = 0
    scoreB = 0
    serveA = False
    while True:
        if ((scoreA <= 9 or scoreB <= 9) and (scoreA >= 9 or scoreB >= 9)):
            break
        else:
            r = random.random()
            if r < proba and serveA == True:
                scoreA = scoreA + 1
            elif r > proba and serveA == True:
                serveA = False
            elif r > proba and serveA != True:
                scoreB = scoreB + 1
            elif r < proba and serveA != True:
                serveA = True
    return scoreA,scoreB

def winProb(ra, rb, n):
    wa = 0
    wb = 0
    for i in range(n):
        res = game(ra, rb)
        if res[0] > res[1]:
            wa += 1
        else:
            wb += 1
    return round(wa/n,2)

def data():
        list = []
        with open('test.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader ,None)
            for row in reader:
                list.append(eval("(" + row[0] + "," + row[1] + ")"))
            skills = list
        return skills

def plot(o):
    ra,rb = 0,0
    ploter, ok = [], []
    for tries in o:
        ra, rb = tries[0], tries[1]
        reso1 = int(ra)/int(rb)
        reso =  winProb(int(ra),int(rb), 100000)
        ploter.append(reso)
        ok.append(reso1)
    plt.plot(ok, ploter)
    plt.ylabel('Probability')
    plt.xlabel('rA/rB')
    plt.title('Probability of player A beating player B')
    plt.show()
