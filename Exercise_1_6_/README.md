# Exercise I.6 & Challenge I.6: Bond Energy Calculations with ASE

## 1. Exercise I.6: Ethane C-C Bond Energy
Calculation of the C-C bond dissociation energy in Ethane ($C_2H_6 \rightarrow 2 CH_3$):

* **Ethane Energy:** 3.0789 eV
* **Methyl Radical Energy ($CH_3$):** 1.9735 eV
* **Calculated C-C Bond Energy:** 0.8680 eV (83.75 kJ/mol)

---

## 2. Challenge I.6: Methane C-H Bond Energy
Modification of the script to compute the C-H bond energy in Methane ($CH_4 \rightarrow CH_3 + H$):

### Python Script (`methane_CH_bond_en.py`):
```python
from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT

# 1. Energy of Methane (CH4)
methane = molecule('CH4')
methane.calc = EMT()
E_methane = methane.get_potential_energy()

# 2. Energy of Methyl radical (CH3)
ch3 = molecule('CH3')
ch3.calc = EMT()
E_ch3 = ch3.get_potential_energy()

# 3. Energy of Hydrogen atom (H)
h_atom = Atoms('H', positions=[(0, 0, 0)])
h_atom.calc = EMT()
E_h = h_atom.get_potential_energy()

# 4. C-H Bond Energy Calculation
E_bond_CH_eV = (E_ch3 + E_h) - E_methane
E_bond_CH_kj = E_bond_CH_eV * 96.485

print(f"Methane Energy: {E_methane:.4f} eV")
print(f"Methyl Radical Energy: {E_ch3:.4f} eV")
print(f"Hydrogen Atom Energy: {E_h:.4f} eV")
print(f"Calculated C-H Bond Energy: {E_bond_CH_eV:.4f} eV")
print(f"Calculated C-H Bond Energy: {E_bond_CH_kj:.2f} kJ/mol")
