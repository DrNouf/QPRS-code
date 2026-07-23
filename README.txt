
QPRS Experiment Code

This repository contains the experimental code used in the paper:

Query Structure as a Privacy Risk: Measuring Information Leakage in Encrypted NoSQL Databases

Files
-----
generate_dataset.py : generates the synthetic dataset (300,000 records)
queries_generator.py : creates the query workload (1,200 queries)
qprs_experiment.py : runs the experiment and computes QPRS values

Folders
-------
figures/ : figures used in the paper
results/ : experiment outputs

Requirements
------------
Python 3.9+
pandas
numpy
matplotlib

Run
---
python qprs_experiment.py
