import seaborn as sns  
from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2, venn2_circles
sns.set(style="ticks")    

sns.set_context("poster")

plt.figure(figsize=(4,4))
v = venn2(subsets=(1, 2, 3), set_labels = (' ', ' ',' ') )

v.get_patch_by_id('A').set_color('white')
v.get_patch_by_id('B').set_color('white')
v.get_patch_by_id('C').set_color('white')

v = venn2_circles(subsets=(1, 2, 3), linestyle='-')
v[0].set_lw(3.0)
v[1].set_lw(3.0)
v[0].set_edgecolor('#C4573C')
v[1].set_edgecolor('#6BA25E')

plt.show()
