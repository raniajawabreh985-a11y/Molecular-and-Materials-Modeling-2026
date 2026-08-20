
cat << 'EOF' > ts_barrier_calc.py
#!/usr/bin/env python3
"""
Exercise I.4: Transition State & Reaction Barrier Calculation
Evaluates Reactant, Transition State (TS), and Product potential energies using ASE.
"""

from ase import Atoms
from ase.calculators.emt import EMT
import numpy as np

def calculate_barrier():
    # Reactant state (separated/initial)
    r_state = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.74)], calculator=EMT())
    e_react = r_state.get_potential_energy()
    
    # Transition State (stretched bond)
    ts_state = Atoms('H2', positions=[(0, 0, 0), (0, 0, 1.20)], calculator=EMT())
    e_ts = ts_state.get_potential_energy()
    
    # Product state
    p_state = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.75)], calculator=EMT())
    e_prod = p_state.get_potential_energy()
    
    e_barrier = e_ts - e_react
    return e_react, e_ts, e_prod, e_barrier

e_r, e_ts, e_p, e_b = calculate_barrier()

print(f"{'State':<18} | {'Energy (eV)':<12}")
print("-" * 35)
print(f"{'Reactants':<18} | {e_r:<12.4f}")
print(f"{'Transition State':<18} | {e_ts:<12.4f}")
print(f"{'Products':<18} | {e_p:<12.4f}")
print(f"{'Activation Barrier':<18} | {e_b:<12.4f}")
EOF

python3 ts_barrier_calc.py
