import matplotlib as mpl 
import matplotlib.pyplot as plt 
import numpy as np 

# Fig. 1: empty figure, no axes 
fig = plt.figure()

# Fig. 2: figure with ingle axes 
fix, ax = plt.subplots()

# Fig. 3: figure with 2x2 grid of Axes 
fig, axs = plt.subplots(2, 2)

# display
plt.show()