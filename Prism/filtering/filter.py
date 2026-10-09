import numpy as np
from rich.console import Console


class Filter:
    def __init__(
        self, name: str = "", waveLgth: np.array = None, divs: np.array = None
    ):
        self.name = name
        self.waveLgth = waveLgth
        self.divs = divs

    def print(self, console: Console = None):
        console.print(f"\t{self.name}")
        console.print("\t[bold green]λ[/bold green] : [bold cyan]x[/bold cyan]")
        console.print(
            "\n".join(
                f"[[green]{l:.2f}[/green]]: {d}"
                for l, d in zip(self.waveLgth, self.divs)
            )
            + "\n"
        )
