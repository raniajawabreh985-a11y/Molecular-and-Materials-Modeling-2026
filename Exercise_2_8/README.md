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


