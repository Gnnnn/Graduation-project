prefix=/home/francois/projects/eyedb/install
include ${prefix}/share/eyedb/Makefile.eyedb

all: Query.class

Query.class: Query.java
	CLASSPATH=$(EYEDB_CLASSPATH):. javac $^

clean:
	rm -f *.class
