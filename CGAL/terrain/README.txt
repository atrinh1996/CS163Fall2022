Instruction for using CGAL
Ryan Coleman, April 2003

1. Log onto sun.eecs.tufts.edu from either the NT labs or the Sun lab.
The maxterms/connections off campus are too slow to actually run geomview
from the unix machines.

2. Put the three attached/included files in a directory, make a directory
within it called data and put points3 in it.

3. Run `use cgal`

4. The makefile _should_ work if you type make or make terrain.  It takes
a long time to compile (relative to programs that don't do a lot of
linking to libraries).

5. You may have to run `setenv DISPLAY computer.eecs.tufts.edu:0.0` where
computer is the machine you are using, like Beethoven in the NT lab or c15
in the sun lab.

6. Typing `terrain` should now work.  Other problems you might have are
not having geomview in your path.

----

Yeah, that's about it.  When you run terrain, it runs geomview for you,
and runs a Voronoi diagram then a Delaunay triangulation.  There is some
output telling you this, it also is documented in the code a little bit.
