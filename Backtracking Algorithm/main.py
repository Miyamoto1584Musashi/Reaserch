from random import randint
import itertools
import time

def graph_generator(n):
    graph = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if graph[i][j] == 0:
                    graph[i][j] = randint(1, 10000)
                    graph[j][i] = graph[i][j]
    return graph

def f(x, graph):
    sum_distance = 0
    for i in range(len(x) - 1):
        sum_distance += graph[x[i]][x[i + 1]]
    sum_distance += graph[x[0]][x[-1]]
    return sum_distance
def tst(initial_x, graph):
    current_f = f(initial_x, graph)
    final_x = initial_x
    for current_x in itertools.permutations(initial_x):
        next_f = f(current_x, graph)
        if next_f < current_f:
            current_f = next_f
            final_x = current_x
    final_f = current_f
    return final_f, final_x

if __name__ == '__main__':

    graph =[[0, 9176, 8711, 1596, 8304], [9176, 0, 377, 9861, 9113], [8711, 377, 0, 7860, 7139], [1596, 9861, 7860, 0, 5143], [8304, 9113, 7139, 5143, 0]]
    initial_x = [int(i) for i in range(len(graph))]
    print(tst(initial_x, graph), end=' ')

    
