#!/usr/bin/env python3
"""
Exercise II.1: Total Energy Calculation of the Silicon Unit Cell
Calculates the total energy of Si bulk using Quantum ESPRESSO via ASE.
"""

import sys
import os
import shutil
from ase.build import bulk
from ase.calculators.espresso import Espresso, EspressoProfile

# Dynamic path resolution for pw.x binary inside Conda environment
conda_bin = os.path.join(sys.prefix, 'bin', 'pw.x')
pw_path = conda_bin if os.path.exists(conda_bin) else shutil.which("pw.x")

profile = EspressoProfile(
    command=pw_path,
    pseudo_dir='.'
)

# Set up Diamond Silicon bulk structure
atoms = bulk('Si', 'diamond', a=5.43)

calc = Espresso(
    profile=profile,
    pseudopotentials={'Si': 'Si.upf'},
    tstress=True,
    tprnfor=True,
    kpts=(6, 6, 6),
    input_data={
        'control': {
            'calculation': 'scf',
            'prefix': 'si_total_energy',
            'outdir': './tmp'
        },
        'system': {
            'ecutwfc': 40,
            'occupations': 'smearing',
            'smearing': 'gaussian',
            'degauss': 0.01,
        },
        'electrons': {
            'conv_thr': 1.0e-10,
        }
    }
)

atoms.calc = calc

try:
    energy = atoms.get_potential_energy()
    print("=" * 45)
    print(f"Lattice Constant (a) : 5.43 Angstrom")
    print(f"Cutoff Energy (Ecut) : 40 Ry")
    print(f"Total Energy         : {energy:.6f} eV")
    print("=" * 45)
except Exception as e:
    print(f"Execution Error: {e}")
for a_val, energy in data:
    print(f"{a_val:<22.3f} | {energy:<20.4f}")
EOF

python3 silicon_cell_calc.py
