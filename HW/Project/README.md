# CS163 Project: Line Segment Intersection in the Primal Using Vertical Sweep Line
## Fall 2022
## Amy Bui

## Summary 
Computes and animates the line segment intersection point of a number of random lines set by the `NUM_SEG` variable in `proj.py`. To run with 5 pre-defined lines for a clear visual demo, run with the below command line options. See Bugs/Notes below.

The algorithm runs O((n + k) log n) time, where k is the number of intersections, so k <= n^2. Preprocess takes O(n log n) time to construct the stopping point data structure (priority queue) and status data structure (AVL tree); insertion and deletion into these each take O(log n). Storege for the status DS is O(n), and the stopping point DS is O(n + k).

## Dependencies 
- python 3.10.6 
- pip 22.0.2
- [matplotlib 3.6.2](https://matplotlib.org/)
    - I couldn't get the animation window to pop up on Halligan. `pip list` shows `matplotlib 3.4.3` was installed. Likely will need to run locally. 

## Run script 
> `python3 proj.py [-h] {animate, static} {random, predefined}`
>
> Example: 
>
> `python3 proj.py animate predefined`
> 
> `python3 proj.py static random`

## Files
- README.md : this file 
- proj.py : main project script 
- Point.py : Point class module 
- Segment.py : Segment class module 
- EventQueue.py : event queue class module 
- AVLTree.py : AVL tree class module
- LineSegmentIntersection.py : main algorithm module
- screenshots.pdf : sample shots of the end of a few test animations, both results that worked and those that didn't.

## Bugs/Notes
- Set predefined points in `proj.py`, but the current 5 segments look nicer on the screen. I don't have a parser to take commandline inputs. 
- Set number of `random` segments in `proj.py`. Currently set to 10.
- Frame rate/speed of animation set in `proj.py` i the `interval` argument of the `FuncAnimation` method at the bottom of the file. 
- I'm not totally sure, but I think if I set the time per frame for the animation (end of `proj.py`) to be too low (fast), the output points might not show up for the frame it is being solved in because the animation package outputs faster than my module. 
- Following the book's algorithm, to switch the order of segments in my status data structure at an intersection event point, I remove the intersecting segments from Status, and re-insert them. This doesn't consistently reverse their order, as intended. My Status is a regular AVL tree, rather than an augmented one where the leaves are the segments, and the internal nodes contain just the key of the rightmost segment node of its left subtree. I couldn't get the augmented tree to update the internal node keys to maintain that invariant with every insertion and deletion, but the book mentions that a regular BBST would work. Their way of reversing intersecting segments may only apply to the augmented BBST, though. I believe due to the way I balance the tree, the "reversing" gets undone. Because of this, some intersection points of "new neighbor segments" get missed. 
- Unless I explicitly check for a point-type at an event/stopping point, I get inconsistent results when the visual displays as "static" (solve for intersections, then plot the results) vs. "animate" (display each stopping/event point), despite both paths using the same event handler and having the same debug output for all events. This leads me to believe that there is something off with `pyplot.plot()` while either `animation` or `plot()` runs, and in the rounding or precision for `Segment.interior(<Point>)` when it calculate if an event point is contained on a line segment, i.e. an intersection point is reporting false for one or more line segments that it is on during this check.
- The output visual is also not consistent between my local machine and when I run on halligan. It may be due to different versions of the `matplotlib` package that I rely on for the graphing. 


## References 
- [`pyplot.plot()`](https://matplotlib.org/2.0.2/api/pyplot_api.html#matplotlib.pyplot.plot)
- Rougier. [matplotlib-tutorial](https://github.com/rougier/matplotlib-tutorial). Aug 21, 2015. 
- March, Charles. [Computation Geometry in Python: From Theory to Application](https://www.toptal.com/python/computational-geometry-in-python-from-theory-to-implementation). Toptal. 2022.
- Mark de Berg, Otfried Cheong, Marc van Kreveld, and Mark Overmars. 2008. Computational Geometry: Algorithms and Applications (3rd ed. ed.). Springer-Verlag TELOS, Santa Clara, CA, USA.
    - Section 2.1: Line Segment Intersection
