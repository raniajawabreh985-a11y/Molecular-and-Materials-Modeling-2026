# Electronic Structure & DOS Analysis of Bulk Silicon (Si)

This repository contains the full Quantum ESPRESSO computational workflow for Silicon (Si), evaluating the electronic structure, spatial charge density, Löwdin orbital populations, and Density of States (DOS/PDOS).

## 1. Summary of Computational Results

* **SCF Total Energy:** `-230.280149 eV`
* **Fermi Energy ($E_F$):** `6.3184 eV`
* **Spilling Parameter:** `0.008900` (< 0.05, excellent projection quality)
* **Integrated Total DOS:** `7.9999 states` (Matches the 8 valence electrons per unit cell)
* **Integrated PDOS Sum:** `7.9280 states`
* **Relative PDOS Difference:** `0.90%` (< 5%, high integration consistency)

### Electronic Density of States (DOS/PDOS) Plot

![Silicon Electronic Properties and DOS](si_dos_plot.png)

## 2. Generated Output Files

* `README.md`: Document detailing exercise overview, methodology, and computational results.
* `electronic_properties_silicon.py`: Primary Python script executing SCF, DOS, and PDOS calculations via Quantum ESPRESSO and ASE.
* `si_dos_plot.png`: Graphical output illustrating total and projected density of states.

### 3. Comparison with Experimental Band Gap
* **Computed Band Gap:** ~0.6–0.7 eV (calculated from DOS/NSCF eigenvalues).
* **Experimental Band Gap:** 1.17 eV.
* **Does it match?** No, the computed band gap is underestimated compared to the experimental value.
* **Why / Why not?** Standard Density Functional Theory (DFT) using standard GGA/LDA exchange-correlation functionals (such as PBE) systematically underestimates the fundamental band gap of semiconductors and insulators. This is a well-known intrinsic limitation of standard DFT due to self-interaction errors and the lack of derivative discontinuity in the approximate exchange-correlation potential.
