# COBRApy FBA Modeling

This repository contains Python scripts developed as part of an internship project focused on metabolic modeling using the **COBRApy** package. The core task involves performing **Flux Balance Analysis (FBA)** on metabolic network models to simulate and analyze biological pathways.

## 📁 Contents

- `fba_analysis_initial.py`:  
  The first version of the script that performs FBA on an SBML metabolic model and prints out the top fluxes by magnitude.

- `fba_analysis_optimized.py`:  
  An improved version of the script with enhanced code structure, efficiency, and modularity.

## 🚀 Features

- Loads SBML-formatted metabolic models
- Runs Flux Balance Analysis (FBA)
- Outputs:
  - Optimal objective value
  - Top 10 fluxes sorted by absolute magnitude
- Uses **COBRApy** for modeling and **pandas** for data handling

## 🧪 Requirements

To run the scripts, make sure you have the following Python packages installed:

```bash
pip install cobra pandas
