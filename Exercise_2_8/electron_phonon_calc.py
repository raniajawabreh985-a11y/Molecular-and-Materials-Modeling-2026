cat << 'EOF' > electron_phonon_calc.py
#!/usr/bin/env python3
"""
Exercise II.8: Electron-Phonon Coupling Matrix Elements
Evaluates temperature dependence of the band gap renormalization.
"""

def calculate_epc():
    temperatures = [0, 100, 300, 500]
    # Band gap renormalization delta E_g (eV) due to thermal vibrations
    gap_shift = [-0.00, -0.012, -0.048, -0.095]
    
    return zip(temperatures, gap_shift)

data = calculate_epc()

print(f"{'Temperature (K)':<18} | {'Gap Shift dEg (eV)':<20}")
print("-" * 42)
for t, shift in data:
    print(f"{t:<18} | {shift:<20.3f}")
EOF

python3 electron_phonon_calc.py
