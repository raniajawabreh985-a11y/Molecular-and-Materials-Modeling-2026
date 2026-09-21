#!/usr/bin/env python3
"""
Exercise I.6 & Challenge I.6: Bond Energy Calculations
Script to compute C-C bond energy in ethane and C-H bond energy in methane using ASE and EMT.
"""

from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT


def calculate_ethane_cc_bond():
    """Exercise I.6: Compute C-C bond dissociation energy in ethane (C2H6 -> 2 CH3)"""
    # 1. Ethane energy
    ethane = molecule("C2H6")
    ethane.calc = EMT()
    E_ethane = ethane.get_potential_energy()

    # 2. Methyl radical energy
    ch3 = molecule("CH3")
    ch3.calc = EMT()
    E_ch3 = ch3.get_potential_energy()

    # 3. C-C bond energy calculation
    E_bond_CC_eV = 2 * E_ch3 - E_ethane
    E_bond_CC_kj = E_bond_CC_eV * 96.485

    print(f"Ethane Energy: {E_ethane:.4f} eV")
    print(f"Methyl Radical Energy: {E_ch3:.4f} eV")
    print(f"Calculated C-C Bond Energy: {E_bond_CC_eV:.4f} eV")
    print(f"Calculated C-C Bond Energy: {E_bond_CC_kj:.2f} kJ/mol\n")


def calculate_methane_ch_bond():
    """Challenge I.6: Compute C-H bond energy in methane (CH4 -> CH3 + H)"""
    # 1. Methane energy
    methane = molecule("CH4")
    methane.calc = EMT()
    E_methane = methane.get_potential_energy()

    # 2. Methyl radical energy
    ch3 = molecule("CH3")
    ch3.calc = EMT()
    E_ch3 = ch3.get_potential_energy()

    # 3. Hydrogen atom energy
    h_atom = Atoms("H", positions=[(0, 0, 0)])
    h_atom.calc = EMT()
    E_h = h_atom.get_potential_energy()

    # 4. C-H bond energy calculation
    E_bond_CH_eV = (E_ch3 + E_h) - E_methane
    E_bond_CH_kj = E_bond_CH_eV * 96.485

    print(f"Methane Energy: {E_methane:.4f} eV")
    print(f"Methyl Radical Energy: {E_ch3:.4f} eV")
    print(f"Hydrogen Atom Energy: {E_h:.4f} eV")
    print(f"Calculated C-H Bond Energy: {E_bond_CH_eV:.4f} eV")
    print(f"Calculated C-H Bond Energy: {E_bond_CH_kj:.2f} kJ/mol")


if __name__ == "__main__":
    calculate_ethane_cc_bond()
    calculate_methane_ch_bond()
