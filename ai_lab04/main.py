from GA import GA
from random import randint

def readNetwork(fileName):
    network = {}
    mat = []
    file = open('./files/' + fileName, 'r')
    n = int(file.readline())
    network['noNodes'] = n
    
    for _ in range(n):
        data = file.readline()
        values = data.split(',')
        line = []
        for v in values:
            line.append(int(v))
        mat.append(line)
    network['mat'] = mat

    return network

def initParams(fileName):
    network = readNetwork(fileName)
    param = {
        'popSize': 20,
        'noGen': 500,
        'network': network
    }
    problParam = {
        'function': solve,
        'noNodes': network['noNodes']
    }
    
    return param, problParam

def solveDestination(repres, network, src, dest):
    mat = network['mat']
    cost = 0

    for i in range(src, dest - 1):
        node = repres[i]
        nextNode = repres[i + 1]
        cost += mat[node - 1][nextNode - 1]
    if src == 1 and dest == network['noNodes']:
        cost += mat[repres[-1] - 1][repres[0] - 1]

    return cost

def solve(repres, network):
    mat = network['mat']
    cost = 0

    for i in range(network['noNodes'] - 1):
        node = repres[i]
        nextNode = repres[i + 1]
        cost += mat[node - 1][nextNode - 1]
    cost += mat[repres[-1] - 1][repres[0] - 1]

    return cost

def initRepres(network):
    repres = []
    
    for i in range(network['noNodes']):
        value = randint(0, network['noNodes'] - 1)
        repres.append(value)
    
    for i in range(len(repres)):
        for j in range(len(repres)):
            if network['mat'].item(i, j) == 1:
                repres[j] = repres[i]

    return repres

def main():
    #fileName = 'easy1.txt'
    #fileName = 'medium.txt'
    fileName = 'hard_02.txt'
    
    param, problParam = initParams(fileName)
    ga = GA(param, problParam)
    ga.initialisation()
    ga.evaluation()

    for i in range(param['noGen'] - 1):
        ga.oneGenerationElitism()
    print(ga.bestChromosome())

if __name__ == '__main__':
    main()