import numpy as np
import simulation
import theory
import plotting

def main():
    # --- Configuration ---
    T = 500
    Nx = 1000
    Ny = 1000
    NUM_ITERATIONS = 10
    
    # --- 1. Simulation ---
    final_eigenvalues = simulation.run_simulation(NUM_ITERATIONS, T, Nx, Ny)
    max_eigenvalue = np.max(final_eigenvalues)
    print(f"Total eigenvalues collected: {len(final_eigenvalues)}")
    print(f"Max eigenvalue: {max_eigenvalue:.2f}")

    # --- 2. Theory ---
    theory_x, theory_y = theory.calculate_theoretical_density(T, Nx, Ny, max_eigenvalue)
    
    # --- 3. Save & Visualize ---
    np.savetxt('simpurenoise0.txt', final_eigenvalues, delimiter=' ')
    plotting.plot_results(final_eigenvalues, theory_x, theory_y)

if __name__ == "__main__":
    main()
