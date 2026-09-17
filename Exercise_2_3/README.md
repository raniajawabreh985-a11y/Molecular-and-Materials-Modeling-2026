# TASK 3: Cell relaxation (QE and ASE)

## Overview

In this task, we will relax the silicon experimental unit cell to determine its ground state structure, allowing both lattice parameters and atomic positions to adjust freely. 

We will perform this using two distinct methods: direct relaxation through Quantum ESPRESSO (QE) and by ASE using QE as a calculator.

## Results

| Property | Value |
| :--- | :--- |
| **Total Energy** | `-230.280072 eV` |
| **ASE-style Max Force (norm)** | `0.006204 eV/Å` |
| **QE-style Max Force** | `0.000000 eV/Å` |
| **Pressure** | `0.489860 kbar` |

## Execution

* **Direct QE run:**
  ```bash
  pw.x < cell_relaxation_si.in > cell_relaxation_si_direct.out
