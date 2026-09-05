import numpy as np
from ase.build import graphene
from ase.calculators.espresso import Espresso

# 1. Structure Setup: Monolayer Graphene
atoms = graphene(formula='C2', vacuum=10.0)

# 2. Convergence Test Setup for ecutwfc
ecutwfc_list = [20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0]
kpts_grid = (39, 39, 1)

# Pseudopotential mapping (adjust filename based on your system)
pseudopotentials = {'C': 'C.pbe-n-kjpaw_psl.1.0.0.UPF'}

energies = []

print("Starting convergence tests...\n" + "=" * 50)
print(f"1. Testing ecutwfc convergence with k-point grid {kpts_grid} :\n" + "-" * 50)
print(f"{'ecutwfc (Ry)':<12} {'Energy (eV)':<15} {'ΔE (meV/atom)':<15}")
print("-" * 50)

# 3. Execution Loop
prev_energy = None

for ecut in ecutwfc_list:
    input_data = {
        'control': {
            'calculation': 'scf',
            'restart_mode': 'from_scratch',
            'prefix': 'graphene_ecut',
            'outdir': './out',
            'tstress': True,
            'tprnfor': True,
        },
        'system': {
            'ecutwfc': ecut,
            'occupations': 'smearing',
            'smearing': 'marzari-vanderbilt',
            'degauss': 0.02,
        },
        'electrons': {
            'conv_thr': 1.0e-8,
            'mixing_beta': 0.30,  # Reduced to resolve charge sloshing in 2D graphene
            'electron_max_step': 100,
        }
    }

    calc = Espresso(
        command='mpirun -np 4 pw.x < espresso.pwi > espresso.pwo',
        pseudopotentials=pseudopotentials,
        tstress=True,
        tprnfor=True,
        kpts=kpts_grid,
        input_data=input_data
    )

    atoms.calc = calc
    
    # Calculate potential energy
    energy = atoms.get_potential_energy()
    energies.append(energy)

    # Calculate Delta E per atom (Graphene unit cell has 2 C atoms)
    if prev_energy is None:
        delta_e_str = "."
    else:
        delta_e = ((energy - prev_energy) / len(atoms)) * 1000.0  # in meV/atom
        delta_e_str = f"{delta_e:.3f}"

    print(f"{ecut:<12.1f} {energy:<15.6f} {delta_e_str:<15}")
    prev_energy = energy

print("-" * 50)

print("-" * 48)
print(f"Linear Thermal Expansion Coefficient (alpha): {alpha_val:.3e} K^-1")
EOF

python3 thermal_expansion_calc.py
