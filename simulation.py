import numpy as np

def generate_wishart_product_eigenvalues(T: int, Nx: int, Ny: int) -> np.ndarray:
    """
    Generates two random matrices (X and Y), computes their Wishart product matrix,
    and returns the eigenvalues.
    
    Formula: B1 = ( (X @ X.T) @ (Y @ Y.T) ) / T^2
    """
    # Generate Random Matrices
    X = np.random.normal(0, 1, size=(T, Nx))
    Y = np.random.normal(0, 1, size=(T, Ny))
    
    # Compute Wishart Matrices
    # A = X X^T
    A = np.matmul(X, X.T)
    # A1 = Y Y^T
    A1 = np.matmul(Y, Y.T)
    
    # Compute Product Matrix B and Normalize
    B = np.matmul(A, A1)
    B1 = B * (1 / (T * T))
    
    # Compute Eigenvalues
    # We take the real part to remove numerical noise 
    return np.real(np.linalg.eigvals(B1))

def run_simulation(n_simulations: int, T: int, Nx: int, Ny: int) -> np.ndarray:
    """Runs the eigenvalue generation simulation multiple times."""
    print(f"Starting simulation: {n_simulations} iterations...")
    all_eigenvalues = []
    
    for i in range(n_simulations):
        if i % 100 == 0:
            print(f"Processing iteration {i}/{n_simulations}")
        eigs = generate_wishart_product_eigenvalues(T, Nx, Ny)
        all_eigenvalues.append(eigs)
        
    return np.concatenate(all_eigenvalues)

