#!/bin/sh
prefix=/home/francois/projects/eyedb/install
exec_prefix=/home/francois/projects/eyedb/install
bindir=/home/francois/projects/eyedb/install/bin

set -e
SCHEMA=$1
DATABASE=person_c

echo Creating the database $DATABASE
echo $bindir/eyedbadmin database create $DATABASE
$bindir/eyedbadmin database create $DATABASE

echo
echo Changing the default access to read/write
echo $bindir/eyedbadmin database defaccess $DATABASE rw
$bindir/eyedbadmin database defaccess $DATABASE rw

echo
echo Updating the database $DATABASE with the schema person...
echo $bindir/eyedbodl --update --database=$DATABASE $SCHEMA
$bindir/eyedbodl --update --database=$DATABASE $SCHEMA

echo
echo Creating a few instances in the database $DATABASE ...
echo $bindir/eyedboql -d $DATABASE -w
$bindir/eyedboql -d $DATABASE -w << EOF
john := new Person(
    name        : "john", 
    age         : 32,
    addr.street : "clichy",
    addr.town   : "Paris",
    cstate      : Sir);
mary := new Person(
    name        : "mary", 
    age         : 30,
    addr.street : "clichy",
    addr.town   : "Paris",
    spouse      : john,
    cstate      : Lady);
for (x in interval(1, 4))
 add (new Car(brand : "renault", num : x+100)) to john->cars;
henry := new Employee(
   name        : "henry",
   salary      : 100000,
   age         : 32,
   addr.street : "parmentier",
   addr.town   : "Paris",
   cstate      : Sir);
nadou := new Employee(
   name        : "nadou",
   salary      : 20000,
   age         : 30,
   addr.street : "parmentier",
   addr.town   : "Paris",
   spouse      : henry,
   cstate      : Sir);
for (x in interval(1, 8))
 add (new Car(brand : "citroen", num : x+100)) to nadou->cars;
\commit
\quit
EOF