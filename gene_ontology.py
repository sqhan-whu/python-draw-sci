### Daivd BP Chart#######

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks")
sns.set_context("poster")

BP_vitro = pd.read_csv('C:/Users/sqhan/Desktop/实验室工作/袁羽书/bp.txt', header=0, sep='\t')
BP_vitro = BP_vitro[BP_vitro['PValue']<0.05]
BP_vitro['-log10(PValue)'] = -np.log10(BP_vitro['PValue'])


fig,ax=plt.subplots(figsize=(20, 6))

sns.barplot(y='Term', x='-log10(PValue)', data=BP_vitro.iloc[0:10,:], color='#8172B2')
plt.tight_layout()
plt.savefig('C:/Users/sqhan/Desktop/实验室工作/袁羽书/bp.pdf')
plt.close()
