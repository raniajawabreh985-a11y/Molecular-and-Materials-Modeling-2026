# Adsorption of Hydrogen and Mercury on Graphene Substrates

This repository presents Quantum ESPRESSO and ASE simulation results for the adsorption energetics of Hydrogen ($\text{H}$) and Mercury ($\text{Hg}$) atoms on graphene substrates ($\text{C}_8$ and $\text{C}_{18}$).

---

## Summary of Results

| System / Exercise | $E_{\text{slab}}$ (eV) | $E_{\text{adsorbate}}$ (eV) | $E_{\text{total}}$ (eV) | Binding Energy (eV) | Notes / Condition |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Primary Exercise ($\text{H@C}_8$)** | `-1288.941908` | `-12.559509` | `-1319.069282` | **17.5679** | Unrelaxed $\text{C}_8$ slab ($ecutwfc = 30\text{ Ry}$) |
| **2. Challenge 1 (Relaxed $\text{C}_8$)** | `-1288.937073` | `-12.559509` | `-1319.069282` | **17.5727** | Fully relaxed $\text{C}_8$ slab ($ecutwfc = 30\text{ Ry}$) |
| **3. Challenge 2 ($ecutwfc$ Convergence)**| `-1297.847139` | `-12.536428` | `-1313.276897` | **2.8933** | Cutoff test at $ecutwfc = 40\text{ Ry}$ |
| **4. Challenge 3 ($\text{Hg@C}_{18}$)** | `-2915.479553` | `-4525.061570` | `-7441.141316` | **0.6002** | Larger $\text{C}_{18}$ substrate ($ecutwfc = 30\text{ Ry}$) |

---

## Detailed Breakdown & Methodology

### 1. Primary Exercise: $\text{H}$ Adsorption on $\text{C}_8$

Calculated the binding energy of a single Hydrogen atom on a $\text{C}_8$ graphene surface using standard parameters ($ecutwfc = 30.0\text{ Ry}$).

$$\text{Binding Energy} = E(\text{C}_8) + E(\text{H}) - E(\text{H@C}_8)$$

| Component | Description | Energy (eV) |
| :--- | :--- | :---: |
| $E(\text{C}_8)$ | Unrelaxed $\text{C}_8$ graphene slab | `-1288.941908` |
| $E(\text{H})$ | Isolated Hydrogen atom | `-12.559509` |
| $E(\text{H@C}_8)$ | Total combined adsorption system | `-1319.069282` |
| **$E_{\text{binding}}$** | **Calculated Binding Energy** | **`17.5679 eV`** |

* **Execution:**
  ```bash
  python3 run_adsorption.py

---

### 2. Challenge 1: Relaxation of $\text{C}_8$ Substrate

Optimized the atomic positions of the isolated $\text{C}_8$ slab using the BFGS algorithm ($f_{\text{max}} < 0.05\text{ eV/\AA}$).

| Parameter | Value |
| :--- | :---: |
| **Relaxed $E(\text{C}_8)$** | `-1288.937073 eV` |
| **Updated Binding Energy** | **`17.5727 eV`** |

* **Execution:**
  ```bash
  python3 relaxation_c.py

---

### 3. Challenge 2: Plane-Wave Cutoff Convergence ($ecutwfc = 40.0\text{ Ry}$)

Evaluated energy convergence by increasing the wave-function kinetic energy cutoff from $30.0\text{ Ry}$ to $40.0\text{ Ry}$.

| System Component | Energy at $40\text{ Ry}$ (eV) |
| :--- | :---: |
| $E(\text{C}_8)$ | `-1297.847139` |
| $E(\text{H})$ | `-12.536428` |
| $E(\text{H@C}_8)$ | `-1313.276897` |
| **New Binding Energy** | **`2.8933 eV`** |

* **Execution:**
  ```bash
  python3 test_ecut.py

---

### 4. Challenge 3: Mercury ($\text{Hg}$) Adsorption on $\text{C}_{18}$ Substrate

Extended the adsorption study to a larger $\text{C}_{18}$ graphene supercell interacting with a single Mercury atom.

| Component | Description | Energy (eV) |
| :--- | :--- | :---: |
| $E(\text{C}_{18})$ | Pure $\text{C}_{18}$ substrate | `-2915.479553` |
| $E(\text{Hg})$ | Isolated Mercury atom | `-4525.061570` |
| $E(\text{Hg@C}_{18})$ | Total $\text{Hg}$ on $\text{C}_{18}$ complex | `-7441.141316` |
| **$E_{\text{binding}}$** | **Calculated Binding Energy ($\text{Hg@C}_{18}$)** | **`0.6002 eV`** |

* **Execution:**
  ```bash
  python3 run_c18.py
  python3 run_hg.py
 
