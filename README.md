# QPRS: Query Privacy Risk Score

## Description

This repository contains the source code for the paper:

**"Query Structure as a Privacy Risk: Measuring Information Leakage in Encrypted NoSQL Databases."**

The project proposes the **Query Privacy Risk Score (QPRS)**, a metric for estimating privacy risks arising from the structure of encrypted NoSQL queries. The implementation generates synthetic datasets, creates query workloads, computes QPRS values, and evaluates their relationship with observable information leakage.

---

## Dataset Information

The experiments use a synthetic NoSQL dataset containing **300,000 records** and **1,200 generated queries** of varying complexity (low, medium, and high). No real or sensitive data are included.

---

## Code Information

The repository includes code for:

- Synthetic dataset generation
- Query workload generation
- QPRS calculation
- Baseline comparison
- Statistical analysis
- Figure generation

---

## Usage Instructions

1. Clone the repository:

```bash
git clone https://github.com/DrNouf/QPRS-code.git
cd QPRS-code
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the main script or Jupyter Notebook included in the repository to reproduce the experiments and figures.

---

## Requirements

- Python 3.9+
- numpy
- pandas
- matplotlib
- scipy
- scikit-learn

---

## Methodology

The workflow consists of:

1. Generate a synthetic dataset.
2. Generate query workloads.
3. Extract query structural features.
4. Calculate QPRS.
5. Compare QPRS with the baseline metric.
6. Perform statistical analysis and generate figures.

---

## Citation

If you use this code, please cite:

Aljuaid, N. *Query Structure as a Privacy Risk: Measuring Information Leakage in Encrypted NoSQL Databases.* (Submitted to PeerJ Computer Science)

---

## License

This project is released under the MIT License.

---

## Contributions

Contributions and suggestions are welcome through GitHub Issues or Pull Requests.
