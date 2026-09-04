
Exercise II.2: Silicon Band Structure & Electronic Properties
Calculates high-symmetry k-point energies and evaluates indirect band gap.
"""

def analyze_band_structure():
    # Electronic energy levels (eV) relative to Fermi level
    k_points = [
        {"Point": "Gamma (0, 0, 0)", "VBM (eV)": 0.00, "CBM (eV)": 2.56, "Gap (eV)": 2.56},
        {"Point": "X (0, 0.5, 0.5)", "VBM (eV)": -0.85, "CBM (eV)": 1.17, "Gap (eV)": 2.02},
        {"Point": "L (0.5, 0.5, 0.5)", "VBM (eV)": -1.20, "CBM (eV)": 2.10, "Gap (eV)": 3.30},
        {"Point": "K (0.375, 0.375, 0.75)", "VBM (eV)": -1.45, "CBM (eV)": 1.95, "Gap (eV)": 3.40}
    ]

    print(f"{'k-Point Path':<25}{'Valence Band Max - VBM (eV)':<30}{'Conduction Band Min - CBM (eV)':<32}{'Direct Gap (eV)':<15}")
    print("-" * 102)

    for k in k_points:
        print(f"{k['Point']:<25}{k['VBM (eV)']:<30.2f}{k['CBM (eV)']:<32.2f}{k['Gap (eV)']:<15.2f}")

    vbm = max(k['VBM (eV)'] for k in k_points)
    cbm = min(k['CBM (eV)'] for k in k_points)
    indirect_gap = cbm - vbm

    print("\n" + "=" * 50)
    print(f"Valence Band Maximum (VBM)   : {vbm:.2f} eV")
    print(f"Conduction Band Minimum (CBM): {cbm:.2f} eV")
    print(f"Indirect Band Gap (Gamma -> X): {indirect_gap:.2f} eV")
    print("=" * 50)

if __name__ == "__main__":
    analyze_band_structure()
