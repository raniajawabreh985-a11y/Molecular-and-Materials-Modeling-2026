cat << 'EOF' > README.md
# Exercise II.7: Work Function of Graphene

## Overview
Calculation of the electrostatic potential profile and determination of the work function ($WF$) for a pristine monolayer graphene slab using Quantum ESPRESSO (`pw.x`, `pp.x`, and `average.x`).

## Calculation Parameters
| Parameter | Value |
| :--- | :--- |
| **System** | Monolayer Graphene Slab |
| **Plane-wave cutoff (ecutwfc)** | 40 Ry |
| **Charge density cutoff (ecutrho)** | 320 Ry |
| **K-point mesh** | $12 \times 12 \times 1$ |
| **Vacuum Spacing** | ~15 Å ($z$-axis) |

## Results

### Key Energy Levels
| Parameter | Value (eV) |
| :--- | :--- |
| **Fermi Energy ($E_{Fermi}$)** | -1.717400 |
| **Vacuum Potential ($V_{vacuum}$)** | 0.185449 |
| **Calculated Work Function ($WF$)** | **1.902849** |

## Formula
$$\text{Work Function} (WF) = V_{\text{vacuum}} - E_{\text{Fermi}}$$

$$\text{Work Function} = 0.185449 - (-1.717400) = 1.902849 \text{ eV}$$

## Output Plot
The planar-averaged electrostatic potential distribution across the $z$-axis is saved in `potential_plot.png`.

## Execution
python3 work_function.py
