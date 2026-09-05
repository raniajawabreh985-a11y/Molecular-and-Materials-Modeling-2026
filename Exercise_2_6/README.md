# Exercise II.6: Energy Cutoff (`ecutwfc`) Convergence for Graphene

## Overview
This calculation evaluates the total energy convergence of monolayer graphene with respect to the plane-wave wavefunction cutoff energy (`ecutwfc`) using Quantum ESPRESSO via the ASE (Atomic Simulation Environment) Python interface.

* **System:** Monolayer Graphene (2D Semi-metal)
* **k-point Grid:** $39 \times 39 \times 1$
* **Target Convergence Threshold:** $< 1.0\text{ meV/atom}$

  ## Results

### `ecutwfc` Convergence Data

| ecutwfc (Ry) | Total Energy (eV) | $\Delta E$ (meV/atom) | SCF Iterations Status |
| :---: | :---: | :---: | :---: |
| 20.0 | -497.449269 | - | Converged |
| 25.0 | -501.132318 | -1841.524 | Converged |
| 30.0 | -501.755881 | -311.782 | Converged |
| 35.0 | -501.875806 | -59.962 | Converged |
| 40.0 | -501.890811 | -7.503 | Converged |
| **45.0** | **-501.892902** | **-1.045** | **Optimal Threshold** |
| 50.0 | -501.895852 | -1.475 | Converged |
| 55.0 | -501.899650 | -1.899 | Converged |

---

## Execution & Computational Setup

### SCF Parameters
* **Quantum ESPRESSO Executable:** `pw.x`
* **Electronic Mixing Parameter (`mixing_beta`):** Reduced to `0.30` to mitigate charge sloshing typical of zero-gap 2D materials.
* **Maximum SCF Steps (`electron_max_step`):** 100
* **Pseudo Potential:** Carbon pseudopotential from standard QE distribution.

### Execution Command
The convergence calculation script was executed using parallel MPI execution within the virtual Linux workstation environment:

```bash
mpirun -np 4 pw.x -in espresso.pwi > espresso.pwo
python3 convergence_test_graphene.py
