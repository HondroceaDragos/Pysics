import math
import matplotlib.pyplot as plt
import numpy as np

U = [3.0, 3.5, 4.0, 4.5, 5.0]
U_v = [x * 1000 for x in U]

d1 = 2.13 * (10 ** (-10))
d2 = 1.23 * (10 ** (-10))
L = 0.135

D1 = [2.85, 2.8, 2.55, 2.4, 2.3]
D1_m = [x / 100 for x in D1]
D2 = [5.0, 4.75, 4.4, 4.1, 3.8]
D2_m = [x / 100 for x in D2]

e = 1.602 * (10 ** (-19))
m = 9.109 * (10 ** (-31))
h = 6.625 * (10 ** (-34))

print("V ^ (-1 / 2):")
V = []
for u in U:
    V.append(1 / math.sqrt(u))
    print(1 / math.sqrt(u))

V_volt = []
for u in U_v:
    V_volt.append(1 / math.sqrt(u))

print()

print("lambda_1_exp:")
for idx in D1_m:
    lambda_1 = (10 ** 12) * d1 * idx / (2 * L)
    print(lambda_1)

print("lambda_2_exp:")
for idx in D2_m:
    lambda_2 = (10 ** 12) * d2 * idx / (2 * L)
    print(lambda_2)

print()
print("lambda_th")
for u in U_v:
    lambda_th = (10 ** 12) * h / (math.sqrt(2 * m * e * u))
    print(lambda_th)

plt.plot(V, D1_m, 'o', color="red", label="Puncte experimentale - d1")
a, b = np.polyfit(V, D1_m, 1)
V = np.array(V)
line = a * V + b
plt.plot(V, line, color="red")

plt.title("Dispersia diametrelor interioare (d1)")
plt.xlabel(r"$V = 1 / \sqrt{U}$ (kV$^{-1/2}$)")
plt.ylabel(r"$d$ (m)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_axisbelow(True)

plt.savefig("Diam1_Graph.png", dpi=300)

print()
a, b = np.polyfit(V_volt, D1_m, 1)
print(f"Ecuatia aproximării: D1 = {a:.4f} * (1/√U) + {b:.4f}")
d1_exp = (2 * h * L) / (a * math.sqrt(2 * m * e))
err = (d1_exp - d1) / d1
print(f"d1_exp = {d1_exp}")
print(f"err = {err * 100}%")
print(f"panta = {a}")

# plt.figure()

plt.plot(V, D2_m, 'o', color="blue", label="Puncte experimentale - d2")
a, b = np.polyfit(V, D2_m, 1)
line = a * V + b
plt.plot(V, line, color="blue")

plt.title("Dispersia diametrelor")
plt.xlabel(r"$V = 1 / \sqrt{U}$ (kV$^{-1/2}$)")
plt.ylabel(r"$d$ (m)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_axisbelow(True)

plt.savefig("Suprapuse.png", dpi=300)

print()
a, b = np.polyfit(V_volt, D2_m, 1)
print(f"Ecuatia aproximării: D2 = {a:.4f} * (1/√U) + {b:.4f}")
d2_exp = (2 * h * L) / (a * math.sqrt(2 * m * e))
err = (d2_exp - d2) / d2
print(f"d1_exp = {d2_exp}")
print(f"err = {err * 100}%")
print(f"panta = {a}")
