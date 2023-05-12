"""
Cement volume estimation 
========================
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
# The rock physics diagnostic elastic bounds can be used to infer the microstructure from velocity-porosity data (Avseth et al. 2010). By locally validating the constant cement model and other diagnostic models such as friable sand model and contact cement model, we can obtain a quantitative measure of the degree of cement volume from the resulting diagnostic crossplots.
# ``QI`` module provides convinient method to perform the cement estimation given data.The following code snippets show the cement volume estimation for synthetic sandstone data. 
#
# Notice that, this method is not strictly valid for cement volume estimation for heavily cemeneted sandstone. The constant cement model has its valid range just like any other models. awareness of the model limitation is necessary when applying the approach in pratice. 
#

# %%


# parameters
Dqz, Kqz, Gqz = 2.65, 36.6, 45 ## grain density, bulk and shear modulus
Dsh, Ksh, Gsh = 2.7, 21, 7 # shale/clay density, bulk and shear modulus
Dc,Kc, Gc =2.65, 36.6, 45 # cement density, bulk and shear modulus
Db, Kb = 1, 2.2 # brine density, bulk modulus
phi_c=0.4 # critical porosity
sigma=20 # effective pressure
scheme=2
Cn=8.6
vsh=0 # shale volume
# define cement porosity for Vp
phib=0.3
f= 0.5 # slip factor


# %%
# Applied to field data 
# ^^^^^^^^^^^^^^^^^^^^^
# Let's import the same synthetic well log data and apply the cement volum estimation using constant cement model  to the well log data 
# 

# %%

# read data
data = pd.read_csv('../../data/well/sandstone.csv',index_col=0)


# estimate cement: 
vcem_seeds=np.array([0,0.005,0.01,0.02,0.03,0.04,0.1] )
phib_p=[0.3,0.37,0.38,0.39,0.395] # define cement porosity for Vp

# compute the elastic bounds
phi,vp1,vp2,vp3,vs1,vs2,vs3 = QI.screening(Dqz,Kqz,Gqz,Dsh,Ksh,Gsh,Dc,Kc,Gc,Db,Kb,phib,phi_c,sigma,vsh,scheme,f, Cn)



# create an object with data 
qi= QI(data.VP,phi=data.PHIT_ND,Vsh= data.VSH_GR)

# estimate the cement volume for data
vcem= qi.estimate_cem(vcem_seeds,Kqz,Gqz,Ksh,Gsh,phi_c,Cn,Kc,Gc,Db,Kb,scheme,vsh,Dsh,Dqz,Dc)


#%%

# color_coding cement volume in the porosity and velocity cross plot. 
fig=qi.cement_diag_plot(vcem,Dqz,Kqz,Gqz,Dsh,Ksh,Gsh,Dc,Kc,Gc,Db,Kb,phib,phib_p,phi_c,sigma,vsh,Cn, scheme,f)
plt.ylim([1900,6100])
plt.ylabel('Vp (Km/s)')
plt.yticks(np.arange(2000,6200, 1000),[2,3,4,5,6])
plt.xlim(-0.01,0.51)



#%%
# As shown by the figure, using a 2D PDF can provide a clearer visualization of the data distribution compared to a normal scatter plot.
#

# %%
# **Reference** 
# - Avseth, P.; Mukerji, T.; Mavko, G. & Dvorkin, J. Rock-physics diagnostics of depositional texture, diagenetic alterations, and reservoir heterogeneity in high-porosity siliciclastic sediments and rocks—A review of selected models and suggested work flows  Geophysics, Society of Exploration Geophysicists, 2010, 75, 75A31-75A47
# 