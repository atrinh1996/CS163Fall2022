import random
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation

# creata a figure containing single axes 
fig, ax = plt.subplots() 
# fig2, ax2 = plt.subplots() 

# plot some data on an axis 
# ax.plot([1,2,3,4], [1,4,2,3])

# empty segment list
segList = []
MAX_SEG = 10

# create some random segments
for i in range(MAX_SEG):
    endpoint1 = (random.uniform(0,10),random.uniform(0,10))
    endpoint2 = (random.uniform(0,10),random.uniform(0,10))
    segList.append( (endpoint1,endpoint2) )

# plot original segments
# for seg in segList:
#     vs,ve = seg
#     # plt.plot([vs[0],ve[0]],[vs[1],ve[1]],'k:')
#     ax.plot([vs[0],ve[0]],[vs[1],ve[1]],'k-')

def animation_init():
    for seg in segList:
        vs,ve = seg
        # plt.plot([vs[0],ve[0]],[vs[1],ve[1]],'k:')
        ax.plot([vs[0],ve[0]],[vs[1],ve[1]],'k-')


def animation_update(frame):
    i = frame % MAX_SEG
    vs,ve = segList[i]
    # ax.plot([vs[0],ve[0]],[vs[1],ve[1]],'k-')
    ax.plot(vs[0],vs[1],'r.')
    ax.plot(ve[0],ve[1],'b.')
    return ax

animation = FuncAnimation(fig, func=animation_update, init_func=animation_init, interval=400)



# pyplot display 
plt.show()