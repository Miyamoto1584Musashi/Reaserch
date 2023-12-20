import random
import time


def graph_generator(n):
    graph = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if graph[i][j] == 0:
                    graph[i][j] = random.randint(1, 10000)
                    graph[j][i] = graph[i][j]
    return graph

def f(x, graph):
    sum_distance = 0
    for i in range(len(x) - 1):
        sum_distance += graph[x[i]][x[i + 1]]
    sum_distance += graph[x[0]][x[-1]]
    return sum_distance

def probability(number, start, end):
    random_number = random.uniform(start, end)
    if random_number < number:
        return True
    else:
        return False
def parents_choice(population, graph):
    p = P(population, graph)
    s = 0
    for i in range(len(p)):
        s += p[i]
        if probability(s, 0, len(population) - 1):
            first_parent = population[i]
            break
    s = 0
    for i in range(len(p)):
        s += p[i]
        if probability(s, 0, len(population) - 1):
            second_parent = population[i]
            break

    parents = [first_parent, second_parent]
    return parents

def mutation(individual):
    first_individual_c = random.randint(0, len(individual) - 1)
    second_c = random.randint(0, len(individual) - 1)
    chromosome_individual = individual[first_individual_c]
    individual[first_individual_c] = individual[second_c]
    individual[second_c] = chromosome_individual

def crossing(first_parent, second_parent):
    q = random.randint(1, len(first_parent) - 1)
    first_descendant = first_parent[:q]
    for i in second_parent[q:]:
        if not (i in first_descendant):
            first_descendant.append(i)

    second_descendant = second_parent[:q]
    for i in first_parent[q:]:
        if not (i in second_descendant):
            second_descendant.append(i)
    descendants = [first_descendant + [i for i in first_parent if not(i in first_descendant)],
                   second_descendant + [i for i in second_parent if not(i in second_descendant)]]
    return descendants


def P(population, graph):
    p = [(1 - (f(population[i], graph) / sum([f(population[j], graph) for j in range(len(population))]))) for i in range(len(population))]
    return p

def creating_initial_population(size, n):
    x = []
    population = []
    for i in range(size):
        for j in range(n):
            x.append(j)
        new_x = x[::]
        random.shuffle(new_x)
        population.append(new_x)
        x.clear()
    return population

def new_population(population, probability_mutation):
    new_population = []

    for i in range(int(len(population) / 2)):
        parents = parents_choice(population, graph)
        descendants = crossing(parents[0], parents[1])
        new_population.append(descendants[0])
        new_population.append(descendants[1])

    for i in range(len(new_population)):
        if probability(probability_mutation, 0, 1):
            mutation(new_population[i])
        else:
            mutation(new_population[i])

    return new_population
def GeneticAlgorithm(population, graph):
    count = 0
    limit = 100
    probability_mutation = 0.25
    newPopulation = []
    while (count <= limit):
        newPopulation = new_population(population, probability_mutation)
        count += 1
    return min([f(individ, graph) for individ in newPopulation])

if __name__ == '__main__':
    n = 300
    size = 50
    s = 0
    for i in range(3):
        graph = graph_generator(n)
        population = creating_initial_population(size, n)
        start = time.time()
        t = GeneticAlgorithm(population, graph)
        finish = time.time()
        s += finish - start
    print(s / 3)




