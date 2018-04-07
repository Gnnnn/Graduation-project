prefix=/home/francois/projects/eyedb/install
include ${prefix}/share/eyedb/Makefile.eyedb

all: Store.class

Store.class: Store.java
	CLASSPATH=$(EYEDB_CLASSPATH):. javac $^

clean:
	rm -f *.class
