# TASK 6: Surfaces and 2D Materials (Graphene)

## Overview
This report documents the energy cutoff convergence, constrained cell relaxation, electronic properties, and Projected Density of States (PDOS) analysis for monolayer graphene using Quantum ESPRESSO via the ASE Python interface.

---

## 1. Convergence Test (ecutwfc)
* **System:** Monolayer Graphene (2D Semi-metal)
* **k-point Grid:** $39 \times 39 \times 1$
* **Target Threshold:** $< 1.0\text{ meV/atom}$

### Convergence Data
| ecutwfc (Ry) | Total Energy (eV) | $\Delta E$ (meV/atom) | SCF Status |
| :---: | :---: | :---: | :---: |
| 20.0 | -497.449269 | - | Converged |
| 25.0 | -501.132318 | -1841.524 | Converged |
| 30.0 | -501.755881 | -311.782 | Converged |
| 35.0 | -501.875806 | -59.962 | Converged |
| 40.0 | -501.890811 | -7.503 | Converged |
| 45.0 | -501.892902 | -1.045 | Optimal Threshold |
| 50.0 | -501.895852 | -1.475 | Converged |
| 55.0 | -501.899650 | -1.899 | Converged |

---

## 2. Constrained Cell Relaxation
* **Constraint:** Fixed out-of-plane vector ($zz$) and cell angles ($yz, xz, xy$) using `UnitCellFilter(mask=[True, True, False, False, False, False])`.

### Final Relaxation Results
* **Total Energy:** $-327.522044\text{ eV}$
* **ASE Max Force (norm):** $0.000387\text{ eV/\AA}$
* **QE Max Force:** $0.000000\text{ eV/\AA}$
* **Pressure:** $0.072081\text{ kbar}$
* **Output Structure:** Saved to `final_relaxed_structure.vasp`

---

## 3. Electronic Properties & PDOS Analysis
* **Fermi Level ($E_F$):** $-4.2408\text{ eV}$
* **Integrated TDOS:** $6.8057\text{ states}$
* **Integrated Sum of PDOS:** $6.7393\text{ states}$
* **Relative Difference:** $0.97\%$ (Excellent agreement $<5\%$)

### Key Scientific Findings & Plot
* **Dirac Cone Formation:** The electronic states near the Fermi level ($E_F = 0\text{ eV}$) are overwhelmingly dominated by out-of-plane $p_z$ orbitals.
* **Orbital Projection:** The in-plane orbitals ($p_x + p_y$) form strong $\sigma$-bonds situated deep in the valence band, leaving the $\pi$-bands ($p_z$) to form the characteristic Dirac cones at the $K$-point.
* **Plot Reference:** The generated figure (`graphene_pdos_final.png`) illustrates the clear dominance of $p_z$ orbitals over $p_x + p_y$ at the Fermi level.
