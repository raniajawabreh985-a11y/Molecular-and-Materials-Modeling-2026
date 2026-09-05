# Electronic Properties of Aluminium (Al) - DOS Calculation

## Overview
Calculation of the electronic structure and Density of States (DOS) for Bulk Aluminium (FCC lattice) using Density Functional Theory (DFT) with Quantum ESPRESSO via the Atomic Simulation Environment (ASE).

## Objectives
* Perform Self-Consistent Field (SCF) calculations for FCC Aluminium.
* Determine the total potential energy and Fermi level ($E_F$).
* Calculate and plot the Electronic Density of States (DOS).

## Methodology & Calculation Setup
* **Structure:** Bulk Aluminium (FCC, $a = 4.05\text{ \AA}$)
* **Pseudopotential:** `Al.pz-vbc.UPF`
* **Exchange-Correlation Functional:** LDA
* **K-points Mesh:** $8 \times 8 \times 8$
* **Wavefunction Cutoff ($e_{\text{cutwfc}}$):** 30.0 Ry
* **Smearing:** Marzari-Vanderbilt ($0.02\text{ Ry}$)

## Results
* **Total Energy:** `-56.986773 eV`
* **Fermi Energy ($E_F$):** `7.627100 eV`
* **DOS Plot:** Computed and generated successfully as `al_dos_plot.png`.

## Execution & How to Run

To run the calculation and generate the output log alongside the DOS plot, execute:

```bash
python3 electronic_properties_al.py > electronic_properties_al.out
