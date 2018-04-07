prefix=/home/francois/projects/eyedb/install
include ${prefix}/share/eyedb/Makefile.eyedb

all: person/Person.class

person/Person.java: schema.odl
	$(EYEDB_ODL) --gencode=Java --package=person --output-dir=person $<

person/Person.class: person/Person.java
	CLASSPATH=$(EYEDB_CLASSPATH):. javac person/*.java

clean:
	rm -f person/*.class person/*.java
