
import random

def generate_queries(n_queries=1200):

    queries = []

    for _ in range(n_queries):

        complexity = random.choice(["low","medium","high"])

        if complexity == "low":
            C = 1
            L = 0
            D = 1
        elif complexity == "medium":
            C = random.randint(2,3)
            L = random.randint(1,2)
            D = random.randint(1,2)
        else:
            C = random.randint(4,6)
            L = random.randint(2,4)
            D = random.randint(2,3)

        queries.append({
            "conditions": C,
            "logical_ops": L,
            "depth": D,
            "complexity": complexity
        })

    return queries
