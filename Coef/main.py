import matplotlib.pyplot as plt
import numpy as np

E = np.array([59.5, 511, 632, 1173, 1332]) #keV
miu = np.array([0.165, 0, 0, 0, 0])

plt.scatter(E, miu, color="red", label="puncte experimentale")

# coeffs = np.polyfit(E, miu, 1)
# x_fit = np.linspace(min(E), max(miu), 3000)
# y_fit = coeffs[0] * x_fit + coeffs[1]

# plt.plot(x_fit, y_fit, color="black")

plt.title("Coeficientul de atenuare în funcție de energie")
plt.xlabel(r"E (keV)")
plt.ylabel(r"μ (cm⁻¹)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_axisbelow(True)

plt.savefig("Graph.png", dpi=300)

