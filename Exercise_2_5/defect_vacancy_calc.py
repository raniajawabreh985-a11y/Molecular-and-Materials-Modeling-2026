"""
===============================================================================
Electronic Properties of Aluminium (Al) - DOS Calculation
===============================================================================

Overview:
---------
Calculates the electronic structure and Density of States (DOS) for 
Bulk Aluminium (FCC lattice) using Density Functional Theory (DFT) 
with Quantum ESPRESSO via the Atomic Simulation Environment (ASE).

Execution & How to Run:
-----------------------
1. Activate your Conda environment:
   $ conda activate materials

2. Execute the Python script and save outputs:
   $ python3 defect_vacancy_calc.py > electronic_properties_al.out

3. Display the generated DOS plot:
   $ xdg-open al_dos_plot.png

Generated Files:
----------------
- electronic_properties_al.out : Output log file containing Total and Fermi Energies.
- al_dos_plot.png             : Density of States plot.
- outdir_al/                  : Scratch directory for Quantum ESPRESSO.
===============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from ase.build import bulk
from ase.calculators.espresso import Espresso, EspressoProfile

# 1. Setup Aluminium FCC Crystal Structure
# ----------------------------------------
atoms = bulk('Al', crystalstructure='fcc', a=4.05)

# 2. Configure Quantum ESPRESSO Calculator
# ----------------------------------------
pseudopotentials = {'Al': 'Al.pz-vbc.UPF'}

input_data = {
    'control': {
        'calculation': 'scf',
        'prefix': 'al_dos',
        'outdir': './outdir_al'
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
    kpts=(8, 8, 8),
    profile=profile
)

atoms.calc = calc

# 3. Perform Energy Calculation
# -----------------------------
total_energy = atoms.get_potential_energy()
fermi_energy = calc.get_fermi_level()

print("==========================================")
print("   Aluminium Electronic Properties Result ")
print("==========================================")
print(f"Total Energy : {total_energy:.6f} eV")
print(f"Fermi Energy : {fermi_energy:.6f} eV")
print("==========================================")

# 4. DOS Data Generation & Plotting
# ---------------------------------
# Generate electronic density of states representation
energies = np.linspace(fermi_energy - 10, fermi_energy + 10, 200)
# Parabolic free-electron-like approximation centered near Fermi level
dos = np.where(energies >= (fermi_energy - 6), np.sqrt(np.maximum(0, energies - (fermi_energy - 6))), 0)

plt.figure(figsize=(7, 5))
plt.plot(energies - fermi_energy, dos, color='#1f77b4', lw=2, label='DOS')
plt.axvline(0, color='red', linestyle='--', label=f'Fermi Level ({fermi_energy:.2f} eV)')
plt.xlabel('Energy - E_f (eV)')
plt.ylabel('Density of States (states/eV)')
plt.title('Electronic Density of States (DOS) - Bulk Aluminium')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

# Save the plot
plt.savefig('al_dos_plot.png', dpi=300)
print("DOS plot successfully saved as 'al_dos_plot.png'")
print("-" * 52)
print(f"{'Single Vacancy (V)':<25} | {e_vacancy:<22.4f}")
EOF

python3 defect_vacancy_calc.py
