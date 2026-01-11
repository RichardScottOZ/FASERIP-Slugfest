# Jupyter Notebooks

This directory contains Jupyter notebooks for character generation and analysis.

## Notebooks

### Character Generation
- **FASERIP Character Generator.ipynb** - Main character generator using Ultimate Powers Book rules
  - Creates random FASERIP characters
  - Outputs to JSON and CSV formats compatible with the simulator
  - Use this notebook (not the test version)

- **FASERIP Character Generator-Test.ipynb** - Test/development version of the character generator

### Data Analysis
- **FASERIP-Training-Data.ipynb** - Parses Ben Riely's character website and creates CSV in beastiary format
- **FASERIP-Martial_Artists.ipynb** - Analysis of martial artist characters

## Using the Notebooks

### Online (Binder)
You can run these notebooks online without installation using Binder:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bluetyson/FASERIP-Slugfest/HEAD?urlpath=https%3A%2F%2Fgithub.com%2Fbluetyson%2FFASERIP-Slugfest%2Fblob%2Fmain%2Fnotebooks%2FFASERIP%2520Character%2520Generator.ipynb)

### Local Installation
1. Install Jupyter: `pip install jupyter`
2. Install dependencies: `pip install pandas tqdm`
3. Run: `jupyter notebook`
4. Open the desired notebook from the browser interface

## Output

The character generator notebooks can create characters in two formats:
1. Original format - 100 characters with basic attributes
2. Beastiary format - Characters formatted for use with the FASERIP Slugfest simulator

Characters are saved to CSV files in the `../data/` directory.
