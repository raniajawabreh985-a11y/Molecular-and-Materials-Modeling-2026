import os
import numpy as np
from ase.build import graphene
from ase.calculators.espresso import Espresso

# Create Monolayer Graphene with 15 Angstrom vacuum along z-axis
atoms = graphene(symbol='C', latticeconstant={'a': 2.46, 'c': 15.0})
atoms.center(vacuum=7.5, axis=2)

ecutwfc_list = [20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0]
kpts = (39, 39, 1)

print(f"Starting ecutwfc convergence test for Graphene with k-point grid {kpts}...")
print(f"{'ecutwfc (Ry)':<15}{'Energy (eV)':<20}{'dE (meV/atom)':<20}")
print("-" * 55)

prev_energy = None
results = []

for ecut in ecutwfc_list:
    calc = Espresso(
        command='mpirun -np 4 /home/user/miniconda3/bin/pw.x -in espresso.pwi > espresso.pwo',
        pseudopotentials={'C': 'C.pbe-n-kjpaw_psl.1.0.0.UPF'},
        kpts=kpts,
        input_data={
            'CONTROL': {
                'calculation': 'scf',
                'restart_mode': 'from_scratch',
                'prefix': 'graphene',
                'outdir': './tmp',
            },
            'SYSTEM': {
                'ecutwfc': ecut,
                'assume_isolated': '2D',
                'occupations': 'smearing',
                'smearing': 'mv',
                'degauss': 0.01,
            },
            'ELECTRONS': {
                'conv_thr': 1.0e-8,
                'electron_max_step': 100,
            },
        },
    )
    atoms.calc = calc
    energy = atoms.get_potential_energy()
    num_atoms = len(atoms)

    if prev_energy is not None:
        de_per_atom = abs(energy - prev_energy) / num_atoms * 1000.0
        de_str = f"{de_per_atom:.3f}"
    else:
        de_str = "-"

    print(f"{ecut:<15.1f}{energy:<20.6f}{de_str:<20}")
    prev_energy = energy

print("-" * 48)
print(f"Linear Thermal Expansion Coefficient (alpha): {alpha_val:.3e} K^-1")
EOF

python3 thermal_expansion_calc.py
