# Exercise I.1: AI-Enhanced Scripting

## Overview
This exercise demonstrates the application of AI tools to refine, optimize, and construct robust Python scripts for computational chemistry workflows.

## Features
* **Automated Property Calculation**: Computes molecular mass accurately for targeted systems (e.g., HF).
* **NWChem Output Analysis**: Features error-handled parsing for Quantum Chemical log files.

## Execution
```bash
python3 molecular_property_calculator.py

## Scripts Included

### 1. Original Basic Script (`basic_script.py`)
```python
def get_molecular_weight(molecule):
    weights = {'H': 1.008, 'F': 18.998, 'N': 14.007, 'O': 15.999}
    if molecule == 'HF':
        return weights['H'] + weights['F']
    return 0

def read_nwchem_output(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if 'Total DFT energy' in line:
            print(line)

mw = get_molecular_weight('HF')
print(f"Molecular weight of HF: {mw} g/mol")
read_nwchem_output('hf_cation_nwchem.out')

import os
import re

class MolecularPropertyCalculator:
    """
    AI-Enhanced Script for Computational Chemistry Workflows:
    - Calculates molecular mass accurately for targeted systems (e.g., HF).
    - Parses NWChem log files with robust error handling.
    """
    
    ATOMIC_WEIGHTS = {
        'H': 1.00794,
        'F': 18.998403,
        'N': 14.0067,
        'O': 15.9994,
        'C': 12.0107
    }

    def __init__(self, molecule_formula="HF"):
        self.formula = molecule_formula

    def calculate_molecular_mass(self):
        elements = re.findall(r'([A-Z][a-z]?)(\d*)', self.formula)
        total_mass = 0.0

        for element, count in elements:
            if not element:
                continue
            num = int(count) if count else 1
            if element in self.ATOMIC_WEIGHTS:
                total_mass += self.ATOMIC_WEIGHTS[element] * num
            else:
                raise ValueError(f"Element '{element}' not found in standard atomic weight database.")
        
        return total_mass

    def parse_nwchem_output(self, file_path):
        if not os.path.exists(file_path):
            print(f"[Warning] NWChem log file '{file_path}' not found in the current directory.")
            return None

        total_energy = None
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if "Total DFT energy" in line:
                        parts = line.split()
                        total_energy = float(parts[-1])
            
            if total_energy is not None:
                print(f"[Success] Extracted Total DFT Energy: {total_energy} Hartree")
            else:
                print(f"[Info] 'Total DFT energy' key not found in {file_path}")

        except Exception as e:
            print(f"[Error] Failed to read NWChem output file: {e}")

        return total_energy


if __name__ == "__main__":
    print("=== AI-Enhanced Molecular Property Calculator ===")
    
    calc = MolecularPropertyCalculator("HF")
    mw = calc.calculate_molecular_mass()
    print(f"Calculated Molecular Weight for {calc.formula}: {mw:.4f} g/mol\n")

    nwchem_file = "hf_cation_nwchem.out"
    calc.parse_nwchem_output(nwchem_file)
