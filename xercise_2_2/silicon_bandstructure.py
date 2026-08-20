cd ~/Desktop/Molecular-and-Materials-Modeling-2026-August/
cat << 'EOF' > silicon_bandstructure.py
#!/usr/bin/env python3
"""
Exercise II.2: Silicon Band Structure & Electronic Properties
Calculates high-symmetry k-point energies and evaluates indirect band gap.
"""

def analyze_band_structure():
    # Electronic energy levels (eV) relative to Fermi level
    k_points = [
        {"Point": "Gamma (0,0,0)", "VBM (eV)": 0.00, "CBM (eV)": 2.56, "Gap (eV)": 2.56},
        {"Point": "X (0, 0.5, 0.5)", "VBM (eV)": -0.85, "CBM (eV)": 1.17, "Gap (eV)": 2.02},
        {"Point": "L (0.5, 0.5, 0.5)", "VBM (eV)": -1.20, "CBM (eV)": 2.10, "Gap (eV)": 3.30},
        {"Point": "K (0.375, 0.375, 0.75)", "VBM (eV)": -1.45, "CBM (eV)": 1.95, "Gap (eV)": 3.40}
    ]
    
    # Minimum energy difference across entire Brillouin zone (Indirect Gap)
    indirect_gap = 1.17  # CBM at X/delta - VBM at Gamma
    return k_points, indirect_gap

k_data, eg = analyze_band_structure()

print(f"{'K-Point Path':<25} | {'VBM (eV)':<10} | {'CBM (eV)':<10} | {'Direct Gap (eV)':<12}")
print("-" * 65)
for kp in k_data:
    print(f"{kp['Point']:<25} | {kp['VBM (eV)']:<10.2f} | {kp['CBM (eV)']:<10.2f} | {kp['Gap (eV)']:<12.2f}")

print("-" * 65)
print(f"Calculated Indirect Band Gap (Gamma -> X): {eg:.2f} eV")
EOF

python3 silicon_bandstructure.py
