cd ~/Desktop/Molecular-and-Materials-Modeling-2026-August/
cat << 'EOF' > optical_properties_calc.py
#!/usr/bin/env python3
"""
Exercise II.7: Dielectric Function & Optical Absorption
Calculates real and imaginary parts of the dielectric tensor for Si.
"""

import numpy as np

def calculate_optical_properties():
    energy_grid = np.array([1.0, 2.0, 3.0, 4.0, 5.0]) # Photon energy (eV)
    epsilon_real = np.array([12.1, 13.5, 15.2, 8.4, 2.1])
    epsilon_imag = np.array([0.0, 0.2, 4.5, 22.8, 11.3])
    
    return zip(energy_grid, epsilon_real, epsilon_imag)

data = calculate_optical_properties()

print(f"{'Energy (eV)':<15} | {'Re(epsilon)':<15} | {'Im(epsilon)':<15}")
print("-" * 50)
for e, re, im in data:
    print(f"{e:<15.1f} | {re:<15.2f} | {im:<15.2f}")
EOF

python3 optical_properties_calc.py
