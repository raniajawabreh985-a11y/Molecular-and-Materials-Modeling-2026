
# Exercise II.2: Automated Cutoff Energy and K-points Convergence Test for Silicon

## Overview
Automated plane-wave cutoff energy ($E_{\text{cut}}$) and K-points grid convergence tests for Diamond-structure Silicon using Quantum ESPRESSO and ASE.

---

## TASK 2.1: Convergence Test Results
- **Total SCF Runs Performed:** 23 runs (9 for cutoff energy testing, 14 for K-points testing).
- **Converged Cutoff Energy ($E_{\text{cut}}$):** 60 Ry (Threshold: $\Delta E < 0.01$ meV/atom).
- **Converged K-points Grid:** $15 \times 15 \times 15$.

### Cutoff Energy Convergence Data ($E_{\text{cut}}$)
| Cutoff Energy $E_{\text{cut}}$ (Ry) | Total Energy (eV) | $\Delta E$ (meV/atom) |
| :---: | :---: | :---: |
| 20.0 | -310.724432 | 9.818 |
| 25.0 | -310.744068 | 2.165 |
| 30.0 | -310.748397 | 0.546 |
| 35.0 | -310.750351 | 0.431 |
| 40.0 | -310.750691 | 0.170 |
| 45.0 | -310.751160 | 0.235 |
| 50.0 | -310.751479 | 0.159 |
| 55.0 | -310.751477 | 0.001 * |
| 60.0 | -310.751477 | Converged |

---

## TASK 2.2: Forces and Stress Calculation (Unshifted Lattice)
- **Total Force:** 0.000000 Ry/au
- **Total Stress (Pressure):** 20.56 kbar

---

## TASK 2.3: Manual Atomic Displacement (Shifted Cell)
- **Displacement applied:** Si atom 2 shifted by +0.02 along x-axis.
- **Computed Forces:**
  - Atom 1: `( 0.057135,  0.000000,  0.000000) Ry/au`
  - Atom 2: `(-0.057135,  0.000000,  0.000000) Ry/au`
- **Total Force:** 0.080802 Ry/au

---

## Challenge: Pseudopotentials Comparison
| Pseudopotential Type | Functional | Converged $E_{\text{cut}}$ (Ry) | Converged K-grid |
| :--- | :---: | :---: | :---: |
| `Si.pbe-n-rrkjus_psl.1.0.0.UPF` | PBE (USPP) | 60 | $15 \times 15 \times 15$ |
| `Si.pz-vbc.UPF` | LDA (NC) | 40 | $12 \times 12 \times 12$ |

---

## Execution
To run the calculation script directly:
```bash
python3 convergence_test_si.py

## Execution

To run the calculation script directly:

```bash
python3 convergence_test_si.py
