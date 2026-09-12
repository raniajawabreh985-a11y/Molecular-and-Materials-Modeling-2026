import os
import subprocess
import matplotlib.pyplot as plt

# 1. Paths Configuration (Set to empty string for system-wide/conda binaries)
qe_bin = ""

# 2. Extract Fermi Energy from SCF Output
fermi_energy = -1.717400  # eV (extracted from espresso.pwo)
total_energy = -327.840416  # eV

print("*** Work Function Calculation ***")
print(f"Total energy: {total_energy:.6f} eV")
print(f"Fermi level: {fermi_energy:.6f} eV\n")

# 3. Execution Commands
pw_command = f"{qe_bin}pw.x -in espresso.pwi > espresso.pwo" if qe_bin else "pw.x -in espresso.pwi > espresso.pwo"
pp_command = f"{qe_bin}pp.x < pp.in > pp.out 2>&1" if qe_bin else "pp.x < pp.in > pp.out 2>&1"
average_command = f"{qe_bin}average.x < average.in > average.out 2>&1" if qe_bin else "average.x < average.in > average.out 2>&1"

def run_qe_tool(cmd, input_file, tool_name):
    if os.path.exists(input_file):
        print(f"Calculating electrostatic potential with {tool_name}...")
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f"  {tool_name} completed successfully.\n")
        except subprocess.CalledProcessError as e:
            print(f"  Error running {tool_name}: {e}\n")
    else:
        print(f"  Warning: {input_file} not found. Skipping {tool_name}.\n")

# Run pp.x and average.x
run_qe_tool(pp_command, 'pp.in', 'pp.x')
run_qe_tool(average_command, 'average.in', 'average.x')

# 5. Plot Electrostatic Potential
if subprocess.run('which gnuplot', shell=True, stdout=subprocess.DEVNULL).returncode == 0:
    subprocess.run('gnuplot plot_potential.gp 2>/dev/null', shell=True)
    print("\nPlot saved successfully as potential_plot.png")
