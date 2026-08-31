# Exercise I.2: Atomization Energy Calculation

## Overview
Calculation of atomization energies ($E_{\text{atomization}} = 2E_{\text{atom}} - E_{\text{molecule}}$) for diatomic molecules ($H_2$, $N_2$, $O_2$) using the ASE EMT calculator, compared against experimental literature data.

## Results & Literature Comparison

| System | Single Atom Energy (eV) | Diatomic Molecule Energy (eV) | Calculated $E_{\text{atomization}}$ (eV) | Literature $E_{\text{atomization}}$ (eV) |
| :---: | :---: | :---: | :---: | :---: |
| **$H_2$** | 3.2100 | 1.1589 | 5.2611 | ~ 4.52 |
| **$N_2$** | 5.1000 | 0.5488 | 9.6512 | ~ 9.79 |
| **$O_2$** | 4.6000 | 0.9227 | 8.2773 | ~ 5.12 |

## Analysis & Discussion
- **Formula:** $E_{\text{atomization}} = 2 \times E_{\text{atom}} - E_{\text{molecule}}$
- **Discussion:** The Effective Medium Theory (EMT) calculator provides a fast empirical approximation. Differences between calculated EMT atomization energies and experimental literature values arise because EMT is primarily designed for metallic bonding and simplified potential surfaces rather than highly covalent gas-phase molecules.

## Script Execution
```bash
python3 atomization_energy.py
