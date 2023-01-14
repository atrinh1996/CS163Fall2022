#
# proj.py 
# runs vertical line sweep to report line segment intersection 
# on random set of segments. 
#
# NUM_SEG is the number of line segments in the problem
#
# Amy Bui
# CS163 Fall 2022
import sys 
import argparse
import random
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation
from LineSegmentIntersection import LineSegmentIntersection
from Point import Point 

# Determine if we are running to animate steps 
# rtype = sys.argv[1]
# dataset = sys.argv[2]
# print(f'Running Line Segment Intersection Algorithm: {rtype}, {dataset}')
parser = argparse.ArgumentParser(description="Line Segment Intersection Program", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("visual", choices=['animate', 'static'], help="type of visualization")
parser.add_argument("dataset", choices=['predefined', 'random'], help="type of data")

args = parser.parse_args()
config = vars(args)
# print(config['visual'])

# creata a figure containing single axes 
fig, ax = plt.subplots() 


# empty segment list
seg_list = []
NUM_SEG = 0

if (config['dataset'] == "predefined"):
    NUM_SEG = 5
    seg_list = [
        ((1, 1), (8, 9)),
        ((1, 3), (9, 6)),
        ((1, 5), (9, 7)),
        ((1, 6), (9, 2)),
        ((2, 9), (9, 1))
    ]
elif (config['dataset'] == "random"):
    NUM_SEG = 10
    # create random segments, equal likely hood over all values in interval
    for i in range(NUM_SEG):
        p1 = (random.uniform(0, 10), random.uniform(0, 10))
        p2 = (random.uniform(0, 10), random.uniform(0, 10))
        seg_list.append((p1, p2))

lsi = LineSegmentIntersection() 
lsi.initializeDataStructures(seg_list)


# set up initial frame
# 
# TODO: Initialize first vertical line? 
# All vertical sweep line should be the line x=<current stopping point>
def animation_init():
    for segment in seg_list:
        p1, p2 = segment

        # insert segment (solid black line)
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-')

        # insert endpoints (solid black point)
        # ax.plot(p1[0], p1[1], 'k.')
        # ax.plot(p2[0], p2[1], 'k.')

    # ax.axvline(x = pt_list[0][0], color = 'b', label = 'axvline - full height')

# tmp animation function. colors endpoints.
# 
#
def animation_update(frame):
    ## This code colors endpoints
    # i = frame % NUM_SEG
    # p1, p2 = seg_list[i]
    # ax.plot(p1[0], p1[1], 'r.')
    # ax.plot(p2[0], p2[1], 'b.')

    ## This code pops the recent plot
    # if (frame < NUM_SEG + 1): 
    #     ax.lines.pop()

    ## This code adds a new vertical line, then pops each off in a cycle
    # i = frame % (2 * NUM_SEG)
    # if (i < NUM_SEG): 
    #     ax.axvline(x = i, color = 'b', label = 'axvline - full height')
    # else:
    #     ax.lines.pop()

    ## this code removes previous vertical and inserts a vertical at an endpoint. 
    # i = (frame + 1) % (2 * NUM_SEG)
    # ax.lines.pop()
    # ax.axvline(x = pt_list[i][0], color = 'b', label = 'axvline - full height')

    ## This code gets the next min x point, and displays a vertical line there.
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
    animation = FuncAnimation(fig, func=animation_update, init_func=animation_init, interval=100)
# display only the final results of computed intersections. "static"
# else: 
#     intersections = lsi.computeIntersections()
#     for point in intersections:
#         ax.plot(point.x , point.y, 'r.', markersize=15, markeredgecolor='k')

# display plot
plt.show()