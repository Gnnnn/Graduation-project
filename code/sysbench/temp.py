import re 

string1="sysbench 1.0.14 (using bundled LuaJIT 2.1.0-beta2)\
\
Running the test with following options:\
Number of threads: 20\
Initializing random number generator from current time\
\
\
Initializing worker threads...\
\
Threads started!\
\
SQL statistics:\
    queries performed:\
        read:                            32774\
        write:                           9181\
        other:                           4620\
        total:                           46575\
    transactions:                        2279   (226.87 per sec.)\
    queries:                             46575  (4636.55 per sec.)\
    ignored errors:                      62     (6.17 per sec.)\
    reconnects:                          0      (0.00 per sec.)\
\
General statistics:\
    total time:                          10.0431s\
    total number of events:              2279\
\
Latency (ms):\
         min:                                   13.14\
         avg:                                   87.95\
         max:                                  225.39\
         95th percentile:                      101.13\
         sum:                               200434.09\
\
Threads fairness:\
    events (avg/stddev):           113.9500/1.94\
    execution time (avg/stddev):   10.0217/0.01"
    
searchObj = re.search( r'(.*) read:\s{27} (\d{5}) ', string1, re.M|re.I)
read = int(searchObj.group(2))
print ("read : ", read)
searchObj = re.match( r'(.*) write:\s{26} (.{10}) ', string1, re.M|re.I)
write = int(searchObj.group(2))
print ("write : ", write)
print ("write : ", write+read)
searchObj = re.search( r'(.*) total:\s{26} (.*?) .*', string1, re.M|re.I)
total = int(searchObj.group(2))
print ("total : ", total)
searchObj = re.search( r'(.*) ignored errors:\s{20} (.{5})', string1, re.M|re.I)
error = int(searchObj.group(2))
print ("error : ", error)