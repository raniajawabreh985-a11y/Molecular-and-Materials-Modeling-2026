"""
===============================================================================
Exercise II.5: Crystal Defect & Vacancy Formation Energy
===============================================================================

Overview:
---------
Calculates point defect energetics and single vacancy formation energy
(E_vac = E_defect - ((N - 1) / N) * E_bulk) in crystal lattices using 
Density Functional Theory (DFT) via Quantum ESPRESSO and ASE.

Execution & How to Run:
-----------------------
1. Ensure your Conda environment with ASE and Quantum ESPRESSO is active:
   $ conda activate materials

2. Execute the python script and redirect outputs to a log file:
   $ python3 defect_vacancy_calc.py > defect_vacancy_calc.out

3. Monitor calculation progress in real-time:
   $ tail -f defect_vacancy_calc.out

Files Generated:
----------------
- defect_vacancy_calc.out : Full calculation log and output results.
- outdir_defect/         : Temporary Quantum ESPRESSO scratch directory.
===============================================================================
"""

import os
from ase.build import bulk
from ase.calculators.espresso import Espresso, EspressoProfile

# 1. System Setup
# ---------------
# Build pristine bulk cell
bulk_atoms = bulk('Al', crystalstructure='fcc', a=4.05, cubic=True)

# Create a vacancy defect (removing one atom)
defect_atoms = bulk_atoms.copy()
del defect_atoms[0]

# 2. Calculator Configuration
# ---------------------------
pseudopotentials = {'Al': 'Al.pz-vbc.UPF'}

input_data = {
    'control': {
        'calculation': 'scf',
        'prefix': 'al_vacancy',
        'outdir': './outdir_defect'
    },
    'system': {
        'ecutwfc': 30.0,
        'occupations': 'smearing',
        'smearing': 'marzari-vanderbilt',
        'degauss': 0.02
    },
    'electrons': {
        'conv_thr': 1.0e-8
    }
}

profile = EspressoProfile(
    command='pw.x',
    pseudo_dir='.'
)

calc = Espresso(
    input_data=input_data,
    pseudopotentials=pseudopotentials,
    kpts=(4, 4, 4),
    profile=profile
)

# 3. Calculation Execution
# ------------------------
# Bulk Calculation
bulk_atoms.calc = calc
E_bulk = bulk_atoms.get_potential_energy()
N = len(bulk_atoms)

# Defect Calculation
defect_atoms.calc = calc
E_defect = defect_atoms.get_potential_energy()

# Vacancy Formation Energy Calculation
E_vac = E_defect - ((N - 1) / N) * E_bulk

# 4. Results Output
# -----------------
print("==========================================")
print("     Crystal Vacancy Energy Results       ")
print("==========================================")
print(f"Total Bulk Supercell Energy (E_bulk) : {E_bulk:.6f} eV")
print(f"Total Defect Supercell Energy (E_def): {E_defect:.6f} eV")
print(f"Calculated Vacancy Energy (E_vac)    : {E_vac:.6f} eV")
print("==========================================")
print("-" * 52)
print(f"{'Single Vacancy (V)':<25} | {e_vacancy:<22.4f}")
EOF

python3 defect_vacancy_calc.py
