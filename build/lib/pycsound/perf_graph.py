import matplotlib.pyplot as plt

# [] implementare plotting di una score compilata
# [] implementare plotting di una score caricata da un file esterno
# [] implementare la possibilita di scegliere quale valore plottare

class PlotPerformance:
    def __init__(self, database: dict) -> None:
        self.database = database
    
    def time_instr(self):
        for instr in self.database:
            for params in self.database[instr]:
                start, end = params[0], params[0] + params[1]
                plt.hlines(y=instr, xmin=start, xmax=end)
                plt.scatter(x=start, y=instr, c="k", linewidth=2.1, zorder=2)
                plt.scatter(x=end, y=instr, c="b", linewidth=0.1, zorder=2)
        plt.show()