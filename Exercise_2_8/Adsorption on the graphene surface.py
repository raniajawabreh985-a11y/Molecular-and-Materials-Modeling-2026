#!/usr/bin/env python3
from ase.io import read
from ase.calculators.espresso import Espresso, EspressoProfile

profile = EspressoProfile(command='pw.x', pseudo_dir='.')

# 1. Total energy of pure C8 slab
c8 = read('c8.vasp')
c8.calc = Espresso(
    profile=profile,
    input_data={
        'control': {'calculation': 'scf', 'prefix': 'c8_scf', 'outdir': './tmp'},
        'system': {'ecutwfc': 30.0, 'occupations': 'smearing', 'smearing': 'gaussian', 'degauss': 0.01},
        'electrons': {'conv_thr': 1e-6}
    },
    pseudopotentials={'C': 'C.upf'}
)
e_c8 = c8.get_total_energy()

# 2. Total energy of isolated H atom
h = read('h.vasp')
h.calc = Espresso(
    profile=profile,
    input_data={
        'control': {'calculation': 'scf', 'prefix': 'h_scf', 'outdir': './tmp'},
        'system': {'ecutwfc': 30.0, 'occupations': 'smearing', 'smearing': 'gaussian', 'degauss': 0.01},
        'electrons': {'conv_thr': 1e-6}
    },
    pseudopotentials={'H': 'H.upf'}
)
e_h = h.get_total_energy()

# 3. Total energy of H adsorbed on C8
h_c8 = read('h_c8.vasp')
h_c8.calc = Espresso(
    profile=profile,
    input_data={
        'control': {'calculation': 'scf', 'prefix': 'hc8_scf', 'outdir': './tmp'},
        'system': {'ecutwfc': 30.0, 'occupations': 'smearing', 'smearing': 'gaussian', 'degauss': 0.01},
        'electrons': {'conv_thr': 1e-6}
    },
    pseudopotentials={'C': 'C.upf', 'H': 'H.upf'}
)
e_h_c8 = h_c8.get_total_energy()

# 4. Binding energy calculation
e_binding = e_c8 + e_h - e_h_c8

print(f"--- Adsorption Results ---")
print(f"E(C8):      {e_c8:.6f} eV")
print(f"E(H):       {e_h:.6f} eV")
print(f"E(H@C8):    {e_h_c8:.6f} eV")
print(f"E_binding:  {e_binding:.6f} eV")
