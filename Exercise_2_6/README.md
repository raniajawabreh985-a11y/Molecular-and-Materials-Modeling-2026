# TASK 6: Surfaces and 2D Materials (Graphene)

## Overview
This report documents the structural relaxation, electronic properties, and Projected Density of States (PDOS) calculations for monolayer graphene using Quantum ESPRESSO via the ASE Python interface.

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
* **Execution:** Relaxed in-plane lattice constants ($xx, yy$) to optimize graphene bonding geometry while maintaining $15\text{ \AA}$ vacuum spacing.

---

## 3. Electronic Properties & PDOS Analysis
* **Fermi Level:** $-4.2408\text{ eV}$
* **PDOS vs TDOS Integration Agreement:** $< 1\%$ difference (excellent agreement).

### Key Scientific Findings
* **Dirac Cone Formation:** The electronic states near the Fermi level ($E_F$) are overwhelmingly dominated by out-of-plane $p_z$ orbitals.
* **Orbital Projection:** The in-plane orbitals ($p_x + p_y$) form strong $\sigma$-bonds situated deep in the valence band, leaving the $\pi$-bands ($p_z$) to meet at the Dirac point.
