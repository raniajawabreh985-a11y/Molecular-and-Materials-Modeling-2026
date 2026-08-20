
#!/usr/bin/env python3
"""
Exercise I.2: Atomization Energy Calculation using ASE EMT Calculator
Systems evaluated: H2, N2, O2
"""

from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT


def get_atomization(sym):
  # Atom calculation
  atom = Atoms(sym, calculator=EMT())
  e_atom = atom.get_potential_energy()

  # Molecule calculation
  mol = molecule(f'{sym}2', calculator=EMT())
  e_mol = mol.get_potential_energy()

  # Atomization Energy: E_at = 2*E_atom - E_mol
  e_at = (2 * e_atom) - e_mol
  return e_atom, e_mol, e_at


if __name__ == '__main__':
  print(
      f"{'System':<8} | {'E_atom (eV)':<12} | {'E_mol (eV)':<12} |"
      f" {'E_atomization (eV)':<18}"
  )
  print('-' * 58)
  for s in ['H', 'N', 'O']:
    ea, em, eat = get_atomization(s)
    print(f'{s+"2":<8} | {ea:<12.4f} | {em:<12.4f} | {eat:<18.4f}')
