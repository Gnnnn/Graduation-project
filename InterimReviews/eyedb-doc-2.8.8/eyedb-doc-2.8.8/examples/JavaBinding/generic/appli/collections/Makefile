prefix=/home/francois/projects/eyedb/install
include ${prefix}/share/eyedb/Makefile.eyedb

all: Collections.class

Collections.class: Collections.java
	CLASSPATH=$(EYEDB_CLASSPATH):. javac $^

clean:
	rm -f *.class
