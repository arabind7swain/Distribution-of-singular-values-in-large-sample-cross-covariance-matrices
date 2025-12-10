# Distribution of Singular Values in Large Sample Cross-Covariance Matrices

This repository contains the Python code and data generation scripts associated with the paper **"Distribution of singular values in large sample cross-covariance matrices"** by Arabind Swain, Sean Alexander Ridout, and Ilya Nemenman, published in Physical Review E (2025).
## 📄 Abstract
Estimating the cross-covariance between two high-dimensional datasets ($X$ and $Y$) is a fundamental problem in data science. When the number of samples $T$ is comparable to the dimensions $N_X$​ and $N_Y$​, sampling fluctuations introduce significant noise, creating spurious correlations even when $X$ and $Y$ are independent. We describe the **Marchenko-Pastur law** equivalent here for cross-covariance matrices.  

This project implements the Random Matrix Theory (RMT) analytical framework derived in the paper to characterize these fluctuations. It provides tools to:
1. **Simulate** large sample cross-covariance matrices ($C=\frac{1}{T}\tilde{Y}^T \tilde{X}$). Here $\tilde{X}$ and $\tilde{Y}$ are row normalized $X$ and $Y$ respectively.
2. **Calculate** the theoretical probability density of singular values by solving the Stieltjes transform cubic equation.
3. **Compute** analytic bounds for the spectrum in various limiting regimes (undersampled, oversampled, and mixed).

## 📊 Key Features
1. **Simulation:** Generation of eigenvalue spectra for products of Wishart matrices (modeling the cross-covariance of uncorrelated Gaussian data).
2. **Semi-Analytic Solver:** Numerical solution of the exact cubic equation for the Stieltjes transform to generate theoretical density curves for any $T$ , $N_X$​​ , $N_Y$ ​. The density curves are for **non-zero eigen values only** that one gets from singular value decomposition when it is **undersampled and mixed**. 
3. **Modular Design:** Clean separation of simulation logic, theoretical calculations, and plotting for easy reuse.

## 🛠️ Installation
Install the required dependencies (Python 3.8+ recommended):

Bash
``` 
pip install numpy matplotlib scipy
```

## 🚀 Usage
### 1. Quick Start

To run the full simulation, calculate the theoretical curve, and generate the plot with default parameters ($T$=500, $N_X$ ​=1000, $N_Y​$ =1000) and 500 independent iterations:

Bash
``` 
python main.py
``` 
This will save the simulation data to simpurenoise0.txt and display the resulting histogram.
### 2. Using the Modules in Your Own Code

The code is split into modular scripts. You can import them into your own scripts or Jupyter Notebooks to explore different parameters.
Python
``` 
import numpy as np
import simulation
import theory
import plotting

# Define Parameters
T, Nx, Ny = 1000, 500, 500  # Example: Undersampled regime
n_iter = 500                # Number of matrix realizations

# 1. Run Simulation
eigenvalues = simulation.run_simulation(n_iter, T, Nx, Ny)

# 2. Get Theoretical Curve
# The theory uses q_x = T/Nx and q_y = T/Ny
max_eig = np.max(eigenvalues)
x_theory, y_theory = theory.calculate_theoretical_density(T, Nx, Ny, max_eig)

# 3. Plot
plotting.plot_results(eigenvalues, x_theory, y_theory)
``` 
## 📂 Repository Structure

* main.py: The driver script. Runs the simulation, computes theory, and generates the plot.

* simulation.py: Handles the generation of Wishart product matrices and eigenvalue computation.

* theory.py: Implements the Stieltjes transform cubic equation to derive the theoretical density.

* plotting.py: Contains functions for visualizing the histogram overlaid with the theoretical curve.

* simpurenoise0.txt: Output file containing the raw eigenvalues from the last run.

## 🔗 Reference

If you use this code or the results in your research, please cite the following paper:
**Distribution of singular values in large sample cross-covariance matrices** Arabind Swain, Sean Alexander Ridout, and Ilya Nemenman, Phys. Rev. E 112, 035312 (2025) DOI: 10.1103/nb6f-4b6p

Bibtex
``` 
@article{nb6f-4b6p,
  title = {Distribution of singular values in large sample cross-covariance matrices},
  author = {Swain, Arabind and Ridout, Sean Alexander and Nemenman, Ilya},
  journal = {Phys. Rev. E},
  volume = {112},
  issue = {3},
  pages = {035312},
  numpages = {8},
  year = {2025},
  month = {Sep},
  publisher = {American Physical Society},
  doi = {10.1103/nb6f-4b6p},
  url = {https://link.aps.org/doi/10.1103/nb6f-4b6p}
}
``` 

