"""
Rock physics data screening: 2D probability density function (PDF)
==================================================================
"""

# %%


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.size']=14
plt.rcParams['font.family']='arial'
plt.rcParams['axes.labelpad'] = 10.0


# %%


# import the module 
from rockphypy import QI




# %%
# When data points cluster or overlap, it can be challenging to visualize their distribution. To address this issue, we can estimate the probability density function (PDF) of the data using kernel density estimation, which can enhance the visual clarity of the data. In "QI", the built-in method for performing KDE is KDE diffusion.
#

# %%


# parameters 
Dqz, Kqz, Gqz = 2.65, 36.6, 45 ## grain density, bulk and shear modulus 
Dsh, Ksh, Gsh = 2.7, 21, 7 # shale/clay density, bulk and shear modulus
Dc,Kc, Gc =2.65, 36.6, 45 # cement density, bulk and shear modulus
Db, Kb = 1, 2.2 # brine density, bulk modulus
Do, Ko = 0.8, 1.5 # oil density, bulk modulus
Dg, Kg = 0.2, 0.06 # gas density, bulk modulus
phi_c=0.4 # critical porosity
sigma=20 # effective pressure 
scheme=2
Cn=8.6
# could be array
vsh=0 # shale volume
#phib_p=[0.3,0.36,0.38,0.39] # define cement porosity for Vp
phib_p=0.3
f= 0.5 # slip factor 



# %%
# Applied to field data 
# ^^^^^^^^^^^^^^^^^^^^^
# Let's import the same synthetic well log data and apply the rock physics screening to the well log data 
# 

# %%

# read data
data = pd.read_csv('../../data/well/sandstone.csv',index_col=0)

# compute the elastic bounds
phi,vp1,vp2,vp3,vs1,vs2,vs3 = QI.screening(Dqz,Kqz,Gqz,Dsh,Ksh,Gsh,Dc,Kc,Gc,Db,Kb,phib_p,phi_c,sigma,vsh,scheme,f, Cn)

# create an object with data 
qi= QI(data.VP,phi=data.PHIT_ND,Vsh= data.VSH_GR)

# call the screening plot method 
fig= qi.kde_plot(phi,vp1,vp2,vp3)

plt.ylim([1900,6100])
plt.ylabel('Vp (Km/s)')
plt.yticks(np.arange(2000,6200, 1000),[2,3,4,5,6])

#%%
# As shown by the figure, using a 2D PDF can provide a clearer visualization of the data distribution compared to a normal scatter plot.

# %%
# **Reference** 
# - Avseth, P., Lehocki, I., Kjøsnes, Ø., & Sandstad, O. (2021). Data‐driven rock physics analysis of North Sea tertiary reservoir sands. Geophysical Prospecting, 69(3), 608-621.
# - Kernel density estimation via diffusion in 1d and 2d: https://kde-diffusion.readthedocs.io/en/stable/
# 