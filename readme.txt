Instruction on running my program:
For Part 1, please implement my program using python3. You can implemented it as
python3 inverted_index.py doc1.txt doc2.txt … . (doc1 and doc2 are just examples.
And you can add any txt files as you like). It should created a JASON file caeed
inverted_index.
For Part 2, please implement my program using python3. Please note, the search2.py
is searching on the JASON file created by Part 1, which means, you must implement
part 1 first. Ensure inverted_index file is created. Then you can implement part 2 by
python3 search2.py. It would ask you to type query or Boolean queries. Please then
type the query or queries as you want.
For Part 3, This is done in python2. it is still divided into 2 parts: creating
inverted_index and doing the search based on that. You need to first upload your txt
file into Hadoop folder by You need to run: Hadoop fs -copyFromLocal 1342.txt
/user/cloudera/inputAssignment2/1342.txt
Then you can run mapper and reducer program by
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming2.6.0-mr1-cdh5.12.0.jar -file mapper.py -mapper "python mapper.py" -file
reducer.py -reducer "python reducer.py" -input /user/cloudera/inputAssignment2 -
output /user/cloudera/outputAssignment39
After that, you can save the inverted index by (the output file must name as “result”,
you cannt change the name):
hadoop fs -cat /user/cloudera/outputAssignment39/*>result
The final step is to run: python search3.py. It would ask you to type query or
Boolean queries. Please then type the query or queries as you want.
