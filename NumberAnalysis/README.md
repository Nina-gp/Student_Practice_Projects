# Pi & e Error Analysis

## Overview
This is a small, beginner-friendly exercise for a **Numerical Analysis** class.
The program calculates approximations of **π (Pi)** and **e (Euler's number)** up to 4 decimal places and explores **error propagation** using simple formulas.

It's a **class practice project**, perfect for understanding rounding, absolute error, and relative error in numerical computations.

---

## How It Works
1. The program takes **π** and **e** from Python's `math` module.
2. It rounds them to **4 decimal places** (a, b).
3. Then it computes the **absolute errors** and checks several **error propagation properties** for addition, subtraction, multiplication, and division.
4. Outputs are rounded to **7 decimal places** for clarity.

---

## Inputs
No input is required from the user.
All values are automatically set to π and e.

---

## Outputs
The program prints:
- Rounded values of π and e.
- Absolute errors of π and e.
- Checks for **error propagation rules**, such as:
  - `e(a+b) <= e(a) + e(b)`
  - `delta(a+b) <= max{delta(a), delta(b)}`
  - `e(ab) <= |a|*e(b) + |b|*e(a)`
  - `e(a/b) <= (b*e(a) + a*e(b))/b^2`

Each check prints `True` or `False` depending on whether the inequality holds.

---

## Purpose
- Understand **rounding errors** and **error propagation** in simple calculations.
- Learn how numerical analysis handles approximations of irrational numbers.
- Practice **Python programming** with math operations and error calculations.

---

## Notes
- This is a **learning exercise** — meant to be simple and illustrative.
- Ideal for students learning **Numerical Analysis basics**.

---

## How to Run
```bash
python PiE_ErrorAnalysis.py
```
No input required. Observe outputs in the console.