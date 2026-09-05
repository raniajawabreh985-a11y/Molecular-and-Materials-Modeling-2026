# Exercise II.5: Crystal Defect & Vacancy Formation Energy

## Overview
Calculation of point defect energetics and single vacancy formation energy ($E_{\text{vac}} = E_{\text{defect}} - (N - 1)\mu$) in crystal lattices using Density Functional Theory (DFT).

## Objectives
* Construct pristine and defective supercells for crystal structure modeling.
* Perform structural relaxation for both pristine and defected systems.
* Calculate the vacancy formation energy ($E_{\text{vac}}$) accurately.

## Methodology & Equations
The vacancy formation energy is computed using the standard relation:

$$E_{\text{vac}} = E_{\text{defect}} - \left(\frac{N - 1}{N}\right) E_{\text{bulk}}$$

Where:
* $E_{\text{defect}}$: Total energy of the supercell containing a single atomic vacancy.
* $E_{\text{bulk}}$: Total energy of the pristine bulk supercell.
* $N$: Total number of atoms in the pristine supercell.

## Execution & How to Run

To run the calculation script, ensure your Python environment with `ASE` and `Quantum ESPRESSO` (`pw.x`) is activated, then execute:

```bash
python3 defect_vacancy_calc.py > defect_vacancy_calc.out
