import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    @staticmethod
    def _getAxis(xArr: np.array, yArr: np.array):
        x = np.array([x for x in xArr])
        y = np.array([y for y in yArr])

        return x, y
    
    @staticmethod
    def _fitPoly(x: np.array, y: np.array, deg: int):
        coeffs = np.polyfit(x, y, deg)
        function = np.poly1d(coeffs)
        return function, coeffs
    
    @staticmethod
    def getCoeffs(x: np.array, y: np.array, deg: int):
        return np.polyfit(x, y, 1)
    
    @staticmethod
    def getRealRoots(coeffs):
        roots = np.roots(coeffs)
        x_intercepts = roots[np.isreal(roots)].real

        return x_intercepts

    @staticmethod
    def scatterExpPts(xArr: np.array,
                      yArr: np.array,
                      color: str="red",
                      label: str="Puncte experimentale") -> None:
        x, y = Plotter._getAxis(xArr, yArr)
        plt.scatter(x, y, color=color, label=label)

    @staticmethod
    def plotExpPts(xArr: np.array,
                   yArr: np.array,
                   deg: int = 1,
                   color: str="black",
                   title: str="Experiment",
                   xLabel: str="x",
                   yLabel: str="y",
                   imgName: str="Diag.png"
                   ) -> None:
        x, y = Plotter._getAxis(xArr, yArr)
        function, coeffs = Plotter._fitPoly(x, y, deg)

        x_fit = np.linspace(min(x), max(x), 3000)
        y_fit = function(x_fit)

        plt.plot(x_fit, y_fit, color=color)

        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.gca().set_axisbelow(True)
        plt.legend()

        plt.savefig(imgName, dpi=300)

        print(f"List of coefficients:")
        coeffs = coeffs[::-1]
        print("\n".join(f"[x^{idx}]: {coeffs[idx]}" for idx in range(len(coeffs))) + "\n")
