
CXX = clang++-14
LDFLAGS = -g3 
CFFLAGS= -Wall -Wextra -pedantic -g3
EXEC = points_and_segment

%.o: %.c 
	${CXX} ${CFFLAGS} -c -o $@ $<

points_and_segment: points_and_segment.o
	${CXX} -o $@ $^ ${LDFLAGS}


clean:
	rm *.o ${EXEC}