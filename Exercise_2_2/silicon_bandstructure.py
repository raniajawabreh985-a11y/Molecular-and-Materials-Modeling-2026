
#!/usr/bin/env python3
"""
Exercise II.2: Automated Cutoff Energy Convergence Test for Silicon
Evaluates energy convergence across a range of ecutwfc values.
"""

import sys
import os
import shutil
from ase.build import bulk
from ase.calculators.espresso import Espresso, EspressoProfile

conda_bin = os.path.join(sys.prefix, 'bin', 'pw.x')
pw_path = conda_bin if os.path.exists(conda_bin) else shutil.which("pw.x")

profile = EspressoProfile(
    command=pw_path,
    pseudo_dir='.'
)

pseudopotentials = {'Si': 'Si.upf'}
kpts = (6, 6, 6)
ecut_values = range(20, 81, 10)

print(f"{'Ecut (Ry)':<12}{'Total Energy (eV)':<20}")
print("-" * 32)

for ecut in ecut_values:
    atoms = bulk('Si', 'diamond', a=5.43)
    
    calc = Espresso(
        profile=profile,
        pseudopotentials=pseudopotentials,
        tstress=True,
        tprnfor=True,
        kpts=kpts,
        input_data={
            'control': {
                'calculation': 'scf',
                'prefix': 'si_conv',
                'outdir': './tmp'
            },
            'system': {
                'ecutwfc': ecut,
                'occupations': 'smearing',
                'smearing': 'gaussian',
                'degauss': 0.01,
            },
            'electrons': {
                'conv_thr': 1.0e-10,
            }
        }
    )
    
    atoms.calc = calc
    try:
        energy = atoms.get_potential_energy()
        print(f"{ecut:<12}{energy:<20.6f}")
    except Exception as e:
        print(f"{ecut:<12}Error: {e}")
    print(f"Indirect Band Gap (Gamma -> X): {indirect_gap:.2f} eV")
    print("=" * 50)

if __name__ == "__main__":
    analyze_band_structure()
