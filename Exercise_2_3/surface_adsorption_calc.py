#!/usr/bin/env python3
"""
Exercise II.3: Surface Formation & Adsorption Energy Analysis
Calculates:
1. Surface Formation Energy (gamma) in J/m^2
2. Adsorption Binding Energy (E_ad) in eV
"""

# Units Conversion Factor
RY_TO_EV = 13.605698066
EV_TO_JOULE = 1.602176634e-19
ANGSTROM2_TO_M2 = 1.0e-20

# ---------------------------------------------------------
# Calculated / Simulated Energies (in Ry)
# ---------------------------------------------------------
E_bulk_per_atom = -16.92527473 / 2.0  # Bulk energy per Si/Au atom in Ry

# Surface Slab Parameters
E_slab = -135.201452      # Total energy of relaxed Au(111) slab (Ry)
N_atoms_slab = 8          # Number of atoms in the slab
Area_angstrom2 = 32.45    # Surface cross-sectional area (A^2)

# Adsorption Parameters
E_molecule = -1.152431    # Energy of the isolated molecule in vacuum (Ry)
E_system = -136.397223    # Total energy of Slab + Molecule system (Ry)

# ---------------------------------------------------------
# 1. Surface Formation Energy Calculation (gamma)
# ---------------------------------------------------------
# Formula: gamma = (E_slab - N * E_bulk) / (2 * Area)
E_surface_unscaled_Ry = E_slab - (N_atoms_slab * E_bulk_per_atom)
E_surface_eV = E_surface_unscaled_Ry * RY_TO_EV
E_surface_Joules = E_surface_eV * EV_TO_JOULE

Area_m2 = Area_angstrom2 * ANGSTROM2_TO_M2
gamma = E_surface_Joules / (2.0 * Area_m2)  # J/m^2

# ---------------------------------------------------------
# 2. Adsorption Binding Energy Calculation (E_ad)
# ---------------------------------------------------------
# Formula: E_ad = E_system - (E_slab + E_molecule)
E_ad_Ry = E_system - (E_slab + E_molecule)
E_ad_eV = E_ad_Ry * RY_TO_EV

# ---------------------------------------------------------
# Print Results
# ---------------------------------------------------------
print("=" * 50)
print(" EXERCISE II.3: CALCULATION RESULTS")
print("=" * 50)
print(f"Surface Formation Energy (gamma) : {gamma:.4f} J/m^2")
print(f"Adsorption Binding Energy (E_ad) : {E_ad_eV:.4f} eV")
print("=" * 50)
print(f"{'Surface Energy (J/m^2)':<30} | {gamma:<15.4f}")
print(f"{'Adsorption Energy (eV)':<30} | {e_ad:<15.4f}")
EOF

python3 surface_adsorption_calc.py
