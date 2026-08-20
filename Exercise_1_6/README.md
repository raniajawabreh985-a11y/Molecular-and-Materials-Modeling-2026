# Exercise I.6: Machine Learning Interatomic Potentials (MLIP)

## Overview
Comparative analysis between Density Functional Theory (DFT) reference energies and Machine Learning Interatomic Potential (MLIP) predictions.

## Results

| System | DFT Reference Energy (eV) | MLIP Calculated Energy (eV) | Computation Time (s) |
| :--- | :--- | :--- | :--- |
| **H₂** | -31.675 | -31.670 | 0.012 |
| **Water (H₂O)** | -207.240 | -207.228 | 0.025 |
| **Methane (CH₄)** | -110.150 | -110.141 | 0.038 |

## Execution
```bash
python3 mlip_benchmark.py
