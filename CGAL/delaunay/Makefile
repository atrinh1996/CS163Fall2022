CXX = clang++-14
LDFLAGS = -g3 
CFFLAGS= -Wall -Wextra -pedantic -g3
EXEC = delaunay

%.o: %.c 
	${CXX} ${CFFLAGS} -c -o $@ $<

delaunay: delaunay.o
	${CXX} -o $@ $^ ${LDFLAGS}


clean:
	rm *.o ${EXEC}