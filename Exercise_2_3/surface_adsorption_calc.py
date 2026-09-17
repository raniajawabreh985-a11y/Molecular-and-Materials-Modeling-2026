#!/usr/bin/env python3
"""
Task 3: Cell Relaxation for Silicon using Quantum ESPRESSO and ASE
"""

from ase.io import read, write
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.optimize import BFGS

# 1. Structure Initialization
atoms = read('cell_relaxation_si.in', format='espresso-in')

# 2. Calculator Configuration
# Update the binary path to your local Quantum ESPRESSO executable
qe_profile = EspressoProfile(
    command='/home/user/miniconda3/bin/pw.x -in PREFIX.pwi > PREFIX.pwo'
)

input_data = {
    'control': {
        'calculation': 'vc-relax',
        'restart_mode': 'from_scratch',
        'pseudo_dir': './',
        'outdir': './tmp',
        'etot_conv_thr': 1.0e-4,
        'forc_conv_thr': 1.0e-3,
    },
    'system': {
        'ecutwfc': 30.0,
        'ibrav': 2,
        'celldm(1)': 10.26,
    },
    'electrons': {
        'conv_thr': 1.0e-8,
        'mixing_beta': 0.7,
    },
    'ions': {
        'ion_dynamics': 'bfgs',
    },
    'cell': {
        'cell_dynamics': 'bfgs',
    }
}

pseudopotentials = {
    'Si': 'Si.pbe-n-kjpaw_psl.1.0.0.UPF'
}

calc = Espresso(
    profile=qe_profile,
    input_data=input_data,
    pseudopotentials=pseudopotentials,
    kpts=(4, 4, 4),
    koffset=(0, 0, 0)
)

atoms.calc = calc

# 3. Execution using ASE Optimizer
dyn = BFGS(atoms, trajectory='relaxation.traj')
dyn.run(fmax=0.05)

# 4. Final Output Processing
final_energy = atoms.get_total_energy()
forces = atoms.get_forces()

print(f"Final Total Energy: {final_energy:.6f} eV")
print(f"Max Force: {abs(forces).max():.6f} eV/Angstrom")

write('final_relaxed_structure.vasp', atoms, format='vasp')
