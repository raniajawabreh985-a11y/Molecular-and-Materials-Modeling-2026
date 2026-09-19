# Exercise 1.7: Geometry Optimization & Cutoff Convergence Analysis

## 1. Cutoff Convergence Analysis for Water ($\text{H}_2\text{O}$)
A series of DFT calculations were conducted using Quantum Espresso via ASE to determine the optimal plane-wave energy cutoff (`ecutwfc`).

| Ecut (Ry) | Total Energy (eV) | O-H Bond Length ($\text{\AA}$) | H-O-H Angle (deg) |
| :---: | :---: | :---: | :---: |
| **30** | -598.6833 | 0.9746 | 104.58 |
| **40** | -598.7710 | 0.9732 | 104.53 |
| **50** | -598.8005 | 0.9727 | 104.54 |
| **60** | -598.8104 | 0.9725 | 104.55 |

* **Conclusion:** The total energy converges within $\sim 0.01\text{ eV}$ starting at **$50\text{ Ry}$**, which is selected as the optimal energy cutoff balancing accuracy and computational effort.

---

## 2. Challenge 1.7: Methane ($\text{CH}_4$) Geometry Relaxation
The original ASE script was modified to perform geometry relaxation for Methane ($\text{CH}_4$) using the BFGS optimization algorithm.

### Methane Optimization Python Script (`methane_opt.py`)
```python
import os
from ase.build import molecule
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.optimize import BFGS

PSEUDO_DIR = "/usr/share/espresso/pseudo/"
os.environ['OMP_NUM_THREADS'] = '1'

ch4 = molecule('CH4')
ch4.set_cell([12.0, 12.0, 12.0])
ch4.center()

pseudopotentials = {
    'C': 'C.pbe-n-kjpaw_psl.0.1.UPF',
    'H': 'H.pbe-kjpaw.UPF',
}

input_data = {
    'control': {
        'calculation': 'scf',
        'prefix': 'ch4_run',
        'outdir': './outdir_ch4',
        'verbosity': 'low',
        'tstress': True,
        'tprnfor': True
    },
    'system': {
        'ecutwfc': 35.0,
        'ecutrho': 280.0,
        'ibrav': 0,
        'nosym': True,
        'noinv': True,
        'occupations': 'smearing',
        'smearing': 'gaussian',
        'degauss': 0.02,
    },
    'electrons': {
        'conv_thr': 1e-6,
        'mixing_beta': 0.7,
        'diagonalization': 'david'
    }
}

profile = EspressoProfile(command='pw.x', pseudo_dir=PSEUDO_DIR)

calc = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials,
    input_data=input_data,
    kpts=(1, 1, 1)
)

ch4.calc = calc

dyn = BFGS(ch4, trajectory='ch4_opt.traj', logfile='ch4_opt.log')
dyn.run(fmax=0.05)

print("\n=== Optimized Methane (CH4) Results ===")
print(f"Final Total Energy : {ch4.get_total_energy():.4f} eV")
print(f"C-H Bond Length    : {ch4.get_distance(0, 1):.4f} A")
print(f"H-C-H Angle        : {ch4.get_angle(1, 0, 2):.2f} deg")
