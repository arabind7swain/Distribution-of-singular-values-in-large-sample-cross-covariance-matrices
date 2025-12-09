import numpy as np

def calculate_theoretical_density(T: int, Nx: int, Ny: int, max_eig: float):
    """
    Computes the theoretical density curve using the Stieltjes transform cubic equation.
    
    Args:
        T, Nx, Ny: Matrix dimensions
        max_eig: The maximum eigenvalue observed (to set the x-axis range)
    Returns:
        x_vals: The x-axis points (eigenvalues)
        density: The theoretical probability density
    """
    print("Calculating theoretical curve...")
    
    # Ratios (p_x -> q_x and p_y -> q_y)
    q_x = T / Nx
    q_y = T / Ny
    
    # Define range for theoretical calculation (0 to max_eig + buffer)
    steps = np.linspace(0.01, max_eig * 1.1, 1000)
    
    xB = []
    yimgB = []

    epsilon = 0.0001 # Small imaginary shift for regularization
    
    for val in steps:
        # Complex variable z (lambda - i*epsilon)
        z = val - 1j * epsilon 
        
        # Coefficients of the cubic equation for Green's function (g)
        # Based on user provided formula: a13*g^3 + a12*g^2 + a11*g + a10 = 0
        a13 = (z**2) * q_x * q_y
        a12 = (q_y * (1 - q_x) + q_x * (1 - q_y)) * z
        a11 = ((1 - q_x) * (1 - q_y)) - z * q_x * q_y
        a10 = q_x * q_y
        
        # Solve roots of polynomial [a13, a12, a11, a10]
        roots = np.roots([a13, a12, a11, a10])
        
        # Find the correct physical root by taking the max positive imaginary part
        imag_parts = [r.imag for r in roots]
        density_val = max(imag_parts) / np.pi
        
        xB.append(val)
        yimgB.append(density_val)

    return np.array(xB), np.array(yimgB)
