# Adsorption on the surface

Adsorption of H atom on a piece of graphene (C8).

Initial structures are read from vasp geometry files. The H atom is placed into a middle of cubic box.

## step 1

`relaxation.py` - optimizes the H@C8 geometry

## step 2

`energy_h.py` - computes the energy of H atom

## step 3

`energy_c.py` - computes the energy of C8 surface

## Execution

```bash
python3 relaxation.py
python3 energy_h.py
python3 energy_c.py

H@C8 Relaxation Output:
-----------------------
Total Energy                : -1319.069282 eV
ASE-style max force (norm)  : 0.003278 eV/A
QE-style max force          : 0.003278 eV/A
Pressure                    : 26.532360 kbar

H Atom SCF Output:
------------------
Total energy                : -12.559509 eV
Fermi level                 : -6.462900 eV

C8 Surface SCF Output:
----------------------
Total energy                : -1303.645873 eV
Fermi level                 : -1.813400 eV

Binding Energy Calculation:
---------------------------
Binding energy = E(C8) + E(H) - E(H@C8)
Binding energy = -1303.645873 - 12.559509 - (-1319.069282) eV
Binding energy = 2.8639 eV

