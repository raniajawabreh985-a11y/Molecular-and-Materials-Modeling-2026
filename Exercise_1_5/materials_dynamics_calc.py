
cat << 'EOF' > materials_dynamics_calc.py
#!/usr/bin/env python3
"""
Exercise I.5: Materials & Molecular Dynamics
Simulation of solid structure lattice/energy and MD temperature trajectory using ASE EMT.
"""

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

def run_materials_simulation():
    # Setup Bulk Gold (Au) System
    atoms = bulk('Au', 'fcc', a=4.08)
    atoms.calc = EMT()
    e_bulk = atoms.get_potential_energy()
    
    # Initialize MD at 300 K
    MaxwellBoltzmannDistribution(atoms, temperature_K=300)
    dyn = VelocityVerlet(atoms, 1.0 * units.fs)
    
    # Run short trajectory
    dyn.run(50)
    e_md = atoms.get_potential_energy()
    
    return e_bulk, e_md

e_b, e_m = run_materials_simulation()

print(f"{'Simulation Phase':<25} | {'Potential Energy (eV)':<20}")
print("-" * 50)
print(f"{'Bulk Au (Lattice Opt)':<25} | {e_b:<20.4f}")
print(f"{'Bulk Au (Post-MD 300K)':<25} | {e_m:<20.4f}")
EOF

python3 materials_dynamics_calc.py
