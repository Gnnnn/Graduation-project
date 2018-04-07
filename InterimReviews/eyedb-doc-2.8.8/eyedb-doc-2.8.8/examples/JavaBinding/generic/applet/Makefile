prefix=/home/francois/projects/eyedb/install
include ${prefix}/share/eyedb/Makefile.eyedb

all: Test.class

Test.class: Test.java
	CLASSPATH=$(EYEDB_CLASSPATH):. javac $^

clean:
	rm -f *.class

