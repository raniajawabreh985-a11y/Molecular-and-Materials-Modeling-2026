# Exercise I.1: AI-Enhanced Scripting

## Overview
This exercise demonstrates the application of AI tools to refine, optimize, and construct robust Python scripts for computational chemistry workflows.

## Features
* **Automated Property Calculation**: Computes molecular mass accurately for targeted systems (e.g., HF).
* **NWChem Output Analysis**: Features error-handled parsing for Quantum Chemical log files.

## Execution
```bash
python3 molecular_property_calculator.py

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

    
    calc = MolecularPropertyCalculator("HF")
    mw = calc.calculate_molecular_mass()
    print(f"Calculated Molecular Weight for {calc.formula}: {mw:.4f} g/mol\n")

    nwchem_file = "hf_cation_nwchem.out"
    calc.parse_nwchem_output(nwchem_file)
