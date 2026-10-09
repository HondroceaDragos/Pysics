import numpy as np
import matplotlib.pyplot as plt

n = np.array([0, 0.5, 1, 1.5])
pts = np.array([12430, 11273, 10541, 9663])

plt.scatter(n, pts, color="red", label="Puncte experimentale")

plt.plot(n, pts, color="black")
plt.title("Impulsuri cesiu")
plt.xlabel("n")
plt.ylabel("Imp")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_axisbelow(True)
plt.savefig("Dist_int.png", dpi=300)

# plt.figure()

area = np.trapezoid(pts, n)
x_fit = np.linspace(n.min(), n.max(), 2000)
coeffs = np.polyfit(n, pts, 1)
y_fit = coeffs[0] * x_fit + coeffs[1]

plt.plot(x_fit, y_fit, color="blue")
plt.title("Impulsuri cesiu")
plt.xlabel("n")
plt.ylabel("Imp")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_axisbelow(True)
plt.savefig("Dist_int.png", dpi=300)

# b = 0.165

print(f"Area = {area}\n")
print(f"n_on = {coeffs[0]}, n_off = {coeffs[1]}")

I = area / (coeffs[1] - coeffs[0])
print(f"I = {I}")


