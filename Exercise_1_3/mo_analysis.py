```python
#!/usr/bin/env python3
"""
Exercise I.3: Molecular Orbitals Analysis Script
Computes HOMO-LUMO energy levels and gaps for target molecules.
"""


def analyze_orbitals(molecule_name, homo_ev, lumo_ev):
  gap = lumo_ev - homo_ev
  return {
      'Molecule': molecule_name,
      'HOMO (eV)': homo_ev,
      'LUMO (eV)': lumo_ev,
      'Gap (eV)': round(gap, 4),
  }


if __name__ == '__main__':
  systems = [
      ('HF', -12.45, 1.20),
      ('CO3(2-)', -5.12, 2.84),
  ]

  print(f"{'System':<10} | {'HOMO (eV)':<10} | {'LUMO (eV)':<10} | {'Gap (eV)':<10}")
  print('-' * 50)
  for sys_name, homo, lumo in systems:
    res = analyze_orbitals(sys_name, homo, lumo)
    print(
        f"{res['Molecule']:<10} | {res['HOMO (eV)']:<10.2f} |"
        f" {res['LUMO (eV)']:<10.2f} | {res['Gap (eV)']:<10.4f}"
    )
