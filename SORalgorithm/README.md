# Successive Over-Relaxation (SOR) – Iterative Method for Solving Linear Systems

This repository includes a Python script that implements the **Successive Over-Relaxation (SOR) method**, an improvement over Jacobi and Gauss–Seidel methods, for solving linear systems of the form:

[
Ax = b
]

The script also automatically calculates the **optimal relaxation parameter (\omega)** based on the spectral radius of the Jacobi iteration matrix, provided the coefficient matrix is **tridiagonal, symmetric, and positive definite**.

---

## How It Works

1. The program asks the user to input:

   - The dimension of the square coefficient matrix **A**.
   - The matrix **A** itself (must be tridiagonal, symmetric, positive definite).
   - The constant vector **b**.
   - The desired error tolerance.

2. The script checks the validity of the matrix (tridiagonal + positive definite).

3. It calculates the optimal relaxation factor:
   [
   \omega = \frac{2}{1 + \sqrt{1 - \rho(H_j)^2}}
   ]
   where (\rho(H_j)) is the spectral radius of the Jacobi iteration matrix.

4. The solution vector is iteratively refined using the SOR formula until the error is below the given threshold.

5. Final results, including the calculated (\omega), are displayed.

---

## Usage

Run the script:

```bash
python sor_solver.py
```

Follow the prompts to enter matrix elements, vector **b**, and error tolerance.

---

## Educational Purpose

This script is designed to help students learn:

- How the **SOR method** improves convergence speed over Jacobi and Gauss–Seidel.
- The role of the **relaxation parameter ((\omega))** in iterative methods.
- Practical applications of **Numerical Linear Algebra** for solving large systems efficiently.
