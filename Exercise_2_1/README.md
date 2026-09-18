# Exercise II.1: Total Energy Calculation of the Silicon Unit Cell

## Overview
Total energy calculation of the bulk Silicon (Si) unit cell using Quantum ESPRESSO driven by ASE[cite: 1].

## Results

| Property | Value |
| :--- | :--- |
| **Lattice Constant ($a$)** | $5.43\text{ \AA}$ |
| **Crystal Structure** | Diamond (FCC) |
| **Plane-Wave Cutoff Energy ($E_{\text{cut}}$)** | $40\text{ Ry}$ |
| **Total Energy** | $-310.726498\text{ eV}$ |

### Challenge Results (Effect of Pseudopotential Change)

By changing the pseudopotential to `Si.upf` and running the SCF calculation:

| Property | Value |
| :--- | :--- |
| **Pseudopotential** | `Si.upf` |
| **Total Energy** | $-227.715035\text{ eV}$ |
| **Fermi Level** | $6.822200\text{ eV}$ |

> **Note:** The shift in total energy is expected due to the different pseudo-atom valence setup in the updated `Si.upf` pseudopotential file.

## Execution

To run the calculation script directly:

```bash
python3 si_ase.py
