import os
import matplotlib.pyplot as plt
import numpy as np

# Locate PDOS output file for carbon p-orbitals
pdos_file = "pdos.pdos_atm#1(C)_wfc#2(p)"

if not os.path.exists(pdos_file):
    for f in os.listdir("."):
        if "wfc#2(p)" in f:
            pdos_file = f
            break

if os.path.exists(pdos_file):
    data = np.loadtxt(pdos_file, skiprows=1)

    energy = data[:, 0]
    ldos = data[:, 1]
    pz = data[:, 2]
    px = data[:, 3]
    py = data[:, 4]

    plt.figure(figsize=(8, 5))
    plt.plot(energy, pz, label=r'$p_z$ (Out-of-plane / $\pi$-states)', color='crimson', linewidth=2)
    plt.plot(energy, px + py, label=r'$p_x + p_y$ (In-plane / $\sigma$-states)', color='navy', linestyle='--', linewidth=1.5)
    plt.axvline(x=0, color='gray', linestyle=':', label='Fermi Level ($E_F$)')

    plt.xlabel('Energy - $E_F$ (eV)', fontsize=12)
    plt.ylabel('Projected DOS (states/eV)', fontsize=12)
    plt.title('Graphene Projected Density of States (PDOS)', fontsize=14, fontweight='bold')
    plt.xlim([-10, 10])
    plt.ylim(bottom=0)
    plt.legend(fontsize=11, loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_filename = 'graphene_pdos_final.png'
    plt.savefig(output_filename, dpi=300)
    print(f"PDOS plot successfully saved as '{output_filename}'")
else:
    print(f"Error: PDOS data file '{pdos_file}' not found in current directory.")
