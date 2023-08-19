# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:09:51 2023

@author: ffaraj
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




Data = pd.read_csv('CuMineBH.csv')

Vars = pd.read_csv('VariogramDirection.csv')

#%% all directions

plt.rcParams["font.size"] = 13
plt.rcParams["font.family"] = "arial"

plt.rcParams.update({'mathtext.default':  'regular' ,"ytick.color" : "k",
          "xtick.color" : "k",
          "axes.labelcolor" : "k",
          "axes.edgecolor" : "k"})

plt.close()
fig, ax = plt.subplots()
fign='Response'


plt.plot([0,200],[1,1],color='k',lw=3)
plt.plot(Vars['lag 000'],Vars['semivar 000']-0.03,marker='o',color='C0',markeredgecolor='k',label='000')
plt.plot(Vars['lag 090'],Vars['semivar 090']+0.03,marker='s',color='C0',markeredgecolor='k',label='090')


plt.plot(Vars['lag 015'],Vars['semivar 015'],marker='o',color='C1',alpha=0.5,label='015')
plt.plot(Vars['lag 105'],Vars['semivar 105'],marker='s',color='C1',alpha=0.5,label='105')


plt.plot(Vars['lag 030'],Vars['semivar 030'],marker='o',color='C2',alpha=0.5,label='030')
plt.plot(Vars['lag 120'],Vars['semivar 120'],marker='s',color='C2',alpha=0.5,label='120')


plt.plot(Vars['lag 045'],Vars['semivar 045'],marker='o',color='C3',alpha=0.5,label='45')
plt.plot(Vars['lag 135'],Vars['semivar 135'],marker='s',color='C3',alpha=0.5,label='135')

plt.plot(Vars['lag 060'],Vars['semivar 060'],marker='o',color='C4',alpha=0.5,label='060')
plt.plot(Vars['lag 150'],Vars['semivar 150'],marker='s',color='C4',alpha=0.5,label='150')

plt.plot(Vars['lag 075'],Vars['semivar 075'],marker='o',color='C5',alpha=0.5,label='075')
plt.plot(Vars['lag 165'],Vars['semivar 165'],marker='s',color='C5',alpha=0.5,label='165')



plt.legend(fancybox=False,edgecolor='k',ncol=6,loc='lower center',facecolor='w',framealpha=1)

plt.xlabel('Lag distance [m]')
plt.ylabel('Semivariogram')
plt.xlim(0,200)
plt.ylim(0,1.3)

ax.grid(axis='both',which='major',alpha=0.75,zorder=0)
ax.grid(which='minor',alpha=0.5,ls='--')


ax.set_axisbelow(True)
ax.tick_params(axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=1)
ax.tick_params(which='minor',axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=1)



ax.spines['right'].set_linewidth(1)
ax.spines['top'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)

plt.savefig(fign, bbox_inches='tight', dpi=300,transparent=True)


#%% variogram modeling

plt.rcParams["font.size"] = 13
plt.rcParams["font.family"] = "arial"

plt.rcParams.update({'mathtext.default':  'regular' ,"ytick.color" : "k",
          "xtick.color" : "k",
          "axes.labelcolor" : "k",
          "axes.edgecolor" : "k"})

plt.close()
fig, ax = plt.subplots()
fign='Response'


plt.plot([0,200],[1,1],color='k',lw=3)



x = np.linspace(0,300)
R1 = 30
R2 = 60
N=0.15
S = 1-N
SphCu1 = N+ (S*(3/2 * x/R1 - 0.5*(x**3 / R1**3)))*(x<=R1) + S*(x>R1)
SphCu2 = N+ (S*(3/2 * x/R2 - 0.5*(x**3 / R2**3)))*(x<=R2) + S*(x>R2)

ExpCu1 = N+ (S*(1 - np.exp(-x/R1)))
ExpCu2 = N+ (S*(1 - np.exp(-x/R2)))


plt.plot(x,ExpCu1,c='#48A2E0',lw=3.5)
plt.plot(x,ExpCu2,c='#1C6DA4',lw=3.5)
plt.scatter(Vars['lag 000'],Vars['semivar 000']-0.03,marker='o',color='#1C6DA4',edgecolor='k',zorder=100,lw=0.5,s=75)
plt.scatter(Vars['lag 090'],Vars['semivar 090']+0.03,marker='s',color='#48A2E0',edgecolor='k',zorder=100,lw=0.5,s=75)



plt.xlabel('Lag distance [m]')
plt.ylabel('Semivariogram')
plt.xlim(0,200)
plt.ylim(0,1.3)


ax.grid(axis='both',which='major',alpha=0.75,zorder=0)
ax.grid(which='minor',alpha=0.5,ls='--')


ax.set_axisbelow(True)
ax.tick_params(axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=1)
ax.tick_params(which='minor',axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=1)



ax.spines['right'].set_linewidth(1)
ax.spines['top'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)

plt.savefig(fign, bbox_inches='tight', dpi=300,transparent=True)





#%% 2d map
plt.rcParams["font.size"] = 13
plt.rcParams["font.family"] = "arial"

plt.rcParams.update({'mathtext.default':  'regular' ,"ytick.color" : "k",
          "xtick.color" : "k",
          "axes.labelcolor" : "k",
          "axes.edgecolor" : "k"})

plt.close()
fig, ax = plt.subplots()
fign='Response'


plt.scatter(Data['EAST'],Data['NORTH'],c=Data['Cu'],edgecolor='k',lw=0.5,cmap='jet')
plt.clim(0.1,0.8)


cbar =plt.colorbar(orientation='horizontal',aspect=40)
cbar.set_label('Copper grade [wt%]')
cbar.outline.set_linewidth(1)
cbar.ax.tick_params(which='both',direction='in',width=1) 


plt.yticks([0,100,200])
plt.gca().set_aspect('equal', adjustable='box')

plt.yticks(rotation = 90,va='center')
plt.xlabel('Easting [m]')
plt.ylabel('Northing [m]')

# plt.xticks([])
# plt.yticks([])
ax.grid(axis='both',which='major',alpha=0.75,zorder=0)
ax.grid(which='minor',alpha=0.5,ls='--')


ax.set_axisbelow(True)
ax.tick_params(axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=1)
ax.tick_params(which='minor',axis="both",direction="in",bottom=True, top=True, left=True, right=True,width=1)

ax.set_aspect('equal', adjustable='box')


ax.spines['right'].set_linewidth(1)
ax.spines['top'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)

plt.savefig(fign, bbox_inches='tight', dpi=300,transparent=True)

