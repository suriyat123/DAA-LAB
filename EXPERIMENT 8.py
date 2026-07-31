

import heapq
from itertools import permutations

INF = float('inf')

def reduce_matrix(mat):
    """Reduce matrix and return reduction cost"""
    m = [row[:] for row in mat]
    n = len(m)
    cost = 0

    # Row reduction
    for i in range(n):
        row_min = min(m[i])
        if row_min != INF and row_min > 0:
            cost += row_min
            for j in range(n):
                if m[i][j] != INF:
                    m[i][j] -= row_min

    # Column reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))
        if col_min != INF and col_min > 0:
            cost += col_min
            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, cost


def tsp_brute_force(cost, n):
    """Find optimal TSP tour (used here for verification)."""
    cities = list(range(1, n))
    best_cost = INF
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]

        total = 0
        for i in range(n):
            total += cost[path[i]][path[i + 1]]

        if total < best_cost:
            best_cost = total
            best_path = path

    return best_path, best_cost


# -----------------------------
# Cost Matrix
# -----------------------------
cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

cities = ['A', 'B', 'C', 'D', 'E']
n = len(cost)

best_path, best_cost = tsp_brute_force(cost, n)

print("5-City TSP - Cost Matrix:\n")

print("     ", end="")
for c in cities:
    print(f"{c:>5}", end="")
print()

for i in range(n):
    print(f"{cities[i]:>3} ", end="")
    for value in cost[i]:
        if value == INF:
            print(f"{'INF':>5}", end="")
        else:
            print(f"{value:>5}", end="")
    print()

print("\nOptimal Tour:")
print(" -> ".join(cities[i] for i in best_path))

print("\nMinimum Cost:", best_cost)

print("\nPath Verification:")
for i in range(n):
    u = best_path[i]
    v = best_path[i + 1]
    print(f"{cities[u]} -> {cities[v]} : Cost = {cost[u][v]}")

