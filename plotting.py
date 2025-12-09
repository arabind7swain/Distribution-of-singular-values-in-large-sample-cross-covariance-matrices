import matplotlib.pyplot as plt
import numpy as np

def plot_results(sim_data: np.ndarray, theory_x: np.ndarray, theory_y: np.ndarray):
    """Plots the simulation histogram overlaid with the theoretical curve."""
    plt.figure(figsize=(10, 6))
    
    # Plot Simulation Histogram
    plt.hist(sim_data, density=True, bins=50, color="skyblue", edgecolor='black', alpha=0.6, label='Simulation')
    
    # Plot Theoretical Curve
    plt.plot(theory_x, theory_y, color='red', linewidth=2, linestyle='--', label='Theory (Stieltjes)')
    
    plt.title("Eigenvalue Density: Wishart Product Matrix")
    plt.xlabel("Eigenvalue $\lambda$")
    plt.ylabel("Probability Density $P(\lambda)$")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
