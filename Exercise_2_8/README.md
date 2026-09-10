# Adsorption of Hydrogen on Graphene (C8)

This project models the adsorption of a Hydrogen (H) atom on a graphene slab (C8) using Quantum ESPRESSO via ASE.

---

## Workflow & Methodology

### Step 1: Geometry Optimization (H@C8)
Optimizes the position of the H atom adsorbed on the C8 graphene surface.

* **Script:** `relaxation.py`
* **Execution:**
  python3 relaxation.py

  * **Output:**
    Total Energy                : -1319.069282 eV
ASE-style max force (norm)  : 0.003278 eV/A
QE-style max force          : 0.003278 eV/A
Pressure                    : 26.532360 kbar

---

### Step 2: Isolated Hydrogen Atom SCF (H)
Calculates the total energy of an isolated H atom in a box.

* **Script:** `energy_h.py`
* **Execution:**
 python3 energy_h.py

* **Output:** 
Total energy                : -12.559509 eV
Fermi level                 : -6.462900 eV

---

### Step 3: Pristine Graphene Slab SCF (C8)
Calculates the total energy of the pristine C8 surface without adsorption.

* **Script:** `energy_c.py`
* **Execution:**
 python3 energy_c.py

* **Output:**
 Total energy                : -1303.645873 eV

Fermi level                 : -1.813400 eV

 ---

## Summary of Results & Binding Energy

### Energy Summary
* **E(H@C8):** -1319.069282 eV
* **E(C8):** -1303.645873 eV
* **E(H):** -12.559509 eV

### Binding Energy Calculation
Binding Energy = E(C8) + E(H) - E(H@C8)

Binding Energy = -1303.645873 + (-12.559509) - (-1319.069282) = **2.8639 eV**

---

## Challenge Exercises

* Modify the Python script to perform the relaxation of the C8 slab and recalculate the adsorption energy.
* Increase the `ecutwfc` parameter to evaluate convergence of the H@C8 binding energy.
* Enlarge the slab to C18 (similar to Hg adsorption) and evaluate the binding energy changes.
 
