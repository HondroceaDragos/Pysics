import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from scipy.optimize import curve_fit

barWidth: float = 0.4
lineWidth: float = 2.5

# ==========================================================
# === 1. POISSON DISTRIBUTION (Experimental + Theoretical) ===
# ==========================================================

# Load experimental data
df = pd.read_csv("data.csv")

# Experimental Poisson Distribution
plt.bar(df['n'] - barWidth / 2, df['k'], width = barWidth, color="red", alpha = 0.9, label = "k_exp")

plt.title("Distribuția Poisson")
plt.xlabel("n")
plt.ylabel("k_exp / k_th")
plt.grid(True)
plt.gca().set_axisbelow(True)

# Compute theoretical Poisson parameters and print them
N = 0
sigma = 0
samples = df.size // 2

for idx in range(samples):
    sigma += df['n'][idx] * df['k'][idx]
    print(f"n = {df['n'][idx]}, k = {df['k'][idx]} => n * k = {df['n'][idx] * df['k'][idx]}")
    N += df['k'][idx]

print(f"N = {N}")
print(f"Sum = {sigma}")

n_aprox = sigma / N

print()
print()

# Compute theoretical Poisson data and print it
th_results = []
for idx in range(samples):
    P_pos = math.e ** (-n_aprox) * (n_aprox ** df['n'][idx]) / math.factorial(df['n'][idx])
    P_gss = (1 / (math.sqrt(2 * math.pi) * math.sqrt(n_aprox))) * math.e ** (-(((df['n'][idx] - n_aprox) ** 2) / (2 * n_aprox)))
    print(f"n = {df['n'][idx]}, k = {df['k'][idx]} => P_pos = {P_pos}")
    print(f"n = {df['n'][idx]}, k = {df['k'][idx]} => P_gss = {P_gss}")
    k_th_pos = math.floor(P_pos * N)
    k_th_gss = math.floor(P_gss * N)
    print(f"n = {df['n'][idx]}, k = {df['k'][idx]} => k_th_pos = {k_th_pos}")
    print(f"n = {df['n'][idx]}, k = {df['k'][idx]} => k_th_gss = {k_th_gss}")
    print()
    th_results.append((df['n'][idx], k_th_pos))

# Save theoretical results
results_df = pd.DataFrame(th_results, columns=["n", "k"])
results_df.to_csv("results.csv", index=False)

# Plot theoretical Poisson Distribution
plt.bar(results_df['n'] + barWidth / 2, results_df['k'], width=barWidth, color="blue", alpha=0.8, label="k_th")

plt.legend(loc="upper left")
plt.savefig("Poisson_Distribution_Graph.png")

# ==========================================================
# === 2. GAUSSIAN DISTRIBUTION (Experimental + Theoretical) ===
# ==========================================================

# Load data again for Gaussian computation
df = pd.read_csv("data.csv")

x = df['n'].values
y = df['k'].values

# Define Gaussian function
def gaussian(x, A, mu, sigma):
    return A * np.exp(-((x - mu)**2) / (2 * sigma**2))

# Fit experimental Gaussian
A_guess = max(df['k'].values)
mu_guess = np.mean(df['n'].values)
sigma_guess = np.std(df['n'].values)
params, _ = curve_fit(gaussian, df['n'].values, df['k'].values, p0=[A_guess, mu_guess, sigma_guess])
A_fit, mu_fit, sigma_fit = params

x_smooth = np.linspace(min(x), max(x), 400)
y_exp_fit = gaussian(x_smooth, A_fit, mu_fit, sigma_fit)

# Theoretical Gaussian (Poisson → Gaussian approximation)
N = y.sum()
mean_th = (x * y).sum() / N
sigma_th = math.sqrt(mean_th)
A_th = max(y)
y_th = A_th * np.exp(-((x_smooth - mean_th)**2) / (2 * sigma_th**2))

# Uncomment this for separate graphs
# plt.figure()

plt.plot(x_smooth, y_exp_fit, color="blue", linewidth=lineWidth, label="k_exp")
plt.plot(x_smooth, y_th, color="red", linewidth=lineWidth, label="k_th")

plt.title("Distribuția Gauss")
plt.xlabel("n")
plt.ylabel("k_th / k_exp")
plt.grid(True)
plt.gca().set_axisbelow(True)
plt.legend(loc="upper left")

plt.savefig("Gaussian_Distribution_Graph.png")
