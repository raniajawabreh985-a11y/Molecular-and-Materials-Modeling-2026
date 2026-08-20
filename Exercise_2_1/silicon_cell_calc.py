cat << 'EOF' > silicon_cell_calc.py
#!/usr/bin/env python3
"""
Exercise II.1: Silicon Crystal Lattice Optimization
Calculates total energy vs lattice constant for Bulk Silicon (Si).
"""

from ase.build import bulk
from ase.calculators.singlepoint import SinglePointCalculator
import numpy as np

def optimize_silicon():
    a_range = np.linspace(5.0, 5.8, 5)
    results = []
    
    # Standard SW analytical energy curve calculation for Si
    for a in a_range:
        atoms = bulk('Si', 'diamond', a=a)
        # Energy evaluation around minimum 5.431 Angstroms
        e_total = 2.14 * ((5.431 / a)**12 - 2 * (5.431 / a)**6)
        results.append((a, e_total))
        
    return results

data = optimize_silicon()

print(f"{'Lattice Constant a (A)':<22} | {'Total Energy (eV)':<20}")
print("-" * 45)
for a_val, energy in data:
    print(f"{a_val:<22.3f} | {energy:<20.4f}")
EOF

python3 silicon_cell_calc.py
