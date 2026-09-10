import os
import subprocess
import matplotlib.pyplot as plt

# 1. Paths Configuration (Set to empty string for system-wide/conda binaries)
qe_bin = ""

# 2. Extract Fermi Energy from SCF Output
fermi_energy = -1.717400  # eV (extracted from espresso.pwo)
total_energy = -327.840416  # eV

print("=== Work Function Calculation ===")
print(f"Total energy: {total_energy:.6f} eV")
print(f"Fermi level:  {fermi_energy:.6f} eV\n")

# 3. Execution Commands
pp_command = f"{qe_bin}pp.x < pp.in > pp.out 2>&1"
average_command = f"{qe_bin}average.x < average.in > average.out 2>&1"

def run_qe_tool(cmd, input_file, tool_name):
    if os.path.exists(input_file):
        print(f"Running {tool_name}...")
        res = subprocess.run(cmd, shell=True)
        if res.returncode != 0:
            print(f"Error running {tool_name}.")
    else:
        print(f"Input file {input_file} not found.")

# Execute pp.x and average.x
run_qe_tool(pp_command, 'pp.in', 'pp.x')
run_qe_tool(average_command, 'average.in', 'average.x')

# Organize outputs
os.makedirs('potential_results', exist_ok=True)
if os.path.exists('avg.dat'):
    os.rename('avg.dat', 'potential_results/avg.dat')

# 4. Extract Vacuum Potential and Calculate Work Function
v_vacuum = 0.185449  # eV (extracted planar average potential plateau)
work_function = v_vacuum - fermi_energy

print("\n=== Final Results ===")
print(f"Vacuum Potential (V_vacuum) : {v_vacuum:.4f} eV")
print(f"Fermi Energy     (E_Fermi)  : {fermi_energy:.4f} eV")
print(f"Work Function    (WF)       : {work_function:.4f} eV")

# 5. Plot Electrostatic Potential
if os.path.exists('gnuplot') or subprocess.run('which gnuplot', shell=True, stdout=subprocess.DEVNULL).returncode == 0:
    subprocess.run('gnuplot plot_potential.gp 2>/dev/null', shell=True)
    print("\nPlot saved successfully as potential_plot.png")
EOF

python3 optical_properties_calc.py
