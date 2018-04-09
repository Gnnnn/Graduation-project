prefix=/home/francois/projects/eyedb/install
include ${prefix}/share/eyedb/Makefile.eyedb

CXXFLAGS += $(EYEDB_CXXFLAGS) $(EYEDB_CPPFLAGS)
LDFLAGS += ${EYEDB_LDFLAGS}
LDLIBS += ${EYEDB_LDLIBS}

all: query

query: query.o
	$(CXX) $(LDFLAGS) -Wl,-R$(EYEDB_LIBDIR) -o $@ $^ $(LDLIBS)

clean:
	rm -f *.o query
