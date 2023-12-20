import random
import math
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


def shuffle(old_state, n):
    first_coordinate = random.randint(0, n - 1)
    second_coordinate = random.randint(0, n - 1)

    new_state = old_state[::]
    new_state[first_coordinate] = old_state[second_coordinate]
    new_state[second_coordinate] = old_state[first_coordinate]

    return new_state


def SimAnnealing(graph, n, x):
    T = 5000
    a = 0.999
    limit = 1000
    count = 0

    while (count < limit):
        new_state = shuffle(x, n)
        if (f(new_state, graph) - f(x, graph)) < 0:
            x = new_state
        else:
            diff_f = f(new_state, graph) - f(x, graph)
            p = math.e ** (-(diff_f / T))
            if random.random() <= p:
                x = new_state
                T *= a
        count += 1
    return f(x, graph)





if __name__ == '__main__':
    n = 2000
    s = 0
    for i in range(50):
        graph = graph_generator(n)
        initial_x = [int(i) for i in range(n)]
        start = time.time()
        r = SimAnnealing(graph, n, initial_x)
        finish = time.time()
        s += finish - start
        print(finish - start)




