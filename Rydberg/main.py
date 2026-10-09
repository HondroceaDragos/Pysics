import matplotlib.pyplot as plt
import numpy as np
import math as mt

lambda_Hg = [623.4, 612.3, 579.0, 577.0, 546.1, 535.4, 435.8, 434.7, 433.9, 407.8, 404.7]
x_Hg = [19.1, 20.2, 23.2, 23.25, 25.5, 26.4, 39.5, 40.45, 40.5, 44.4, 45.3]
x_H = [16.9, 31.6, 40.4, 44.3, 46.2, 57.1]

x = np.array(x_Hg)
y_org = np.array(lambda_Hg)
y = np.array(lambda_Hg)

y = 1 / (y_org ** 2)

coeffs = np.polyfit(x, y, 1)
poly = np.poly1d(coeffs)

x_fit = np.linspace(min(x), max(x), 300)
y_fit = np.sqrt(1 / (coeffs[0] * x_fit + coeffs[1]))

plt.scatter(x, y_org, color="red", label="Puncte experimentale")

plt.plot(x_fit, y_fit, color="black")

plt.title("Etalonarea λ (Hg)")
plt.xlabel(r"$x$ (mm)")
plt.ylabel(r"$\lambda$ (nm)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_axisbelow(True)
plt.legend()

plt.savefig("EtaHg_Graph.png", dpi=300)
# plt.show()

print("Ecuatia aproximată (1/λ² = A·x + B) pt Hg:")
print(f"A = {coeffs[0]}")
print(f"B = {coeffs[1]}")

lambda_H = []
for x in x_H:
    lambda_H.append(mt.sqrt(1 / (coeffs[0] * x + coeffs[1])))

print()
print(f"λ_H (nm):")
for h in lambda_H:
    print(f"{h:.5f}")

plt.figure()

x = np.array(x_H)
y_org = np.array(lambda_H)
y = np.array(lambda_H)

y = 1 / (y_org ** 2)

coeffs = np.polyfit(x, y, 1)
poly = np.poly1d(coeffs)

x_fit = np.linspace(min(x), max(x), 300)
y_fit = np.sqrt(1 / (coeffs[0] * x_fit + coeffs[1]))

plt.scatter(x, y_org, color="red", label="Puncte experimentale")

plt.plot(x_fit, y_fit, color="black")

plt.title("Etalonarea λ (H)")
plt.xlabel(r"$x$ (mm)")
plt.ylabel(r"$\lambda$ (nm)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_axisbelow(True)
plt.legend()

plt.savefig("EtaH_Graph.png", dpi=300)

print()
print("Ecuatia aproximată (1/λ² = A·x + B) pt H:")
print(f"A = {coeffs[0]}")
print(f"B = {coeffs[1]}")

print()

E1 = 13.6 * (1.602176634 * (10 ** (-19)))
h = 6.62607015 * (10 ** (-34)) # Js
c = 2.99792458 * (10 ** 8) # m/s

R_H_th = E1 / (h * c)
print(f"R_H_th (× 10⁷ m⁻¹):")
print(R_H_th / (10 ** 7))
print()

R_H = []
n = 3
for l in lambda_H[:-1]:
    R_H.append((1 / l) * ((4 * (n ** 2)) / ((n ** 2) - 4)) * 100)
    n += 1

R_H.append(4 / lambda_H[5] * 100)

print(f"R_H (× 10⁷ m⁻¹):")
for r in R_H:
    print(f"{r:.5f}")

print()
print(f"<R_H> (× 10⁷ m⁻¹):")
R_H_med = sum(R_H) / len(R_H)
print(R_H_med)

R_real = 1.09678

print()
print(f"err")
print(f"{(R_H_med - R_real) / R_real * 100}%")

eps = mt.sqrt(sum((r - R_H_med) ** 2 for r in R_H) / 30)
print()
print(f"eps (× 10⁷ m⁻¹):")
print(eps)

print()
print(f"Precision:")
print(f"{eps / R_H_med * 100}%")

print()
print(f"Final estimation:")
print(f"R_H = ({R_H_med:.4f} ± {eps:.4f}) × 10⁷ m⁻¹")

