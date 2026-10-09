import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from scipy.signal import find_peaks

x = np.linspace(-20, 20, 41) / 1000 # m
I = np.array([0, 0, 0, 0, 0, 0, 0, 0.001, 0.001, 0.002, 0.002, 0.002, 0.002, 0, 0.003, 0.008, 0.005, 0.002, 0.026, 0.050, 0.061, 0.058, 0.040, 0.010, 0.002, 0.007, 0.004, 0, 0.001, 0.002, 0.001, 0, 0.001, 0.001, 0, 0, 0, 0, 0, 0, 0])

plt.scatter(x, I, color="red", label="Puncte experimentale")

x_fit = np.linspace(x.min(), x.max(), 2000)
graph = UnivariateSpline(x, I, k=3, s=0)
y_fit = graph(x_fit)

plt.plot(x_fit, y_fit, color="black")
plt.title("Distributia de intensitate")
plt.xlabel("x (m)")
plt.ylabel("I (div)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_axisbelow(True)
plt.savefig("Dist_int.png", dpi=300)

plt.figure()

x0 = x_fit[np.argmax(y_fit)]
min_idx, _ = find_peaks(-y_fit, prominence=1e-4)
minima_x = x_fit[min_idx]

left = minima_x[minima_x < x0][::-1]
right = minima_x[minima_x > x0]

n = min(len(left), len(right))

x_vals = [abs(left[i] - x0) for i in range(n)]

print("\nx₁, x₂, x₃, ...:")
for i, xv in enumerate(x_vals, 1):
    print(f"x{i} = {xv:.6f} m")

print()

plt.scatter(x, I, color="red", label="Puncte experimentale")

min_points_x = np.concatenate([left, right])
min_points_y = graph(min_points_x)

plt.scatter(min_points_x, min_points_y, color="blue", label="Delimitatoare minime")


x_fit = np.linspace(x.min(), x.max(), 2000)
graph = UnivariateSpline(x, I, k=3, s=0)
y_fit = graph(x_fit)

plt.plot(x_fit, y_fit, color="black")
plt.title("Distributia de intensitate")
plt.xlabel("x (m)")
plt.ylabel("I (div)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_axisbelow(True)
plt.savefig("Dist_int_pct.png", dpi=300)

a = 0.24 / 1000
L = 190 / 100

n = np.array([1, 2, 3, 4])

plt.figure()
plt.scatter(n, x_vals, color="red", label="Puncte experimentale")

x_fit = np.linspace(min(n), max(n), 2000)
coeffs = np.polyfit(n, x_vals, 1)
y_fit = coeffs[0] * x_fit + coeffs[1]

print("Line eq: ")
print(f"{coeffs[0]} * x + {coeffs[1]}")

lmbd = (coeffs[0] * a) / L
print(f"Lambda = {lmbd} (m)")

plt.plot(x_fit, y_fit, color="black")
plt.title("x vs n")
plt.xlabel("n")
plt.ylabel("x (m)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_axisbelow(True)
plt.savefig("Det_lmbd.png", dpi=300)

n_exp = []
for x in x_vals:
    n_exp.append((x * a) / (lmbd * L))

print("\nn_exp:")
for i in n_exp:
    print(i)

n_exp = np.array(n_exp)
err = (n_exp - n) / n * 100
print(err)