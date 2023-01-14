from Point import Point 
from Segment import Segment
from EventQueue import EventQueue, EventQueueNode
from AVLTree import AVLTree, TreeNode

class LineSegmentIntersection():
    def __init__(self):
        self.statusDS   = AVLTree()     # BBST: key is the y-coord
        self.eventQueue = EventQueue()  # Priority Queue
        self.result = []
        self.SweepX = None

    ## segments are tuple list: [(p1, p2), ...]
    ## p1 and p2 are each point coordinate tuples: (x, y)
    ## Insert all current endpoints from the segment list into the event queue
    ## status tree already initialized to empty. 
    def initializeDataStructures(self, segments):
        for seg_num, seg in enumerate(segments):
            p1, p2 = seg 

            # create a Segment from p1, p2
            s = Segment(p1, p2)
            label = s.label

            # insert the left and right end points into eventQueue 
            self.eventQueue.insert(s.left_endpoint, ({label}, s.left_endpoint, {s}))
            self.eventQueue.insert(s.right_endpoint, ({label}, s.right_endpoint, {s}))

    # must have called initializeDataStructures() prior to calling compute
    # computes all intersection points, and reports a set of event points in a list 
    def computeIntersections(self):
        while (not self.eventQueue.empty()):
            # Get next stopping point 
            eventNode = self.nextStop()
            if (eventNode):
                # (label, point, segment) = eventNode.value
                self.printEvent(eventNode)

                # Do Event Handling 
                self.handleEventPoint(eventNode)
                
        return self.result

    # reports the next stopping point as an EventQueueNode
    def nextStop(self):
        node = self.eventQueue.remove()
        return node 

    # reports the next stopping point upon an event; 
    # Best for "animated" demo
    def nextEvent(self):
        node = self.eventQueue.remove()

        if (node): 
            (_, point, _) = node.value
            self.printEvent(node)

            # Do Event Handling 
            self.handleEventPoint(node)

            # return the point for animation
            # return (point.x, point.y)
            return point
        else:
            # print("No event point")
            return None

    # At a stopping point, process the point and data structures
    def handleEventPoint(self, eventNode):
        (label, p, seg_set) = eventNode.value
        self.SweepX = p.x

        # L(p) is the set of Segments whose left_endpoint is p
        L = set()
        for seg in seg_set:
            if (seg.left_endpoint == p):
                L.add(seg)

        # R(p) is the set of Segments whose right_endpoint is p
        # C(p) is the sef of Segments found that contain p in their interior
        # for each segment currently in the status tree, check if p is on segment
        R = set()
        C = set()
        statusList = self.statusDS.inorder()
        self.printStatus(statusList)
        for seg in statusList:
            # segment.setSweepX(self.SweepX)
            if (seg.interior(p)):
                # print(f'[handleEventPoint]: adding to C(p): seg {seg}')
                C.add(seg)
            
            if (seg.right_endpoint == p):
                # print(f'[handleEventPoint]: adding to R(p)')
                R.add(seg)

        # union the three sets 
        LR = L.union(R)
        LC = L.union(C)
        RC = R.union(C)
        LRC = LR.union(C)
        
        # report p is an intersection
        if (len(LRC) > 1 or p.ptype == 2): 
            # print(f'p({p.x},{p.y}) is an intersection of segments {label}')
            ipoint = Point(p.x, p.y, 2)
            self.result.append(ipoint)

        # delete segments in RC from status tree 
        # print(f'len(RC) = {len(RC)}')
        for seg in RC:
            key_height = seg.heightAtSweep()
            print(f'[handleEventPoint] Deleting from RC: Seg {seg}, key={key_height}')
            self.statusDS.remove_recursive(key_height)
        # statusList1 = self.statusDS.inorder()
        # self.printStatus(statusList1)

        # insert segments in LC
        for seg in LC:
            seg.setSweepX(self.SweepX)
            key_height = seg.heightAtSweep()
            print(f'[handleEventPoint] Inserting from LC: {seg}, key={key_height}')
            self.statusDS.insert_recursive(key_height, seg)

        
        # statusList2 = self.statusDS.inorder()
        statusList2 = self.statusDS.inorder()
        self.printStatus(statusList2)
        lower = None 
        upper = None 
        # print(f'[handleEventPoint] statusList2: {statusList2}')
        for seg in statusList2:
            # seg.setSweepX(self.SweepX)
            upper = seg 

            ## print
            lower_label = None 
            upper_label = None  
            if (lower):
                lower_label = lower.label
            if (upper):
                upper_label = upper.label
            # print(f'Finding Event with Segment {lower_label} and Segment {upper_label}')


            self.findNewEvent(lower, upper, p)
            lower = upper
    
    # Find next intersection point of segment left and right. 
    # Put only those beyond the sweep line / event point into the evenet Queue.
    def findNewEvent(self, seg_left, seg_right, currEventPoint):
        # print(f'[findNewEvent] Start')
        # if l and r intersect to the RIGHT of the sweep line, 
        #   or on the sweep line and above current event point p,
        #   AND the intersection is not yet in the event Queue:
        #       THEN: Intesert the intersection point into eventQueue
        if (seg_left and seg_right):
            llabel = seg_left.label
            rlabel = seg_right.label
            intersection_point = seg_left.intersection(seg_right)

            if (intersection_point):
                # print(f'[findNewEvent] Intersection point found {seg_left} {seg_right}: ({intersection_point.x},{intersection_point.y})')

                if (intersection_point > currEventPoint and 
                    intersection_point < seg_left.right_endpoint and 
                    intersection_point < seg_right.right_endpoint):
                    print(f'[findNewEvent] Intersection point inserting: ({intersection_point.x},{intersection_point.y}) for Seg {seg_left} and {seg_right}')
                    self.eventQueue.insert(intersection_point, ({llabel, rlabel}, intersection_point, {seg_left, seg_right}))
            #     else: 
            #         print(f'[findNewEvent] Intersection point NOT inserting')

            # else:
            #     print(f'[findNewEvent] Intersection point NOT found')


    def printEvent(self, eventNode):
        (label, point, seg_set) = eventNode.value
        ptype = None
        if (point.ptype == 0):
            ptype = "a left endpoint"
        elif (point.ptype  == 1):
            ptype = "a right endpoint"
        else: 
            ptype = "an intersection point"

        print(f'p({point.x},{point.y}) is {ptype} of segment {label}')

    def printStatus(self, segmentList):
        print("Segment List:")
        for seg in segmentList:
            print(f'Segment {seg}')
