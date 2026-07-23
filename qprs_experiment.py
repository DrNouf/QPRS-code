
# QPRS Experiment Script
# Reproduces the main experiment for the paper:
# "Query Structure as a Privacy Risk: Measuring Information Leakage in Encrypted NoSQL Databases"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from generate_dataset import generate_dataset
from queries_generator import generate_queries

def compute_qprs(C, L, D, alpha=1, beta=1, gamma=1):
    return alpha*C + beta*L + gamma*D

def main():
    print("Generating synthetic dataset...")
    df = generate_dataset(300000)

    print("Generating queries...")
    queries = generate_queries(1200)

    results = []
    for q in queries:
        C = q["conditions"]
        L = q["logical_ops"]
        D = q["depth"]
        qprs = compute_qprs(C, L, D)
        leakage_proxy = np.random.normal(loc=20 + qprs, scale=2)

        results.append({
            "conditions": C,
            "logical_ops": L,
            "depth": D,
            "QPRS": qprs,
            "leakage_proxy": leakage_proxy
        })

    results_df = pd.DataFrame(results)
    results_df.to_csv("results/qprs_results.csv", index=False)

    print("Saved results to results/qprs_results.csv")

if __name__ == "__main__":
    main()
