import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Configurations ---
prefix = 'Si'
outdir = './out'
pseudo_dir = '.'
pseudopotentials = {'Si': 'Si.upf'}

pw_command = "pw.x < {input_file} > {output_file} 2>&1"
pp_command = "pp.x < {input_file} > {output_file} 2>&1"
projwfc_command = "projwfc.x < {input_file} > {output_file} 2>&1"
dos_command = "dos.x < {input_file} > {output_file} 2>&1"

os.makedirs(outdir, exist_ok=True)
os.makedirs('pdos_results', exist_ok=True)

# --- 2. Step 1: SCF Calculation ---
print("Running SCF calculation...")
scf_input = f"""
&CONTROL
  calculation = 'scf'
  restart_mode = 'from_scratch'
  prefix = '{prefix}'
  pseudo_dir = '{pseudo_dir}'
  outdir = '{outdir}'
/
&SYSTEM
  ibrav = 2, celldm(1) = 10.26, nat = 2, ntyp = 1,
  ecutwfc = 30.0
/
&ELECTRONS
  conv_thr = 1.0d-8
/
ATOMIC_SPECIES
  Si 28.0855 Si.upf
ATOMIC_POSITIONS (alab)
  Si 0.00 0.00 0.00
  Si 0.25 0.25 0.25
K_POINTS (automatic)
  6 6 6 1 1 1
"""

with open('scf.in', 'w') as f:
    f.write(scf_input)

subprocess.run(pw_command.format(input_file='scf.in', output_file='scf.out'), shell=True, check=True)

# Extract SCF Total Energy
with open('scf.out', 'r') as f:
    for line in f:
        if '!' in line and 'total energy' in line:
            total_energy_ry = float(line.split('=')[1].split('Ry')[0].strip())
            total_energy_ev = total_energy_ry * 13.605698066
            print(f"  Total energy: {total_energy_ev:.6f} eV")

# --- 3. Step 2: Löwdin Charges & Charge Density Analysis ---
print("\n[Phase A.] Extracting charge density and Löwdin charges from SCF calculation...")

print("\n1. Calculating charge density from SCF...")
pp_input = f"""
&INPUTPP
  prefix = '{prefix}'
  outdir = '{outdir}'
  filplot = 'charge_density'
  plot_num = 0
/
&PLOT
  nfile = 1
  filepp(1) = 'charge_density'
  weight(1) = 1.0
  iflag = 3
  output_format = 6
  fileout = 'charge_density.cube'
/
"""
with open('pp.in', 'w') as f:
    f.write(pp_input)

subprocess.run(pp_command.format(input_file='pp.in', output_file='pp.out'), shell=True, check=True)
print("   pp.x completed successfully")

print("\n2. Running projwfc.x on SCF...")
projwfc_scf_input = f"""
&PROJWFC
  prefix = '{prefix}'
  outdir = '{outdir}'
  lsym = .true.
  filpdos = 'scf_pdos'
/
"""
with open('projwfc_scf.in', 'w') as f:
    f.write(projwfc_scf_input)

subprocess.run(projwfc_command.format(input_file='projwfc_scf.in', output_file='projwfc_scf.out'), shell=True, check=True)
print("   projwfc.x completed successfully")

print("\n3. Extracting Löwdin charges from SCF (projwfc.out)...")
with open('projwfc_scf.out', 'r') as infile, open('lowdin.out', 'w') as outfile:
    recording = False
    for line in infile:
        if "Lowdin Charges:" in line or "Löwdin Charges:" in line:
            recording = True
        if recording:
            outfile.write(line)
            if "Spilling Parameter" in line:
                print(f"   {line.strip()}")
                recording = False
print("   Löwdin charges saved to lowdin.out")

# --- 4. Step 3: NSCF Calculation for DOS ---
print("\nCleaning up SCF files and preparing for NSCF calculation...")
os.makedirs('scf_files', exist_ok=True)
subprocess.run("mv scf.in scf.out pp.in pp.out projwfc_scf.in projwfc_scf.out scf_files/ 2>/dev/null", shell=True)
print("  Moved all SCF-related files to scf_files directory")

print("\nRunning NSCF calculation for DOS with k-grid (30, 30, 30)...")
nscf_input = f"""
&CONTROL
  calculation = 'nscf'
  restart_mode = 'from_scratch'
  prefix = '{prefix}'
  pseudo_dir = '{pseudo_dir}'
  outdir = '{outdir}'
/
&SYSTEM
  ibrav = 2, celldm(1) = 10.26, nat = 2, ntyp = 1,
  ecutwfc = 30.0,
  nosym = .false.
/
&ELECTRONS
  conv_thr = 1.0d-8
/
ATOMIC_SPECIES
  Si 28.0855 Si.upf
ATOMIC_POSITIONS (alab)
  Si 0.00 0.00 0.00
  Si 0.25 0.25 0.25
K_POINTS (automatic)
  30 30 30 0 0 0
"""
with open('nscf.in', 'w') as f:
    f.write(nscf_input)

subprocess.run(pw_command.format(input_file='nscf.in', output_file='nscf.out'), shell=True, check=True)

# Extract Fermi Level
fermi_level = None
with open('nscf.out', 'r') as f:
    for line in f:
        if 'the Fermi energy is' in line:
            fermi_level = float(line.split('is')[1].split('ev')[0].strip())
            print(f"  Fermi level: {fermi_level:.4f} eV")

# --- 5. Step 4: Total & Partial DOS Calculation ---
print("\n4. Calculating Total DOS...")
dos_input = f"""
&DOS
  prefix = '{prefix}'
  outdir = '{outdir}'
  fildos = 'total_dos.dat'
  Emin = -20.0, Emax = 25.0, DeltaE = 0.01
/
"""
with open('dos.in', 'w') as f:
    f.write(dos_input)

subprocess.run(dos_command.format(input_file='dos.in', output_file='dos.out'), shell=True, check=True)
print("   dos.x completed successfully")

print("\n5. Calculating PDOS from NSCF...")
projwfc_nscf_input = f"""
&PROJWFC
  prefix = '{prefix}'
  outdir = '{outdir}'
  filpdos = 'pdos'
  Emin = -20.0, Emax = 25.0, DeltaE = 0.01
/
"""
with open('projwfc_nscf.in', 'w') as f:
    f.write(projwfc_nscf_input)

subprocess.run(projwfc_command.format(input_file='projwfc_nscf.in', output_file='projwfc_nscf.out'), shell=True, check=True)
print("   projwfc.x completed successfully")

# Organize PDOS files into designated directory
subprocess.run("mv pdos.pdos* projections.projwfc_up pdos_results/ 2>/dev/null", shell=True)

print("\n=== Electronic Structure Analysis Complete ===")
print("Generated files:")
print(" - Charge density (from SCF): charge_density.cube")
print(" - Löwdin Charges (from SCF): lowdin.out")
print(" - Total DOS (from NSCF): total_dos.dat")
print(" - PDOS files (from NSCF): pdos_results/")
