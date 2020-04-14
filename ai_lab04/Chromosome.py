from random import randint, seed

class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam  # problParam has to store the number of nodes/cities
        self.__repres = self.generateARandomPermutation(self.__problParam['noNodes'])
        self.__fitness = 0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        # order XO
        pos1 = randint(-1, self.__problParam['noNodes'] - 1)
        pos2 = randint(-1, self.__problParam['noNodes'] - 1)
        
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if (el not in newrepres):
                if (len(newrepres) < self.__problParam['noNodes'] - pos1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        
        return offspring
    
    def generateARandomPermutation(self, n):
        permutation = []
        pos1 = randint(0, n - 1)
        pos2 = randint(0, n - 1)
    
        for i in range(n):
            permutation.append(i)
        aux = permutation[pos1]
        permutation[pos1] = permutation[pos2]
        permutation[pos2] = aux
    
        return permutation

    def mutation(self):
        # insert mutation
        pos1 = randint(0, self.__problParam['noNodes'] - 1)
        pos2 = randint(0, self.__problParam['noNodes'] - 1)
        
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + "\nFitness: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness