prefix=/home/francois/projects/eyedb/install
include ${prefix}/share/eyedb/Makefile.eyedb

all: PersonTest.class

PersonTest.class: PersonTest.java
	CLASSPATH=$(EYEDB_CLASSPATH):.:../share javac $^

clean:
	rm -f *.class
