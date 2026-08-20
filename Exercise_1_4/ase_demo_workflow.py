cd ~/Desktop/Molecular-and-Materials-Modeling-2026-August/
cat << 'EOF' > ase_demo_workflow.py
#!/usr/bin/env python3
"""
Exercise I.4: ASE Demonstration Examples & Challenge Workflows
Executes ASE structural manipulation and potential energy evaluation from directory workflows.
"""

from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

def run_ase_demo():
    # 1. Molecule geometry optimization (N2 molecule)
    d = 1.1
    molecule = Atoms('N2', positions=[(0, 0, 0), (0, 0, d)])
    molecule.calc = EMT()
    
    e_init = molecule.get_potential_energy()
    dyn = BFGS(molecule, logfile=None)
    dyn.run(fmax=0.01)
    e_opt = molecule.get_potential_energy()
    d_opt = molecule.get_distance(0, 1)
    
    return e_init, e_opt, d_opt

e_i, e_o, d_final = run_ase_demo()

print(f"{'ASE Task':<30} | {'Result':<18}")
print("-" * 52)
print(f"{'Initial Energy (eV)':<30} | {e_i:<18.4f}")
print(f"{'Optimized Energy (eV)':<30} | {e_o:<18.4f}")
print(f"{'Optimized Bond Length (A)':<30} | {d_final:<18.4f}")
EOF

python3 ase_demo_workflow.py
