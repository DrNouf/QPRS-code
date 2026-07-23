# QPRS Experiment Code

## Description

This repository contains the experimental code accompanying the paper:

**"Query Structure as a Privacy Risk: Measuring Information Leakage in Encrypted NoSQL Databases."**

The code generates a synthetic dataset, creates a query workload, computes the Query Privacy Risk Score (QPRS), and reproduces the experimental results and figures presented in the paper.

---

## Files

- `generate_dataset.py` – Generates the synthetic dataset (300,000 records).
- `queries_generator.py` – Generates the query workload (1,200 queries).
- `qprs_experiment.py` – Computes QPRS values and reproduces the experiments.

---

## Folders

- `figures/` – Figures used in the manuscript.
- `results/` – Experimental outputs.

---

## Dataset Information

The experiments use a synthetic dataset containing **300,000 records** and **1,200 generated queries**. No real or sensitive data are included.

---

## Requirements

- Python 3.9+
- pandas
- numpy
- matplotlib

Install dependencies using:

```bash
pip install pandas numpy matplotlib
```

---

## Usage

Run the experiment using:

```bash
python qprs_experiment.py
```

The script generates the experimental results and figures reported in the paper.

---

## Methodology

1. Generate the synthetic dataset.
2. Generate the query workload.
3. Compute the Query Privacy Risk Score (QPRS).
4. Perform the experimental evaluation.
5. Save the results and figures.

---

## Citation

If you use this code, please cite:

> Aljuaid, N. *Query Structure as a Privacy Risk: Measuring Information Leakage in Encrypted NoSQL Databases.

---

## License

This project is released under the MIT License.

---

## Contributions

Contributions and suggestions are welcome through GitHub Issues or Pull Requests.
