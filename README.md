# 🌞 solar-challenge-week0

## Overview
This repository contains the setup and preparation for the Solar Challenge Week 0 project.  
The aim of this week is to establish the development environment, create the Git repository structure, and prepare for data profiling, cleaning, and exploratory data analysis (EDA).

---

## Repository Structure
.vscode/ → VS Code configuration files
.github/workflows/ → Continuous Integration (CI) workflows
.gitignore → Ignored files (includes data/ and CSVs)
requirements.txt → List of dependencies
src/ → Source code folder
scripts/ → Reusable data processing scripts
notebooks/ → Jupyter notebooks for EDA and analysis
tests/ → Unit tests


---

## Environment Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/solar-challenge-week0.git
   cd solar-challenge-week0
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Start Jupyter (for EDA):
   ```bash
   jupyter notebook

---

## Continuous Integration (CI)

A GitHub Actions workflow is configured in .github/workflows/ci.yml.
It installs dependencies and checks Python version on push and pull requests.

---

## Data Folder Notice

A data/ folder will be used locally for raw and cleaned datasets.
Important: data/ and CSV files are excluded from Git tracking via .gitignore.

---

## Next Steps (Week 0 Plan)

Create branches for each country EDA:

eda-benin

eda-sierraleone

eda-togo

Perform EDA in benin_eda.ipynb, sierraleone_eda.ipynb, togo_eda.ipynb.

Export cleaned CSVs to data/ (ignored).

Create compare-countries branch and compare_countries.ipynb for cross-country analysis.

(Optional) Implement Streamlit dashboard under app/ and branch dashboard-dev.

---

## 🌞 Solar Data Discovery Dashboard

This dashboard allows exploration and comparison of solar farm data from **Benin, Sierra Leone, and Togo**.

### How to Run the Dashboard Locally

1. **Activate your virtual environment**:

  ```bash
  # On Linux / macOS
  source venv/bin/activate

  # On Windows
  venv\Scripts\activate

---
## Author
Tsion Mekasha Mamo
GitHub: https://github.com/tsionmekasha/solar-challenge-week0.git

