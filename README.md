# QPRS Experiment Code

## Description

This repository contains the experimental code accompanying the paper:

**"Query Structure as a Privacy Risk: Measuring Information Leakage in Encrypted NoSQL Databases."**

The code generates a synthetic dataset, creates a query workload, computes the Query Privacy Risk Score (QPRS), and reproduces the experimental results presented in the manuscript.

---

## Dataset Information

The experiments use a synthetic dataset containing:

- 300,000 records
- 1,200 generated NoSQL queries
- Low, medium, and high query complexity levels

No real or sensitive data are included.

---

## Code Information

### Files

- `generate_dataset.py` – Generates the synthetic dataset.
- `queries_generator.py` – Generates the query workload.
- `qprs_experiment.py` – Computes QPRS values and performs the experiments.

### Folders

- `figures/` – Figures used in the paper.
- `results/` – Experimental outputs.

---

## Requirements

- Python 3.9+
- pandas
- numpy
- matplotlib

Install the required packages:

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
5. Save the generated results and figures.

---

## Citation

If you use this code, please cite:

Aljuaid, N.

*Query Structure as a Privacy Risk: Measuring Information Leakage in Encrypted NoSQL Databases.*

---

## License

MIT License.

---

## Contributions

Contributions and suggestions are welcome through GitHub Issues or Pull Requests.
