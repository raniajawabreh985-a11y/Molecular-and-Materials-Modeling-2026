cd ~/Desktop/Molecular-and-Materials-Modeling-2026-August/
cat << 'EOF' > surface_adsorption_calc.py
#!/usr/bin/env python3
"""
Exercise II.3: Surface & Adsorption Energy Calculation
Evaluates surface formation energy (Au 111 slab) and molecular adsorption energy.
"""

def calculate_surface_properties():
    # Surface formation energy (J/m^2)
    e_bulk_per_atom = -3.93  # eV
    e_slab_total = -15.10    # eV (4-layer slab)
    n_atoms = 4
    area = 7.15              # Angstrom^2
    
    # Surface energy gamma = (E_slab - N*E_bulk) / (2 * Area)
    gamma_ev_a2 = (e_slab_total - (n_atoms * e_bulk_per_atom)) / (2 * area)
    gamma_j_m2 = gamma_ev_a2 * 16.0218  # Conversion factor to J/m^2
    
    # Adsorption energy E_ad = E_total - (E_slab + E_molecule)
    e_molecule = -1.16       # eV (e.g. CO or H2)
    e_system = -16.85        # eV
    e_adsorption = e_system - (e_slab_total + e_molecule)
    
    return gamma_j_m2, e_adsorption

gamma, e_ad = calculate_surface_properties()

print(f"{'Property':<30} | {'Calculated Value':<15}")
print("-" * 50)
print(f"{'Surface Energy (J/m^2)':<30} | {gamma:<15.4f}")
print(f"{'Adsorption Energy (eV)':<30} | {e_ad:<15.4f}")
EOF

python3 surface_adsorption_calc.py
