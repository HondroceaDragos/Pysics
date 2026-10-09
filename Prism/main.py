import numpy as np
from rich.console import Console

from plotting import Plotter
from filtering import Filter

console = Console()

dataSetMercury = Filter(
    name="Mercury",
    waveLgth=np.array(
        [
            623.4,
            612.3,
            607.3,
            589.0,
            585.9,
            579.0,
            577.0,
            546.1,
            538.5,
            535.4,
            496.0,
            491.6,
            435.8,
            407.8,
            404.7,
        ]
    ),
    divs=np.array(
        [
            295.83,
            296.0,
            296.21,
            296.33,
            296.36,
            296.58,
            296.61,
            296.91,
            297.0,
            297.41,
            297.55,
            297.63,
            298.71,
            299.55,
            299.61,
        ]
    ),
)

dataSetMercury.print(console)

Plotter.scatterExpPts(dataSetMercury.divs, dataSetMercury.waveLgth)
Plotter.plotExpPts(
    dataSetMercury.divs,
    dataSetMercury.waveLgth,
    title="Etalonare Hg",
    xLabel="x (div)",
    yLabel="λ (nm)",
    imgName="Eta_Hg",
)

dataSetHelium = Filter(
    name="Helium",
    waveLgth=None,
    divs=np.array([295.75, 296.0, 296.53, 297.5, 297.61, 297.93, 298.46]),
)

m, b = Plotter.getCoeffs(dataSetMercury.divs, dataSetMercury.waveLgth, 1)
dataSetHelium.waveLgth = np.array([m * x + b for x in dataSetHelium.divs])
dataSetHelium.print(console)

Plotter.reset()
Plotter.scatterExpPts(dataSetHelium.divs, dataSetHelium.waveLgth)
Plotter.plotExpPts(
    dataSetHelium.divs,
    dataSetHelium.waveLgth,
    title="Lampa He",
    xLabel="x (div)",
    yLabel="λ (nm)",
    imgName="Diag_He",
)

tgPts = {
    420: [(407.8, 299.55), (435.8, 298.71)],
    500: [(491.6, 297.63), (496.0, 297.55)],
    580: [(579.0, 296.58), (585.9, 296.36)],
}

slopes = np.array([(x2 - x1) / (l2 - l1) for (l1, x1), (l2, x2) in tgPts.values()])
slopes = np.abs(slopes)
print("\t Slopes")
console.print(
    "\n".join(
        f"[[bold green]m_{idx + 1}[/bold green]]: [cyan]{s}[/cyan]"
        for idx, s in zip(range(0, len(slopes)), slopes)
    )
    + "\n"
)

avgSlope = np.mean(slopes)
relSlope = 1 / np.abs(m)
console.print(f"Average slope: [yellow]{avgSlope}[/yellow] (div / nm)")
console.print(f"Linear approx. slope: [yellow]{relSlope}[/yellow] (div / nm)")

err = (avgSlope - relSlope) / relSlope
console.print(f"Relative error: [bold red]{(100 * err):.2f}%[/bold red]")
