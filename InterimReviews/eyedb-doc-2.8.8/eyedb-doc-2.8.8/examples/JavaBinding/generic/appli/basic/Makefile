prefix=/home/francois/projects/eyedb/install
include ${prefix}/share/eyedb/Makefile.eyedb

all: Basic.class

Basic.class: Basic.java
	CLASSPATH=$(EYEDB_CLASSPATH):. javac $^

clean:
	rm -f *.class

