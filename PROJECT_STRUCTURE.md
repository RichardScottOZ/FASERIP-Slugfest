# Project Structure

## Before Reorganization
```
FASERIP-Slugfest/
├── 14 CSV files (scattered in root)
├── 4 Jupyter notebooks (in root)
├── 1 pickle file (in root)
├── PowersFix.txt (in root)
├── DnD-battler/
│   └── 20+ runtest*.py files
├── .idea/ (tracked in git)
└── minimal documentation
```

## After Reorganization
```
FASERIP-Slugfest/
├── README.md (improved, 180 lines)
├── CONTRIBUTING.md (new, 134 lines)
├── LICENSE
├── requirements.txt (improved with comments)
├── .gitignore (updated to exclude IDE files)
│
├── DnD-battler/          # Core simulator package
│   ├── DnD_battler/      # Python package
│   ├── setup.py
│   └── README.md
│
├── examples/             # Example scripts (22 files)
│   ├── README.md (new, explains all examples)
│   ├── simple_battle.py (new, easy entry point)
│   └── runtestFASERIP-*.py (moved from DnD-battler/)
│
├── notebooks/            # Jupyter notebooks (4 files)
│   ├── README.md (new, explains usage)
│   ├── FASERIP Character Generator.ipynb
│   ├── FASERIP Character Generator-Test.ipynb
│   ├── FASERIP-Martial_Artists.ipynb
│   └── FASERIP-Training-Data.ipynb
│
├── data/                 # Data files (15 files)
│   ├── README.md (new, explains all data files)
│   ├── benriely.csv (7.3MB character database)
│   ├── superheroapi.pkl
│   ├── PowersFix.csv / PowersFix.txt
│   ├── TalentsFix.csv
│   ├── EquipmentFix.csv
│   └── ... (other data files)
│
├── Slugfest/            # Additional utilities
├── olddata/             # Reference data
└── .idea/               # (removed from git tracking)
```

## Key Improvements

1. **Organization**: Files grouped by purpose (data, examples, notebooks)
2. **Documentation**: 5 new/improved README files + CONTRIBUTING.md
3. **User Experience**: Clear entry points, better structure
4. **Maintenance**: IDE files excluded, better .gitignore
5. **Discoverability**: Each directory explains its contents

## Benefits

- **For New Users**: Clear quickstart example, organized structure
- **For Developers**: CONTRIBUTING.md with guidelines, organized code
- **For Contributors**: Clear structure, easy to find relevant files
- **For Maintenance**: Less clutter, better organized, self-documenting
