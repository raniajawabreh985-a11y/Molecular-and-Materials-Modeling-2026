# Exercise II.7: Work Function of Graphene

## Overview
Calculation of the electrostatic potential profile and determination of the work function ($WF$) for a pristine monolayer graphene slab using Quantum ESPRESSO (`pw.x`, `pp.x`, and `average.x`).

## Calculation Parameters
| Parameter | Value |
| :--- | :--- |
| **System** | Monolayer Graphene Slab |
| **Plane-wave Cutoff (`ecutwfc`)** | $40\text{ Ry}$ |
| **Charge Density Cutoff (`ecutrho`)** | $320\text{ Ry}$ |
| **K-point Mesh** | $12 \times 12 \times 1$ |
| **Vacuum Spacing** | $\sim 15\text{ \AA}$ ($z\text{-axis}$) |

## Execution Commands
| Step | Tool / Command |
| :--- | :--- |
| **1. Main Script Execution** | `python3 work_function.py > work_function.out` |
| **2. SCF Calculation** | `mpirun -np 2 /home/user/miniconda3/bin/pw.x -in espresso.pwi > espresso.pwo` |
| **3. Extract Potential Grid** | `/home/user/miniconda3/bin/pp.x < pp.in > pp.out 2>&1` |
| **4. Planar Averaging** | `/home/user/miniconda3/bin/average.x < average.in > average.out 2>&1` |

## Results & Values
| Quantity | Calculated Value | Reference / Standard |
| :--- | :--- | :--- |
| **Fermi Level ($E_F$)** | $-1.7174\text{ eV}$ | — |
| **Vacuum Potential ($V_{\text{vacuum}}$)** | $+2.5230\text{ eV}$ ($0.18545\text{ Ry}$) | — |
| **Work Function ($WF = V_{\text{vacuum}} - E_F$)** | $\mathbf{4.24\text{ eV}}$ | $4.56 \pm 0.10\text{ eV}$ |

## Output Artifacts
| File / Path | Description |
| :--- | :--- |
| `potential_plot.png` | Planar and macroscopic average of the electrostatic potential along the $z$-direction |
| `potential_results/avg.dat` | Data file containing planar-averaged potential values |
| `potential_results/electrostatic_potential` | 3D real-space electrostatic potential grid |
