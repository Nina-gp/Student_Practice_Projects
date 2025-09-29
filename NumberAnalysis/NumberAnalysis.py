#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

# Original numbers
PI = math.pi
E = math.e

# Rounded approximations (4 decimal digits)
approx_pi = round(PI, 4)
approx_e = round(E, 4)

print("Original numbers: PI =", PI, "& E =", E)
print("Rounded approximations: a =", approx_pi, ", b =", approx_e)

# Absolute errors
abs_error_pi = round(abs(PI - approx_pi), 7)
abs_error_e = round(abs(E - approx_e), 7)
total_abs_error = round(abs_error_pi + abs_error_e, 7)

# Error in sum and difference
error_sum = round((PI + E) - (approx_pi + approx_e), 7)
error_diff = round((PI - E) - (approx_pi - approx_e), 7)

print("\nCheck absolute error propagation for sum: e(a+b) <= e(a)+e(b)?")
print(error_sum <= total_abs_error)

print("Check absolute error propagation for difference: e(a-b) <= e(a)+e(b)?")
print(error_diff <= total_abs_error)

# Relative errors
rel_error_pi = round(abs(PI - approx_pi)/PI, 7)
rel_error_e = round(abs(E - approx_e)/E, 7)

rel_error_sum = round(error_sum/(PI + E), 7)
print("Check relative error propagation for sum: delta(a+b) <= max(delta a, delta b)?")
print(rel_error_sum <= max(rel_error_pi, rel_error_e))

rel_error_diff = round((PI - E - (approx_pi - approx_e))/(PI - E), 7)
upper_bound_diff = (approx_pi/(approx_pi - approx_e))*rel_error_pi + (approx_e/(approx_pi - approx_e))*rel_error_e
print("Check relative error propagation for difference: delta(a-b) <= (a/(a-b))*delta_a + (b/(a-b))*delta_b ?")
print(rel_error_diff <= upper_bound_diff)

# Error propagation for multiplication
error_mul = round(abs((PI*E) - (approx_pi*approx_e)), 7)
bound_mul = round(abs(approx_pi*(E-approx_e)) + abs(approx_e*(PI-approx_pi)), 7)
print("Check absolute error propagation for multiplication: e(ab) <= |a|*e(b) + |B|*e(a)?")
print(error_mul <= bound_mul)

# Error propagation for division
error_div = round((PI/E - approx_pi/approx_e), 7)
bound_div = round((approx_e*abs(PI-approx_pi) + approx_pi*abs(E-approx_e))/approx_e**2, 7)
print("Check absolute error propagation for division: e(a/b) <= (b*e(a) + a*e(b))/b^2?")
print(error_div <= bound_div)

# Relative error propagation for multiplication
rel_error_mul = round(error_mul/(PI*E), 7)
rel_error_sum_mul = round(rel_error_pi + rel_error_e, 7)
print("Check relative error propagation for multiplication: delta(ab) <= delta(a) + delta(b)?")
print(rel_error_mul <= rel_error_sum_mul)

