# 문제 9 5차 다항식 보간식

# i = 0, V = -193
# i = -0.5, V = -41
# i = -0.25, V = -13.5625
# i = 0.25, V = 13.5625
# i = 0.5, V = 41
# i = 1, V = 193

import numpy as np

i_data = np.array([0, -0.5, -0.25, 0.25, 0.5, 1])
V_data = np.array([-193, -41, -13.5625, 13.5625, 41, 193])

coeffs = np.polyfit(i_data, V_data, deg=5)

# Print the coefficients
print("5차 다항식 보간식의 계수:")
for idx, coeff in enumerate(coeffs):
    print(f"계수 x^{5 - idx}: {coeff}")

# Print the polynomial
print("\n5차 다항식 보간식:")
polynomial = np.poly1d(coeffs)
print(polynomial)

# i = 0.1 일때 V 값
i_target = 0.1
V_target = polynomial(i_target)
print(f"i = {i_target}일 때 V 값: {V_target}")