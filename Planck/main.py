import matplotlib.pyplot as plt
import numpy as np

from filtering import Filter, c
from plotting import Plotter

e = 1.6e-19 # C
 
filters = np.array([
    Filter(578, np.array([0.60, 0.59, 0.61, 0.64, 0.59, 0.59, 0.65, 0.64, 0.63, 0.62]), tag="Yellow"),
    Filter(546, np.array([0.72, 0.73, 0.72, 0.73, 0.73, 0.79, 0.77, 0.75, 0.74, 0.77]), tag="Green"),
    Filter(436, np.array([1.06, 1.10, 1.08, 1.06, 1.13, 1.14, 1.07, 1.09, 1.11, 1.13]), tag="Blue"),
    Filter(405, np.array([1.09, 1.11, 1.20, 1.17, 1.10, 1.17, 1.14, 1.18, 1.12, 1.15]), tag="Violet"),
    # Filter(366, np.array([1.09, 1.04, 1.13, 1.28, 1.23, 1.16, 1.13, 1.09, 1.17, 1.16]), tag="Ultraviolet")
])

nu = np.array([f.freq * 1e14 for f in filters])
U = np.array([f.mean for f in filters])

print("\nList of frequencies (× 10¹⁴ Hz):")
print("\n".join(f"{f.tag}: {f.freq}" for f in filters) + "\n")

Plotter.scatterExpPts(nu, U)
Plotter.plotExpPts(nu,
                   U,
                   title="Tensiune în funcție de frecvență",
                   xLabel="ν (× 10¹⁴ Hz)",
                   yLabel="U (V)")

coeffs = Plotter.getCoeffs(nu, U, 1)
h = coeffs[0] * e

print("Planck's constant (m² × kg / s):")
print(f"h = {h}\n")

print("x-intercept (× 10¹⁴ Hz):")
print("\n".join(f"{x / 1e14}" for x in Plotter.getRealRoots(coeffs)) + "\n")

print("Target Wavelength (nm):")
print("\n".join(f"{c / x * 1e9}" for x in Plotter.getRealRoots(coeffs)) + "\n")

print("Extraction Work:")
print("\n".join(f"{x * h}" for x in Plotter.getRealRoots(coeffs)) + "\n")
