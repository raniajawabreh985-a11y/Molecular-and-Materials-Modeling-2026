#!/usr/bin/env python3
from ase.io import read, write
from ase.calculators.espresso import Espresso

atoms = read('h_c8.vasp')

pseudopotentials = {
    'C': 'C.pbe-n-kjpaw_psl.1.0.0.UPF',
    'H': 'H.pbe-rrkjus_psl.1.0.0.UPF'
}

input_data = {
    'control': {
        'calculation': 'relax',
        'restart_mode': 'from_scratch',
        'pseudo_dir': './',
    },
    'system': {
        'ecutwfc': 30,
        'occupations': 'smearing',
        'smearing': 'mv',
        'degauss': 0.01,
    },
    'electrons': {
        'conv_thr': 1.0e-6,
    },
}

calc = Espresso(
    input_data=input_data,
    pseudopotentials=pseudopotentials,
    kpts=(2, 2, 1)
)

atoms.calc = calc
energy = atoms.get_potential_energy()
write('final_relaxed_structure.vasp', atoms)
print(f"Total Energy: {energy} eV")

#!/usr/bin/env python3
from ase.io import read
from ase.calculators.espresso import Espresso

atoms = read('h.vasp')

pseudopotentials = {
    'H': 'H.pbe-rrkjus_psl.1.0.0.UPF'
}

input_data = {
    'control': {
        'calculation': 'scf',
        'restart_mode': 'from_scratch',
        'pseudo_dir': './',
    },
    'system': {
        'ecutwfc': 30,
        'occupations': 'smearing',
        'smearing': 'mv',
        'degauss': 0.01,
        'nspin': 2,
    },
    'electrons': {
        'conv_thr': 1.0e-6,
    },
}

calc = Espresso(
    input_data=input_data,
    pseudopotentials=pseudopotentials,
    kpts=(1, 1, 1)
)

atoms.calc = calc
energy = atoms.get_potential_energy()
print(f"Total energy: {energy} eV")

#!/usr/bin/env python3
from ase.io import read
from ase.calculators.espresso import Espresso

atoms = read('c.vasp')

pseudopotentials = {
    'C': 'C.pbe-n-kjpaw_psl.1.0.0.UPF'
}

input_data = {
    'control': {
        'calculation': 'scf',
        'restart_mode': 'from_scratch',
        'pseudo_dir': './',
    },
    'system': {
        'ecutwfc': 30,
        'occupations': 'smearing',
        'smearing': 'mv',
        'degauss': 0.01,
    },
    'electrons': {
        'conv_thr': 1.0e-6,
    },
}

calc = Espresso(
    input_data=input_data,
    pseudopotentials=pseudopotentials,
    kpts=(2, 2, 1)
)

atoms.calc = calc
energy = atoms.get_potential_energy()
print(f"Total energy: {energy} eV")
