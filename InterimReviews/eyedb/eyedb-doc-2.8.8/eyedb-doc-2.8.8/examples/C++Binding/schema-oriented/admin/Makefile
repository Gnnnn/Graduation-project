prefix=/home/francois/projects/eyedb/install
include ${prefix}/share/eyedb/Makefile.eyedb

CXXFLAGS += $(EYEDB_CXXFLAGS) $(EYEDB_CPPFLAGS) -I${prefix}/share/doc/eyedb/examples/C++Binding/schema-oriented/share
LDFLAGS += ${EYEDB_LDFLAGS}
LDLIBS += ${EYEDB_LDLIBS}

all: admin

admin: admin.o
	$(CXX) $(LDFLAGS) -Wl,-R$(EYEDB_LIBDIR) -o $@ $^ $(LDLIBS)

init:

clean:
	rm -f *.o admin
