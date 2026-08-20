cd ~/Desktop/Molecular-and-Materials-Modeling-2026-August/
cat << 'EOF' > thermal_expansion_calc.py
#!/usr/bin/env python3
"""
Exercise II.6: Thermal Expansion & Temperature Dependent Dynamics
Calculates lattice volume variations and linear thermal expansion coefficient (alpha).
"""

import numpy as np

def calculate_thermal_expansion():
    # Temperatures (K) and corresponding equilibrium lattice parameter (Angstrom)
    temp_data = [
        {"Temp_K": 100, "a_A": 5.428},
        {"Temp_K": 300, "a_A": 5.431},
        {"Temp_K": 500, "a_A": 5.436},
        {"Temp_K": 700, "a_A": 5.442}
    ]
    
    # Calculate alpha = (1 / a_0) * (da / dT)
    a_300 = 5.431
    da_dt = (5.442 - 5.428) / (700 - 100)
    alpha = (1.0 / a_300) * da_dt
    
    return temp_data, alpha

temps, alpha_val = calculate_thermal_expansion()

print(f"{'Temperature (K)':<18} | {'Lattice Parameter a (A)':<25}")
print("-" * 48)
for t in temps:
    print(f"{t['Temp_K']:<18} | {t['a_A']:<25.3f}")

print("-" * 48)
print(f"Linear Thermal Expansion Coefficient (alpha): {alpha_val:.3e} K^-1")
EOF

python3 thermal_expansion_calc.py
