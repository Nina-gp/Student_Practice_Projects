# Jacobi Algorithm – Iterative Method for Solving Linear Systems

This repository contains two Python scripts that implement the **Jacobi iterative method** for solving systems of linear equations of the form:

[
Ax = b
]

The scripts are tailored for specific matrix sizes and are intended as part of exercises in **Linear Algebra** course.

---

## Files

- **`Jacobi_algorithm_6_6.py`**
  Solves a linear system with a **6×6 coefficient matrix** using the Jacobi iterative method.

- **`Jacobi_algorithm_13_13.py`**
  Solves a linear system with a **13×13 coefficient matrix** using the same method.

---

## How It Works

1. The program asks the user to input:

   - The coefficient matrix **A** (square: 6×6 or 13×13 depending on the script).
   - The constant vector **b** (column vector).
   - The desired **error threshold** for approximation.

2. The script checks whether the given matrix **A** is:

   - Square
   - Symmetric
   - Positive definite (all leading principal minors have positive determinants)

   This ensures convergence of the Jacobi method.

3. The algorithm starts with an initial guess ( x^{(0)} = [0, 0, …, 0]^T ) and iteratively applies:

   [
   x^{(k+1)} = D^{-1}(b - (L + U)x^{(k)})
   ]

   where:

   - ( D ) = diagonal part of ( A )
   - ( L ) = lower triangular part
   - ( U ) = upper triangular part

4. Iterations continue until the error (infinity norm of the difference between successive approximations) is less than the user-defined threshold.

5. The final approximate solution vector **X** is printed.

---

## Usage

Run either script directly:

```bash
python Jacobi_algorithm_6_6.py
```

or

```bash
python Jacobi_algorithm_13_13.py
```

Follow the prompts to enter matrix elements and error tolerance.

---

## Requirements

- Python 3.x
- NumPy

Install dependencies:

```bash
pip install numpy
```

---

## Educational Purpose

These scripts are designed to help students understand:

- The implementation of the **Jacobi iterative method**.
- Convergence conditions for iterative solvers.
- Practical application of linear algebra.

---
