#!/usr/bin/env python3
"""
Script: run_mace.py
Description: Initial geometry optimization of UO2I2(OH2)2 complex using 
             MACE machine-learned interatomic potential via ASE.
"""

import os
import sys
from ase import Atoms
from ase.io import read, write
from ase.optimize import BFGS

try:
    from mace.calculators import mace_mp
except ImportError:
    print("[Error] MACE package is not installed. Install it using: pip install mace-torch")
    sys.exit(1)


def get_initial_structure():
    """Reads existing initial structure file or generates a fallback geometry."""
    input_file = "initial_structure.xyz"
    
    if os.path.exists(input_file):
        print(f"[+] Loading structure from '{input_file}'...")
        return read(input_file)
    
    print(f"[!] '{input_file}' not found. Generating default UO2I2(OH2)2 structure...")
    # Default coordinates for UO2I2(OH2)2 (11 atoms)
    atoms = Atoms(
        symbols=['U', 'O', 'O', 'I', 'I', 'O', 'H', 'H', 'O', 'H', 'H'],
        positions=[
            [0.000000,  0.000000,  0.000000],  # U
            [0.000000,  0.000000,  1.770000],  # O (uranyl)
            [0.000000,  0.000000, -1.770000],  # O (uranyl)
            [2.600000,  0.000000,  0.000000],  # I
            [-2.600000, 0.000000,  0.000000],  # I
            [0.000000,  2.400000,  0.000000],  # O (water 1)
            [0.800000,  2.950000,  0.000000],  # H (water 1)
            [-0.800000, 2.950000,  0.000000],  # H (water 1)
            [0.000000, -2.400000,  0.000000],  # O (water 2)
            [0.800000, -2.950000,  0.000000],  # H (water 2)
            [-0.800000, -2.950000, 0.000000]   # H (water 2)
        ]
    )
    # Save standard initial file for future reference
    write(input_file, atoms)
    return atoms


def main():
    # 1. Load or create initial geometry
    atoms = get_initial_structure()
    print(f"[+] Initial system loaded with {len(atoms)} atoms.")

    # 2. Attach MACE Machine Learning Calculator
    print("[+] Initializing MACE calculator (mace_mp)...")
    calc = mace_mp(model="medium", dispersion=True, device="cpu")
    atoms.calc = calc

    # 3. Perform Geometry Optimization using BFGS algorithm
    output_traj = "mace_opt.traj"
    output_xyz = "mace_opt.xyz"
    
    print("[+] Starting BFGS geometry optimization...")
    optimizer = BFGS(atoms, trajectory=output_traj)
    optimizer.run(fmax=0.02)  # Convergence threshold for forces (eV/A)

    # 4. Save optimized geometry to XYZ format
    write(output_xyz, atoms)
    print(f"[✔] Optimization completed successfully!")
    print(f"[✔] Optimized structure saved to '{output_xyz}'")


if __name__ == "__main__":
    main()
