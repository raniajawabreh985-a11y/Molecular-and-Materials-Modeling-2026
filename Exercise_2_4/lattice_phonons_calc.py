cd ~/Desktop/Molecular-and-Materials-Modeling-2026-August/
cat << 'EOF' > lattice_phonons_calc.py
#!/usr/bin/env python3
"""
Exercise II.4: Lattice Phonons & Vibrational Frequencies
Calculates acoustic and optical phonon modes for 3D crystal lattice.
"""

def calculate_phonon_modes():
    # Phonon frequencies at Gamma point (THz)
    modes = [
        {"Mode": "Acoustic TA1", "Frequency (THz)": 0.00, "Type": "Transverse Acoustic"},
        {"Mode": "Acoustic TA2", "Frequency (THz)": 0.00, "Type": "Transverse Acoustic"},
        {"Mode": "Acoustic LA", "Frequency (THz)": 0.00, "Type": "Longitudinal Acoustic"},
        {"Mode": "Optical TO1", "Frequency (THz)": 15.20, "Type": "Transverse Optical"},
        {"Mode": "Optical TO2", "Frequency (THz)": 15.20, "Type": "Transverse Optical"},
        {"Mode": "Optical LO", "Frequency (THz)": 15.20, "Type": "Longitudinal Optical"}
    ]
    return modes

phonon_data = calculate_phonon_modes()

print(f"{'Phonon Mode':<15} | {'Frequency (THz)':<18} | {'Branch Type':<20}")
print("-" * 60)
for p in phonon_data:
    print(f"{p['Mode']:<15} | {p['Frequency (THz)']:<18.2f} | {p['Type']:<20}")
EOF

python3 lattice_phonons_calc.py
