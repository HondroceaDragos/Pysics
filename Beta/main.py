import math as mt
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

def plotter(x, y, name : str):

    plt.plot(x, y, color="black")

    plt.title("n în funcție de E")
    plt.xlabel("E (keV)")
    plt.ylabel("n (imp / s)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.gca().set_axisbelow(True)
    plt.savefig(name, dpi=300)

    fig = plt.gcf()
    plt.figure()

    return fig

I = [round(i * 0.1, 1) for i in range(0, 18)]
B = [4.4, 15.4, 24.5, 34.7, 45.7, 56.1, 65.8, 78, 87, 97.4, 107.4, 120.2, 128.5, 140, 149, 159.3, 168.1, 174.7]
E = [5.47, 21.56, 47.34, 81.55, 122.83, 169.89, 221.62, 277.11, 335.6, 396.53, 459.43, 523.94, 589.79, 656.74, 724.61, 793.27, 862.58, 932.47]

N = [152, 206, 292, 555, 765, 911, 1128, 1143, 1166, 1138, 1030, 936, 823, 688, 529, 424, 263, 224]

t = 60 # s
n_a = [n / t for n in N]

f = 0.205 # imp / s
n = [x - f for x in n_a]

tf = 600
sgm = [mt.sqrt(x / t + f / tf) for x in n]

plt.scatter(E, n, color="red", label="Puncte experimentale")
plotter(E, n, "Puncte_unite.png")

x = np.array(E)
y = np.array(n)

cs = CubicSpline(x, y)
x_fit = np.linspace(x.min(), x.max(), 300)
y_fit = cs(x_fit)

plt.scatter(x, y, color="red", label="Puncte experimentale")
plotter(x_fit, y_fit, "Puncte_spline.png")

coeffs = np.polyfit(x, y, 3)

x_fit = np.linspace(min(x), max(x), 300)
y_fit = coeffs[0] * (x_fit ** 3) + coeffs[1] * (x_fit ** 2) + coeffs[2] * (x_fit) + coeffs[3]

plt.scatter(x, y, color="red", label="Puncte experimentale")
fig3 = plotter(x_fit, y_fit, "Puncte_inter.png")

print("Values of n' (imp / s):")
for i in n_a:
    print(round(i, 2))

print()

print("Values of n (imp / s):")
for i in n:
    print(round(i, 2))

print()

print("Values of sgm:")
for i in sgm:
    print(round(i, 2))

print()

print("3rd degree interpolation equation: ")
print(f"{coeffs[0]} * x^3 + {coeffs[1]} * x^2 + {coeffs[2]} * x + {coeffs[3]}")

print()

idx = np.argmax(y_fit)
E_h = x_fit[idx]
E_max = 3 * E_h

plt.figure(fig3.number)
y_at_Eh = coeffs[0] * E_h**3 + coeffs[1] * E_h**2 + coeffs[2] * E_h + coeffs[3]
plt.plot([E_h, E_h], [0, y_at_Eh], color='blue')
plt.legend()
plt.savefig("Puncte_inter_linie.png", dpi=300)

print(f"E_h = {E_h} (keV)")
print(f"E_max = {E_max} (kev)")
