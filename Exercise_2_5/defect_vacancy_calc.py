cd ~/Desktop/Molecular-and-Materials-Modeling-2026-August/
cat << 'EOF' > defect_vacancy_calc.py
#!/usr/bin/env python3
"""
Exercise II.5: Crystal Defect & Vacancy Formation Energy
Calculates vacancy formation energy for bulk crystal supercells.
"""

def calculate_vacancy_energy():
    # Total energy of perfect supercell (eV)
    e_perfect = -108.00
    # Total energy of supercell with one vacancy (eV)
    e_defect = -102.50
    # Chemical potential per atom (eV)
    mu_atom = -5.40
    
    n_atoms = 20
    e_vac = e_defect - ((n_atoms - 1) * mu_atom)
    return e_vac

e_vacancy = calculate_vacancy_energy()

print(f"{'Defect Type':<25} | {'Formation Energy (eV)':<22}")
print("-" * 52)
print(f"{'Single Vacancy (V)':<25} | {e_vacancy:<22.4f}")
EOF

python3 defect_vacancy_calc.py
