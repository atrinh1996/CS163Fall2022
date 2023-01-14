#
# proj.py 
# runs vertical line sweep to report line segment intersection 
# on random set of segments. 
#
# Amy Bui
# CS163 Fall 2022
#
import sys 
import argparse
import random
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
from LineSegmentIntersection import LineSegmentIntersection
from Point import Point 

# Set command line arguments
parser = argparse.ArgumentParser(description="Line Segment Intersection Program", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("visual", choices=['animate', 'static'], help="type of visualization")
parser.add_argument("dataset", choices=['predefined', 'random'], help="type of data")

args = parser.parse_args()
config = vars(args)


# creata a figure containing single axes 
fig, ax = plt.subplots() 



# empty segment list
seg_list = []
NUM_SEG = 0

# set PREDEFINED points here
if (config['dataset'] == "predefined"):
    NUM_SEG = 5
    seg_list = [
        ((1, 1), (8, 9)),
        ((1, 3), (9, 6)),
        ((1, 5), (9, 7)),
        ((1, 6), (9, 2)),
        ((2, 9), (9, 1))
    ]
# RANDOM points generating
elif (config['dataset'] == "random"):
    NUM_SEG = 100
    # create random segments, equal likely hood over all values in interval
    for i in range(NUM_SEG):
        p1 = (random.uniform(0, 10), random.uniform(0, 10))
        p2 = (random.uniform(0, 10), random.uniform(0, 10))
        seg_list.append((p1, p2))

# initialize Line sweep
lsi = LineSegmentIntersection() 
lsi.initializeDataStructures(seg_list)


# set up initial frame
def animation_init():
    for segment in seg_list:
        p1, p2 = segment
        # insert segment (solid black line)
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-')

# updates animation frame for every event point
def animation_update(frame):
    point = lsi.nextEvent()
    if (frame != 0 and point): 
         ax.lines.pop()

    if (point): 
        ptype = None
        if (point.ptype == 0 or point.ptype  == 1): # left/right
            ptype = 'w.'
        else:       # intersection
            ptype = 'r.'

        ax.plot(point.x , point.y, ptype, markersize=15, markeredgecolor='k')
        ax.axvline(x = point.x , color = 'b', label = 'axvline - full height')

    return ax

# run animation - pick a slow interval to see the stops
if (config['visual'] == "animate"):
    animation = FuncAnimation(fig, func=animation_update, init_func=animation_init, interval=500)
# display only the final results of computed intersections. "static"
else: 
    # plot original segments
    animation_init()
    intersections = lsi.computeIntersections()
    # plot only intersection points
    for point in intersections:
        ax.plot(point.x , point.y, 'r.', markersize=15, markeredgecolor='k')

# display plot
plt.show()