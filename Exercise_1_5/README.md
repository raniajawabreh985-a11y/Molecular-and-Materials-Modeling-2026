# Exercise I.5: Verification of VSEPR Theory with MM, seQM (MOPAC), and DFT (NWChem)

## Overview
Quantitative comparison of molecular geometry parameters (bond angles) predicted by VSEPR theory against Molecular Mechanics (Avogadro2), semi-empirical Quantum Mechanics (MOPAC), and Density Functional Theory (NWChem).

## Results

| Molecule & Geometry | MM (Avogadro2) | seQM (MOPAC) | DFT (NWChem) | VSEPR Prediction |
| :--- | :--- | :--- | :--- | :--- |
| **Methane ($\text{CH}_4$)** | 109.5° | 109.4° | 109.5° | 109.5° |
| **Ammonia ($\text{NH}_3$)** | 106.8° | 107.1° | 106.7° | 107.3° |
| **Water ($\text{H}_2\text{O}$)** | 104.2° | 104.8° | 104.5° | 104.5° |

## Execution
```bash
python3 vsepr_verification.py
