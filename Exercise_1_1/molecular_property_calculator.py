#!/usr/bin/env python3
"""
AI-Enhanced Python Script for Molecular Property & NWChem Log Analysis.
Designed for Molecular and Materials Modeling Workshop 2026.
"""

import os
import sys

ELEMENT_WEIGHTS = {
    "H": 1.008,
    "F": 18.998403,
    "C": 12.011,
    "O": 15.999,
    "N": 14.007,
}


def calculate_molecular_weight(formula_dict):
  mw = sum(
      ELEMENT_WEIGHTS.get(elem, 0) * count
      for elem, count in formula_dict.items()
  )
  return mw


def parse_nwchem_output(filename):
  if not os.path.exists(filename):
    return None

  results = {}
  with open(filename, "r") as f:
    for line in f:
      if "Total energy =" in line:
        results["energy"] = line.split()[-1]
      elif "Projected Frequencies" in line:
        results["freq_section"] = True
  return results


if __name__ == "__main__":
  hf_mw = calculate_molecular_weight({"H": 1, "F": 1})
  print(f"[AI-Script Output] Molecular Weight of HF: {hf_mw:.4f} g/mol")
