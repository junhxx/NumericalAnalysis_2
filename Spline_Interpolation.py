# 문제 8 Spline 보간법

# 온도 40 : 기전력 1.36
# 온도 48 : 기전력 1.67
# 온도 56 : 기전력 2.12
# 온도 64 : 기전력 2.36
# 온도 72 : 기전력 2.72
# 온도 80 : 기전력 3.19

#(a)
import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([40, 48, 56, 64, 72, 80])
y_data = np.array([1.36, 1.67, 2.12, 2.36, 2.72, 3.19])

plt.scatter(x_data, y_data, label='Data points', marker='o', color='red')
plt.plot(x_data, y_data, label='Interpolation', color='blue')
plt.xlabel('Temperature')
plt.ylabel('Thermal power')
plt.title('Temperature vs. Thermal power')
plt.legend()
plt.show()


#(b)
import numpy as np

def cubic_spline_coeffs(x, y):
    n = len(x) - 1
    h = np.diff(x)
    df = np.diff(y) / h
    A = np.zeros((n-1, n-1))
    b = np.zeros(n-1)
    for i in range(n-1):
        if i > 0:
            A[i, i-1] = h[i]
        A[i, i] = 2 * (h[i] + h[i+1])
        if i < n-2:
            A[i, i+1] = h[i+1]
        b[i] = 6 * (df[i+1] - df[i])
    
    c = np.zeros(n+1)
    c[1:-1] = np.linalg.solve(A, b)
    
    d = np.diff(c) / (6 * h)
    b = df - h * (2 * c[:-1] + c[1:]) / 6
    
    return y, b, c, d

def cubic_spline_eval(coeffs, x_data, x):
    idx = np.searchsorted(x_data, x) - 1
    if idx < 0:
        idx = 0
    if idx > len(x_data) - 2:
        idx = len(x_data) - 2
    h = x - x_data[idx]
    return coeffs[0][idx] + coeffs[1][idx] * h + coeffs[2][idx] * h**2 / 2 + coeffs[3][idx] * h**3 / 6

x_data = np.array([40, 48, 56, 64, 72, 80])
y_data = np.array([1.36, 1.67, 2.12, 2.36, 2.72, 3.19])

coeffs = cubic_spline_coeffs(x_data, y_data)
x_target = 75
y_target = cubic_spline_eval(coeffs, x_data, x_target)

print("온도가 75일 때 기전력 값:", y_target)
