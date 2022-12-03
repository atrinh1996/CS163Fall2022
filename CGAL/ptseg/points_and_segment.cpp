#include <iostream>
#include <CGAL/Simple_cartesian.h>

using namespace std;

/* Typedefs */
typedef CGAL::Simple_cartesian<double> Kernal;
typedef Kernal::Point_2 Point_2;
typedef Kernal::Segment_2 Segment_2;
/*************/

int main() {
    Point_2 p(1, 1);
    Point_2 q(10, 10);

    cout << "p: " << p << endl;
    cout << "q: " << q.x() << " " << q.y() << endl;

    cout << "squared_distance(p, q): " << CGAL::squared_distance(p, q) << endl;

    /*****************************************************/
    Segment_2 s(p, q);
    Point_2 m(5, 9);

    cout << "m: " << m << endl;
    cout << "squared_distance(segment(p,q), m): " << CGAL::squared_distance(s, m) << endl;
    /*****************************************************/

    cout << "p, q, and m ";

    switch (CGAL::orientation(p, q, m))
    {
        case CGAL::COLLINEAR:
            cout << "are collinear." << endl;
            break;
        case CGAL::LEFT_TURN:
            cout << "make a left turn." << endl;
            break;
        case CGAL::RIGHT_TURN:
            cout << "make a right turn." << endl;
            break;
        default:
            break;
    }
    /*****************************************************/

    cout << "midpoint(p,q): " << CGAL::midpoint(p,q) << endl;

    return 0;

}