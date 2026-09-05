# Electronic Properties of Silicon (Si) using Quantum ESPRESSO

This repository contains the setup and computational workflow for analyzing the electronic structure of bulk Silicon ($Si$) using Quantum ESPRESSO.

## Workflow Summary

1. **Self-Consistent Field (SCF) Calculation**:
   - Computes the ground-state electron density and total energy.
   - **Total Energy**: `-230.280149 eV`

2. **Charge Density & Löwdin Population Analysis**:
   - Generates 3D spatial charge density (`charge_density.cube`).
   - Extracts atomic charges and orbital occupations stored in `lowdin.out`.
   - **Spilling Parameter**: `0.008900` (High projection accuracy).

3. **Non-Self-Consistent Field (NSCF) Calculation**:
   - Evaluates dense k-space energy levels using a $30 \times 30 \times 30$ Monkhorst-Pack grid.
   - **Fermi Energy ($E_F$)**: `6.3184 eV`

4. **Density of States (DOS & PDOS)**:
   - Computes total DOS (`total_dos.dat`) and projected atomic orbital contributions (`pdos_results/`).
   - Integrates DOS below $E_F$: `7.9999` states (Matches 8 valence electrons per unit cell).

## Generated Files

- `lowdin.out`: Löwdin charges and orbital occupations.
- `charge_density.cube`: Electronic charge density spatial map.
- `total_dos.dat`: Total density of states spectrum.
- `pdos_results/`: Directory containing orbital-projected DOS data.

## Running the Python Workflow

```bash
python3 electronic_properties_si.py
