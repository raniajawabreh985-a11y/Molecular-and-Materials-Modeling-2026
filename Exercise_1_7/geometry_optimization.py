import os
from ase.build import molecule
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.optimize import BFGS

# 1. Setup pseudo-potential path and environment
PSEUDO_DIR = "/usr/share/espresso/pseudo/"
os.environ['OMP_NUM_THREADS'] = '1'

# 2. Build Methane (CH4) molecule in a vacuum cell
ch4 = molecule('CH4')
ch4.set_cell([12.0, 12.0, 12.0])
ch4.center()

# 3. Specify pseudopotentials
pseudopotentials = {
    'C': 'C.pbe-n-kjpaw_psl.0.1.UPF',
    'H': 'H.pbe-kjpaw.UPF',
}

# 4. Configure Quantum Espresso input parameters
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

# 5. Attach calculator to the molecule
profile = EspressoProfile(command='pw.x', pseudo_dir=PSEUDO_DIR)

calc = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials,
    input_data=input_data,
    kpts=(1, 1, 1)
)

ch4.calc = calc

# 6. Run geometry optimization using BFGS algorithm
dyn = BFGS(ch4, trajectory='ch4_opt.traj', logfile='ch4_opt.log')
dyn.run(fmax=0.05)

# 7. Print optimization results
print("\n==========================================")
print("=== Optimized Methane (CH4) Results ===")
print("==========================================")
print(f"Final Total Energy : {ch4.get_total_energy():.4f} eV")
print(f"C-H Bond Length    : {ch4.get_distance(0, 1):.4f} A")
print(f"H-C-H Angle        : {ch4.get_angle(1, 0, 2):.2f} deg")
print("==========================================")
