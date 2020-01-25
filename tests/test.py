import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from CITIfile import read_citifile


mpl.rcParams.update(mpl.rcParamsDefault)

res = read_citifile("data.citi")

df = res['aele_0.Sweep2.Sweep1.SP1']["Mu1"].to_dataframe().reset_index()

g = sns.FacetGrid(df, hue="L_load", row="C_d2")
g = g.map(plt.plot, "freq", "Mu1", marker=".")
g.add_legend()
plt.show()
