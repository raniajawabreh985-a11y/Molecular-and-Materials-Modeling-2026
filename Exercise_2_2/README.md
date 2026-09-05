
# Exercise II.2: Automated Cutoff Energy Convergence Test for Silicon

## Overview
Automated plane-wave cutoff energy ($E_{\text{cut}}$) convergence test for Diamond-structure Silicon using Quantum ESPRESSO and ASE[cite: 1].

## Convergence Results

| Cutoff Energy $E_{\text{cut}}$ (Ry) | Total Energy (eV) |
| :--- | :--- |
| **20** | -310.700205 |
| **30** | -310.724546 |
| **40** | -310.726498 |
| **50** | -310.727313 |
| **60** | -310.727631 |
| **70** | -310.727817 |
| **80** | -310.727973 |

* **Convergence Threshold:** Total energy converges within $1\text{ meV/atom}$ at **$E_{\text{cut}} = 40\text{--}50\text{ Ry}$**.

## Execution

To run the calculation script directly:

```bash
python3 convergence_test_si.py
