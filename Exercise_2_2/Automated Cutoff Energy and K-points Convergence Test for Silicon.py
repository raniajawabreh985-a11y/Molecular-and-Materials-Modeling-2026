#!/usr/bin/env python3
"""
Exercise II.2: Automated Cutoff Energy and K-points Convergence Test for Silicon.

"""

import os
import sys
import shutil
from ase.build import bulk
from ase.calculators.espresso import Espresso, EspressoProfile

# 1. Setup execution profile for Quantum ESPRESSO (pw.x)
pw_path = shutil.which("pw.x") or '/usr/bin/pw.x'
profile = EspressoProfile(command=pw_path, pseudo_dir='.')

# ==============================================================================
# TASK 2.1: Automated Cutoff Energy and K-points Grid Convergence Tests
# ==============================================================================
print("==================================================")
print("TASK 2.1: Starting Automated Convergence Tests")
print("==================================================")

atoms_si = bulk('Si', 'diamond', a=5.43)
pseudopotentials_pbe = {'Si': 'Si.pbe-n-rrkjus_psl.1.0.0.UPF'}

# A. Cutoff Energy Convergence Test
ecut_values = [20, 25, 30, 35, 40, 45, 50, 55, 60]
print("\n--- A. Cutoff Energy (ecutwfc) Convergence ---")
for ecut in ecut_values:
    calc = Espresso(
        profile=profile,
        pseudopotentials=pseudopotentials_pbe,
        input_data={
            'control': {'calculation': 'scf', 'restart_mode': 'from_scratch', 'prefix': 'si_ecut', 'outdir': './tmp'},
            'system': {'ecutwfc': ecut},
            'electrons': {'conv_thr': 1.0e-8}
        },
        kpts=(8, 8, 8)
    )
    atoms_si.calc = calc
    e_tot = atoms_si.get_potential_energy()
    print(f"ecutwfc = {ecut:2d} Ry  --> Total Energy = {e_tot:12.6f} eV")

# B. K-points Grid Convergence Test
k_values = [2, 4, 6, 8, 10, 12, 14, 15]
print("\n--- B. K-points Grid Convergence (at ecutwfc = 60 Ry) ---")
for k in k_values:
    calc = Espresso(
        profile=profile,
        pseudopotentials=pseudopotentials_pbe,
        input_data={
            'control': {'calculation': 'scf', 'restart_mode': 'from_scratch', 'prefix': 'si_kpts', 'outdir': './tmp'},
            'system': {'ecutwfc': 60},
            'electrons': {'conv_thr': 1.0e-8}
        },
        kpts=(k, k, k)
    )
    atoms_si.calc = calc
    e_tot = atoms_si.get_potential_energy()
    print(f"K-grid = {k:2d}x{k:2d}x{k:2d}  --> Total Energy = {e_tot:12.6f} eV")

# ==============================================================================
# TASK 2.2: Forces and Stress Calculation (Unshifted Ideal Lattice)
# ==============================================================================
print("\n==================================================")
print("TASK 2.2: Calculating Forces and Stress (Symmetric)")
print("==================================================")

calc_task22 = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials_pbe,
    tstress=True,
    tprnfor=True,
    input_data={
        'control': {'calculation': 'scf', 'restart_mode': 'from_scratch', 'prefix': 'si_t22', 'outdir': './tmp'},
        'system': {'ecutwfc': 60},
        'electrons': {'conv_thr': 1.0e-8}
    },
    kpts=(15, 15, 15)
)
atoms_si.calc = calc_task22
forces_22 = atoms_si.get_forces()
stress_22 = atoms_si.get_stress()

print(f"Forces (eV/A):\n{forces_22}")
print(f"Stress tensor (Voigt notation):\n{stress_22}")

# ==============================================================================
# TASK 2.3: Manual Atomic Shift & Forces Recalculation
# ==============================================================================
print("\n==================================================")
print("TASK 2.3: Calculating Forces after Manual Atomic Displacement")
print("==================================================")

# atoms_shifted
atoms_shifted = atoms_si.copy()
positions = atoms_shifted.get_positions()
positions[1, 0] += 0.1  # Shift second atom in x-direction
atoms_shifted.set_positions(positions)

calc_task23 = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials_pbe,
    tstress=True,
    tprnfor=True,
    input_data={
        'control': {'calculation': 'scf', 'restart_mode': 'from_scratch', 'prefix': 'si_t23', 'outdir': './tmp'},
        'system': {'ecutwfc': 60},
        'electrons': {'conv_thr': 1.0e-8}
    },
    kpts=(15, 15, 15)
)
atoms_shifted.calc = calc_task23
forces_23 = atoms_shifted.get_forces()

print("Computed Forces after shift (eV/A):")
for i, f in enumerate(forces_23):
    print(f" Atom {i+1}: Fx={f[0]:.6f}, Fy={f[1]:.6f}, Fz={f[2]:.6f}")

# ==============================================================================
# CHALLENGE: Pseudopotentials Comparison (LDA vs PBE)
# ==============================================================================
print("\n==================================================")
print("CHALLENGE: Pseudopotentials Comparison (Si.pz-vbc.UPF)")
print("==================================================")

pseudopotentials_lda = {'Si': 'Si.pz-vbc.UPF'}
if os.path.exists('Si.pz-vbc.UPF'):
    for ecut in [20, 30, 40]:
        calc_ch = Espresso(
            profile=profile,
            pseudopotentials=pseudopotentials_lda,
            input_data={
                'control': {'calculation': 'scf', 'restart_mode': 'from_scratch', 'prefix': 'si_lda', 'outdir': './tmp'},
                'system': {'ecutwfc': ecut},
                'electrons': {'conv_thr': 1.0e-8}
            },
            kpts=(12, 12, 12)
        )
        atoms_si.calc = calc_ch
        e_tot_lda = atoms_si.get_potential_energy()
        print(f"LDA (Norm-Conserving) ecut = {ecut:2d} Ry --> Total Energy = {e_tot_lda:12.6f} eV")
else:
    print("Notice: 'Si.pz-vbc.UPF' file not found in current directory. Skipped LDA test run.")

print("\nAll Tasks Executed Successfully!")
