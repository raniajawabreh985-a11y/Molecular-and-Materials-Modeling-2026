# Exercise II.1: Energy Cutoff (`ecutwfc`) Convergence for Graphene

## Overview
This calculation evaluates the total energy convergence of monolayer graphene with respect to the plane-wave wavefunction cutoff energy (`ecutwfc`) using Quantum ESPRESSO via the ASE (Atomic Simulation Environment) python interface.

* **System:** Monolayer Graphene (2D Semi-metal)
* **k-point Grid:** $39 \times 39 \times 1$
* **Target Convergence Threshold:** $< 1.0\text{ meV/atom}$

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
