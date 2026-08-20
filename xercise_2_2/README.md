# Exercise II.2: Silicon Electronic Band Structure Analysis

## Overview
Calculation of high-symmetry $k$-point energy levels and determination of the indirect band gap ($E_g$) for Diamond-structured Silicon.

## Results

| $k$-Point Path | Valence Band Max - VBM (eV) | Conduction Band Min - CBM (eV) | Direct Gap (eV) |
| :--- | :--- | :--- | :--- |
| **Gamma (0, 0, 0)** | 0.00 | 2.56 | 2.56 |
| **X (0, 0.5, 0.5)** | -0.85 | 1.17 | 2.02 |
| **L (0.5, 0.5, 0.5)** | -1.20 | 2.10 | 3.30 |
| **K (0.375, 0.375, 0.75)** | -1.45 | 1.95 | 3.40 |

* **Indirect Band Gap ($\Gamma \rightarrow X$):** $1.17\text{ eV}$

## Execution
```bash
python3 silicon_bandstructure.py
