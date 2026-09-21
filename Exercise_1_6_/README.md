## Overview
Quantitative comparison of bond energies calculated using the Atomic Simulation Environment (ASE) with the EMT potential calculator.

## Results

| System / Molecule | Process / Bond Type | Calculated Energy (eV) | Calculated Bond Energy (kJ/mol) |
| :--- | :--- | :---: | :---: |
| **Ethane ($\text{C}_2\text{H}_6$)** | $\text{C-C}$ Bond Dissociation | 0.8680 | 83.75 |
| **Methane ($\text{CH}_4$)** | $\text{C-H}$ Bond Dissociation | 3.1929 | 308.07 |

### Detailed Species Energy Breakdown

| Molecule / Radical / Atom | Total Potential Energy (eV) |
| :--- | :---: |
| **Ethane ($\text{C}_2\text{H}_6$)** | 3.0789 |
| **Methane ($\text{CH}_4$)** | 1.9906 |
| **Methyl Radical ($\text{CH}_3^\bullet$)** | 1.9735 |
| **Hydrogen Atom ($\text{H}^\bullet$)** | 3.2100 |

## Execution

```bash
python3 methane_CH_bond_en.py


